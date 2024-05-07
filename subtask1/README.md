# Task 1 metrics comparison


|  Model    | F1 @ epoch 6 | F1 @ epoch 10     | 
|-----------|------------|-----------|
| [PlanTL-GOB-ES](https://huggingface.co/PlanTL-GOB-ES/roberta-base-biomedical-clinical-es)     | 0.750      | ??? | 
| [CLIN-X-ES](https://huggingface.co/llange/xlm-roberta-large-spanish-clinical)      | 0.804      | 0.812     | 
| [pretrained-CLIN-X-ES](https://huggingface.co/llange/xlm-roberta-large-spanish-clinical)   | 0.804  | 	0.818     | 
| [deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) | 0.769  | ??? | 
| [ddeberta-v3-large-dapt-scientific-papers-pubmed-tapt](https://huggingface.co/domenicrosati/deberta-v3-large-dapt-scientific-papers-pubmed-tapt) | 0.771  | ??? |

NOTE: pretrained-CLIN-X-ES is the CLIN-X-ES model pretrained on the IDENTIFICATION OF COLON
CANCER RISK FACTORS dataset
