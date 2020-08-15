from ballet import Feature
from ballet.eng import NullFiller

input = ["DIVISION_x", "PWGTP3"]  # TODO - str or list of str
transformer = [
    lambda df: np.log(1 + df["DIVISION_x"]) * np.log(1 + df["PWGTP3"]),
    NullFiller(),
]  # TODO - function, transformer-like, or list thereof
name = "Highest Variance"  # TODO - str
description = "Agreggation of highest variance features"  # TODO - str
feature = Feature(input, transformer, name=name, description=description)
