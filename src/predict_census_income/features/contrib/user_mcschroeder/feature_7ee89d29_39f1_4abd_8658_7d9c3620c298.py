from ballet import Feature
from ballet.eng import NullFiller

input = ["JWAP", "JWMNP"]
transformer = NullFiller()
name = "Commute"
description = "Travel time and time of arrival at work"
feature = Feature(input, transformer, name=name, description=description)
