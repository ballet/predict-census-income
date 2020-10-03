from ballet import Feature
from ballet.eng.sklearn import SimpleImputer
import numpy as np

input = "JWAP"  # Time of arrival at work
transformer = [
    SimpleImputer(missing_values=np.nan, strategy="constant", fill_value=0.0),
    lambda df: np.where((df >= 70) & (df <= 124), 1, 0),
]
name = "If job has a morning start time"
description = "Return 1 if the Work arrival time >=6:30AM and <=10:30AM"
feature = Feature(input, transformer, name=name, description=description)
