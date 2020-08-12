from ballet import Feature
from sklearn.preprocessing import OneHotEncoder
from ballet.eng.base import BaseTransformer


class OneHotEncoderWithNan(BaseTransformer):
    def __init__(self):
        self.onehot = OneHotEncoder()

    def fit(self, X, y=None):
        X = X.fillna(0)
        self.onehot.fit(X, y)
        return self

    def transform(self, X):
        X = X.fillna(0)
        X = self.onehot.transform(X)
        return X


input = "FES"  # TODO - str or list of str
transformer = (
    OneHotEncoderWithNan()
)  # TODO - function, transformer-like, or list thereof
name = "one-hot family-employment-status"  # TODO - str
description = "one-hot encoded family-employment-status"  # TODO - str
feature = Feature(input, transformer, name=name, description=description)
