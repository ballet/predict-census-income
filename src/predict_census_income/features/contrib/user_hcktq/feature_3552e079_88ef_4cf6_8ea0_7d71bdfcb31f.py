from ballet import Feature
from ballet.eng import NullFiller, ValueReplacer

input = ["HINS1", "HINS2", "HINS3", "HINS4", "HINS5", "HINS6", "HINS7"]
transformer = [
    NullFiller(replacement=0),
    ValueReplacer(2, 0),
    lambda df: df.sum(axis=1) > 0,
]  # TODO - function, transformer-like, or list thereof
name = "insurance"  # TODO - str
description = "has any form of insurance"  # TODO - str
feature = Feature(input, transformer, name=name, description=description)
