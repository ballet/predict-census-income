from ballet import Feature
from ballet.eng.sklearn import SimpleImputer

input = ["GRNTP"]
transformer = SimpleImputer(
    strategy="mean"
)  # TODO - function, transformer-like, or list thereof
name = "Imputed GRNTP"  # TODO - str
feature = Feature(input=input, transformer=transformer, name=name)
