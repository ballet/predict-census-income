from ballet import Feature
from ballet.eng import NullFiller

input = ["JWAP", "JWDP"]  # TODO - str or list of str
transformer = [lambda df: df["JWAP"] - df["JWDP"], NullFiller()]
# TODO - function, transformer-like, or list thereof
name = "JWAP - JWDP"  # TODO - str
description = "Time of arrival for work minus Time of departure for work"  # TODO - str
feature = Feature(input, transformer, name=name, description=description)
