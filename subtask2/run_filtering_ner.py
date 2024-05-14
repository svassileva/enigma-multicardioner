from transformers import AutoTokenizer
from transformers import pipeline
from transformers import AutoModelForTokenClassification
import pandas as pd
import torch
from tqdm.auto import tqdm
import evaluate

tqdm.pandas()
metric = evaluate.load('seqeval')
map = {0: "O", 1: "B-FARMACO", 2: "I-FARMACO"}
MODEL_CLASS = "aaaksenova/xlmr_drug_classifier"
MODEL_NER = "aaaksenova/xlmr_medical"
tokenizer_kwargs = {'padding': True, 'truncation':True, 'max_length':512}


def align_labels_with_tokens(labels, word_ids):
    new_labels = []
    current_word = None
    for word_id in word_ids:
        if word_id != current_word:
            # Start of a new word!
            current_word = word_id
            label = -100 if word_id is None else labels[word_id]
            new_labels.append(label)
        elif word_id is None:
            # Special token
            new_labels.append(-100)
        else:
            # Same word as previous token
            label = labels[word_id]
            # If the label is B-XXX we change it to I-XXX
            if label % 2 == 1:
                label += 1
            new_labels.append(label)

    return new_labels


# For now it predicts label per token. It could be changed to token classification pipeline with span prediction
def predictions(tokens, labels):
    out = classifier(' '.join(tokens), **tokenizer_kwargs)
    if out[0]['label'] == "ent":
        inputs = tokenizer(tokens, return_tensors="pt", is_split_into_words=True, truncation=True)
        word_ids = inputs.word_ids(0)
        with torch.no_grad():
            logits = model(**inputs.to('cuda')).logits
        predictions = torch.argmax(logits, dim=2)
        predicted_token_class = [model.config.id2label[t.item()] for t in predictions[0]]
        return align_labels_with_tokens(labels, word_ids), predicted_token_class
    inputs = tokenizer(tokens, return_tensors="pt", is_split_into_words=True, truncation=True)
    word_ids = inputs.word_ids(0)
    return align_labels_with_tokens(labels, word_ids), ["O"] * len(word_ids)


classifier = pipeline(task="text-classification", model=MODEL_CLASS, device='cuda')
tokenizer = AutoTokenizer.from_pretrained(MODEL_NER)
model = AutoModelForTokenClassification.from_pretrained(MODEL_NER).to('cuda')
df = pd.read_json('./data/dev.json')  # Here should be the data for evaluation
df[['true_aligned', 'preds']] = df[['tokens', 'ner_tags']].progress_apply(lambda x: predictions(*x), axis=1, result_type="expand")
df.to_json('predictions.json')

predictions = list(df.preds.values)
labels = list(df.true_aligned.values)
true_labels = [[map[l] for l in label if l != -100] for label in labels]
true_predictions = [[p for (p, l) in zip(prediction, label) if l != -100] for prediction, label in zip(predictions, labels)]

all_metrics = metric.compute(predictions=true_predictions, references=true_labels)
print(all_metrics)
