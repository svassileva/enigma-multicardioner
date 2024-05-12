# 1. Introduction

Scripts to compute DisTEMIST evaluation metrics.
Written by [TeMU/BSC](https://github.com/TeMU-BSC/distemist_evaluation_library)

# 2. Requirements

+ Python3
+ pandas

# 3. Execution
+ MultiCardioNER Entities 

```
cd src  
python3 main.py -g path/to/gold/entities/multicardioner_track1_cardioccc_dev.tsv -p path/to/predicted/entities/multicardioner_track1_cardioccc_dev_predictions.tsv -s ner
```
