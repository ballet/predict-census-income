from ballet import Feature
from sklearn.preprocessing import OneHotEncoder

input = "ST_x"
transformer = OneHotEncoder()
name = "one_hot_state"
description = "convert the state id to a one hot vector."
feature = Feature(input, transformer, name=name, description=description)
