from ballet import Feature
from ballet.eng import NullFiller

input = ["NP", "SCHL"]

transformer = [lambda df: df["SCHL"] / (1 + df["NP"]), NullFiller()]

name = "Education Household Average"
description = "Ratio between level of education and number of person in household."
feature = Feature(input, transformer, name=name, description=description)
