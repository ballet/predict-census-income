from ballet import Feature
from ballet.eng import NullFiller

input = ["MRGP", "MHP", "GASP", "FULP", "ELEP", "RNTP"]
transformer = [lambda df: df.sum(axis=1), NullFiller()]
name = "Monthly_Basic_Living_Cost"
description = "total basic monthly living cost including rent, mortgage and utility"
feature = Feature(input, transformer, name=name, description=description)
