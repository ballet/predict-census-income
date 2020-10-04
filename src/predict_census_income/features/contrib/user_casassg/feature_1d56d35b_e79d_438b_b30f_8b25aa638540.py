from ballet import Feature

from ballet.eng import ConditionalTransformer
from ballet.eng.sklearn import SimpleImputer

input = ["JWTR", "JWRIP", "JWMNP"]  # TODO - str or list of str


def calculate_travel_budget(df):
    if (df["JWTR"] == 1.0).all():
        return df["JWMNP"] * df["JWRIP"]
    return df["JWMNP"] * df["JWTR"]


transformer = [
    calculate_travel_budget,
    SimpleImputer(strategy="mean"),
]  # TODO - function, transformer-like, or list thereof
name = "work_travel_combined"  # TODO - str
description = "Combine data for time to travel to work with vehicle. Lower value, the most likely they have higher income"  # TODO - str
feature = Feature(input, transformer, name=name, description=description)
