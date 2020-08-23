from ballet import Feature
import pandas as pd

input = ["BLD"]
transformer = lambda df: pd.get_dummies(df["BLD"], prefix="bld")
name = "building type"
description = "onehot building type"
feature = Feature(input, transformer, name=name, description=description)
