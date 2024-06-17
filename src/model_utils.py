# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from pickle import load
import nltk
from nltk.stem.porter import *


def make_inference(in_model: Pipeline, in_data: dict) -> dict[str, list]:
    """Return the result of predictions for in_data using in_model."""
    in_data_tfidf = in_model[1].transform(in_data)
    result = {}

    for target_variable, model in in_model[0].items():
        preds = model.predict(in_data_tfidf)
        result[target_variable] = preds
    return result


def load_model(path: str) -> Pipeline:
    """Return the model being read which stored on the path."""
    with open(path, "rb") as file:
        model: Pipeline = load(file)

    return model
