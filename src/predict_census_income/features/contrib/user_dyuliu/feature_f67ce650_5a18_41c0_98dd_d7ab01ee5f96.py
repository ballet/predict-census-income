from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import Binarizer

input = []
for i in range(80):
    input.append("WGTP{}".format(i + 1))
transformer = [
    lambda df: df.sum(axis=1),
    NullFiller()
    #     Binarizer(threshold=3000)
]
name = "WGTP Sum"
feature = Feature(input=input, transformer=transformer, name=name)
