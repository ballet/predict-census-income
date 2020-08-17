from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import Binarizer

input = ["CONP"]
transformer = [NullFiller(), Binarizer(threshold=2000)]
name = "BCONP"
feature = Feature(input=input, transformer=transformer, name=name)
