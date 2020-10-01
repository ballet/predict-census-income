# X_trainllet import Feature
from ballet import Feature
from ballet.eng.sklearn import SimpleImputer
from ballet.eng.sklearn import StandardScaler

input = ["POVPIP", "WKHP", "TAXAMT"]  # TODO - str or list of str
transformer = [
    SimpleImputer(strategy="mean"),
    StandardScaler(),
]  # TODO - function, transformer-like, or list thereof
name = "TOP3_PINCP_CORR"  # TODO - str
description = (
    "TOP 3 corr featuers to PINCP. Note, Prone to multicollinearity!"  # TODO - str
)
feature = Feature(input, transformer, name=name, description=description)
