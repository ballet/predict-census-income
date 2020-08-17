from ballet import Feature
from ballet.eng.sklearn import MinMaxScaler, StandardScaler

input = "AGEP"
transformer = MinMaxScaler()
name = "Age scaled"
description = "Age scaled from 0 to 1"
feature = Feature(input, transformer, name=name, description=description)
