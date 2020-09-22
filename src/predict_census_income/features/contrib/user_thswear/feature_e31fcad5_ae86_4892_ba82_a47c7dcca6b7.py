from ballet import Feature
from ballet.eng.sklearn import SimpleImputer

input = "ELEP"  # TODO - str or list of str
transformer = SimpleImputer(
    strategy="mean"
)  # TODO - function, transformer-like, or list thereof
name = "Imputed Electric Cost"  # TODO - str
description = "Higher electric bill => more money"  # TODO - str
feature = Feature(input, transformer, name=name, description=description)
