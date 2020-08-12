from ballet import Feature
from ballet.eng.base import BaseTransformer
import math
import pandas as pd
import numpy as np

input = ["BROADBND", "ACCESS"]


class Internet(BaseTransformer):
    def fit(self, X, y=None):
        X[np.isnan(X)] = 0

        X[:, 0] = np.where(
            X[:, 0] == [2], 0, X[:, 0]
        )  # If 'No' or 'N/A' for Broadband, replace with 0
        X[:, 1] = np.where(
            X[:, 1] == 2, 1, X[:, 1]
        )  # If 'Yes' for Access, replace with 1
        X[:, 1] = np.where(
            X[:, 1] == [3], 0, X[:, 1]
        )  # If 'No' or 'N/A' for Access, replace with 0

        self.has_internet_ = X
        return self

    def transform(self, X):
        # The feature vector is 1 if they have both access and broadband
        X = np.sum(self.has_internet_, axis=1) / 2
        return X


transformer = Internet()
name = "Connected"
description = "Does a person have access to both a Cellular data plan for a smartphone or other mobile device and access to the Internet"
feature = Feature(input, transformer, name=name, description=description)
