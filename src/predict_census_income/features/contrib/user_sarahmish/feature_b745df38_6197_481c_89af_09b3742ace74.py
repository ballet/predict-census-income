from ballet import Feature

input = ["ELEP", "FULP", "GASP", "WATP"]  # TODO - str or list of str
transformer = (
    lambda df: df.sum(axis=1),
)  # TODO - function, transformer-like, or list thereof
name = "Total Auxiliary Cost"  # TODO - str
description = "The total cost of electricity, fuel, gas, and water on a monthly bases."  # TODO - str
feature = Feature(input, transformer, name=name, description=description)
