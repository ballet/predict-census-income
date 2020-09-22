from ballet import Feature
from ballet.eng.sklearn import SimpleImputer

input = ["JWRIP"]
transformer = SimpleImputer(strategy="mean")
name = "Imputed JWRIP"
description = "A feature created by Zhihua."
feature = Feature(
    input=input, transformer=transformer, name=name, description=description
)
