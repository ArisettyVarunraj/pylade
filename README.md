# Language Identification tools

Usage:

```bash
python train.py \
    --implementation CavnarTrenkleImpl \
    --training-data training_set.csv \
    --corpus-reader TwitterCorpusReader \
    --output model.pickle

python evaluate.py \
    --model model.pickle \
    --test-data test_set.csv \
    --corpus-reader TwitterCorpusReader \
    --output results.json

python detect.py \
    --model model.pickle \
    --text "Put text here"
```

# Requirements

- python 3.5
- `nltk`
