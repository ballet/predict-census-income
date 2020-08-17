from ballet import Feature
from ballet.eng import NullFiller

input = "OCCP"  # TODO - str or list of str
transformer = [
    lambda df: np.sqrt(df),
    NullFiller(),
]  # TODO - function, transformer-like, or list thereof
name = "Square Root"  # TODO - str
description = None  # TODO - str
feature = Feature(input, transformer, name=name, description=description)
