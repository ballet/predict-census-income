from ballet import Feature
from ballet.eng import NullFiller

input = ["VALP", "NP"]
transformer = [lambda x: x["VALP"] / x["NP"], NullFiller()]
name = "Property value per household member"
description = "Property value divided by number of person in households"
feature = Feature(input, transformer, name=name, description=description)
