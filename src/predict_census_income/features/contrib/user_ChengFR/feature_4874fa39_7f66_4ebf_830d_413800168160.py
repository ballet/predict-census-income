from ballet import Feature
from ballet.eng.sklearn import SimpleImputer
from ballet.eng.external import MinMaxScaler

input = ["POVPIP"]  # TODO - str or list of str
transformer = [
    SimpleImputer(strategy="mean"),
    MinMaxScaler(),
]  # TODO - function, transformer-like, or list thereof
name = "Normed_POVPIP"  # TODO - str
description = "POVPIP normalized by minmax scaler."  # TODO - str
feature = Feature(input, transformer, name=name, description=description)
