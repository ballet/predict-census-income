from ballet import Feature
from ballet.eng import NullFiller
import numpy as np

input = ["WKL", "WKHP", "WKW"]
transformer = [
    lambda df: np.where(df["WKL"] == 1, df["WKHP"] * df["WKW"], 0),
    NullFiller(),
]
name = "Total working hours in the last 12 months"
description = (
    "If the person had worked in the last 12 months, calculate the total hours of work"
)
feature = Feature(input, transformer, name=name, description=description)
