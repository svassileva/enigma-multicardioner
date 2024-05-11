# Task 2 metrics comparison


These are metrics on full texts

|           | F1 overall | F1-es     | F1-it     | F1-en     |
|-----------|------------|-----------|-----------|-----------|
| NuNER     | 0.848      | 0.849     | 0.852     | 0.844     |
| XLMR      | 0.851      | 0.860     | 0.845     | 0.849     |
| XLMR-resq | **0.871**  | **0.875** | **0.863** | **0.873** |

These are metrics on splitted sentences

|           | F1 overall | 
|-----------|------------|
| XLMR-resq     | 0.850      | 
| XLMR-resq+it      | 0.865      | 
| XLMR-resq+it+filtering | **0.872**  |
| XLMR-resq+it+filtering+undersampling | 0.866 |
