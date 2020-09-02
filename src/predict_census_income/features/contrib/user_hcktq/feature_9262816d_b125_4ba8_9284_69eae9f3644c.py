from ballet import Feature
from ballet.eng import NullFiller, ValueReplacer

input = [
    "DDRS",
    "DEAR",
    "DEYE",
    "DOUT",
    "DPHY",
    "DRATX",
    "DREM",
]
transformer = [
    NullFiller(replacement=0),
    ValueReplacer(2, 0),
    lambda df: df.sum(axis=1) > 0,
]  # TODO - function, transformer-like, or list thereof
name = "disability"  # TODO - str
description = "has any kind of disability"  # TODO - str
feature = Feature(input, transformer, name=name, description=description)
