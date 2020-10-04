input = ["CONP", "ELEP", "FULP", "GASP", "WATP"]
transformer = [lambda df: df.sum(axis=1), NullFiller()]
name = "Total Miscellaneous Costs"
feature = Feature(input=input, transformer=transformer, name=name)
