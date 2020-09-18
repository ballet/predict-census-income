from ballet import Feature
from ballet.eng.sklearn import SimpleImputer
import numpy as np

input = "RESMODE"
transformer = SimpleImputer(missing_values=np.nan, strategy="constant", fill_value=0)
name = "Imputed Response Mode"
description = "Missing response modes values filled in with 0"
feature = Feature(input, transformer, name=name, description=description)
