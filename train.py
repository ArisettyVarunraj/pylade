#/usr/bin/env python
#! -*- coding: utf-8 -*-

from __future__ import division
from collections import defaultdict
import argparse
import logging
import sys

import utils

# def _str_to_class(class_name):
    # return next(corpus_reader for corpus_reader in CORPUS_READERS if corpus_reader.__name__ == class_name )
    # try:
    #     # return eval(class_name)
    #     return globals()[class_name]
    # except NameError as e:
    #     # TODO: Use logging
    #     print("No class with that name, sorry!")
    #     raise e

def _find_class_in_set(class_name, class_set):
    try:
        return next(class_item for class_item in class_set if class_item.__name__ == class_name )
    except StopIteration as exception:
        logging.error('The provided class name was not found in the available classes.')
        raise exception

def _find_corpus_reader(class_name):
    return _find_class_in_set(class_name, utils.CORPUS_READERS)

def _find_implementation(class_name):
    return _find_class_in_set(class_name, utils.IMPLEMENTATIONS)

def _parse_arguments():
    """Parse arguments provided from command-line and return them as a dictionary."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--debug',
        help="Activates debug mode",
        action="store_const", dest="loglevel", const=logging.DEBUG,
        default=logging.WARNING,
    )
    parser.add_argument(
        '-v', '--verbose',
        help="Activates verbose mode",
        action="store_const", dest="loglevel", const=logging.INFO,
    )
    parser.add_argument(
        '-i', '--implementation',
        help="Chosen method (e.g. CanvarTrenkle)",
        action="store", dest="implementation",
        default='CavnarTrenkleImpl'
    )
    parser.add_argument(
        '-t', '--training-data',
        help="Path for training data file (e.g. training_tweets.csv)",
        action="store", dest="training_data_file",
        default='training_data.csv'
    )
    parser.add_argument(
        '-c', '--corpus-reader',
        help="Corpus Reader class (e.g. TwitterCorpusReader)",
        action="store", dest="corpus_reader_class",
        default='TwitterCorpusReader'
    )
    parser.add_argument(
        '-o', '--output',
        help="Model output pickle file",
        action="store", dest="model_output_file",
        default='model.pickle'
    )

    return vars(parser.parse_args())

def start_training(arguments):
    import os # TODO: remove

    training_data_file = arguments['training_data_file']
    corpus_reader_class = _find_corpus_reader(arguments['corpus_reader_class'])
    training_corpus = corpus_reader_class(training_data_file)

    # languages =  training_corpus.available_languages()
    logging.info("Retrieving all documents from training corpus...")
    labeled_tweets = training_corpus.all_tweets() # TODO: rename this method into 'all_instances', 'all_rows' or similarly generic

    logging.info("Training model...")
    output_file = arguments['model_output_file']

    implementation = _find_implementation(arguments['implementation'])
    model = implementation().train(labeled_tweets, limit=5000)
    utils.save_as_pickle(model, output_file)


if __name__ == '__main__':
    arguments = _parse_arguments()
    utils._configure_logger(arguments['loglevel'])
    start_training(arguments)
