from ballet import Feature
from ballet.eng.sklearn import SimpleImputer

input = "WIF"  # TODO - str or list of str
transformer = SimpleImputer(
    strategy="mean"
)  # TODO - function, transformer-like, or list thereof
name = "Imputed HUPAC"  # TODO - str
description = "Mean imputed Workers in family during the past 12 months"  # TODO - str
feature = Feature(input, transformer, name=name, description=description)
