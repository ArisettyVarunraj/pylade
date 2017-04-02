# Pylade

`pylade` is a lightweight language detection tool written in Python. The tool provides a ready-to-use command-line interface, along with a more complex scaffolding for customized tasks.

The current version of `pylade` implements the *Cavnar-Trenkle N-Gram-based approach*. However, the tool can be further expanded with customized language identification implementations.

## Requirements

- python 3.4, 3.5
- `nltk`

## Installation

Download the repository and install using pip (locally):

```bash
$ git clone git@github.com:fievelk/language-detection.git
$ cd language-detection
$ pip install .
```

## Usage

For a quick use, simply give the following command from terminal:

```bash
pylade "Put text here"
# en
```
Done!

If you want to get deeper and use some more advanced features, please keep reading. **Note:** you can obtain more information about each of the following commands using the `--help` flag.

### Train a model on a training set

```bash
pylade_train \
    training_set.csv \
    --implementation CavnarTrenkleImpl \
    --corpus-reader TwitterCorpusReader \
    --output model.json \
    --train-args '{"limit": 5000, "verbose": "True"}'
```

### Evaluate a model on a test set

```bash
pylade_eval \
    test_set.csv \
    -m model.json \
    --corpus-reader TwitterCorpusReader \
    --output results.json \
    --eval-args '{"languages": ["it", "de"], "error_values": 8000}'
```

### Detect language of a text using a trained model

```bash
pylade \
    "Put text here" \
    -m model.json \
    --implementation CavnarTrenkleImpl \
    --output detected_language.txt \
    --predict-args '{"error_value": 8000}'
```

## Info

The default model (`data/model.json`) has been trained using `limit = 5000`. This value provides a good balance between computational performance and accuracy. Please note that this might change if you use your own data to train a new model.

## Tests

Give the command `tox` from the package root in order to perform tests.

Tests with `tox` require the following dependencies:

- `tox`
- `pytest`

### Customization

Different language deteection approaches can be implemented creating new classes that inherit from the `Implementation` class. This class should be considered as an interface whose methods are meant to be implemented by the inheriting class.

Customized corpus readers can be created the same way, inheriting from the `CorpusReader` interface instead.

### References

- Cavnar, William B., and John M. Trenkle. "N-gram-based text categorization." *Ann Arbor MI* 48113.2 (1994): 161-175.
