from ballet import Feature
from ballet.eng.sklearn import SimpleImputer

input = "ESP"  # TODO - str or list of str
transformer = SimpleImputer(
    strategy="most_frequent"
)  # TODO - function, transformer-like, or list thereof
name = "Imputed ESP"  # TODO - str
description = "Mode imputed employment status of parents"  # TODO - str
feature = Feature(input, transformer, name=name, description=description)
