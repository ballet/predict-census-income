from ballet import Feature
from ballet.eng.sklearn import MinMaxScaler


def fillna(df):
    df[["SCHG", "SCHL"]] = df[["SCHG", "SCHL"]].fillna(0)
    df["COW"] = df["COW"].replace("b", 9)
    df["COW"] = df["COW"].fillna(9)
    return df


def filter_func(df):
    df["SCHG"].astype("int")
    df["SCHG"] = df["SCHG"].apply(lambda x: 1 if x > 16 else 0)  # graduate
    df["SCHL"].astype("int")
    df["SCHL"] = df["SCHL"].apply(lambda x: 1 if x > 21 else 0)  # bachelor
    df["EDU"] = df["SCHL"] + df["SCHG"]
    df["COW"].astype("int")
    df["COW"] = df["COW"].apply(lambda x: 1 if x < 7 and x >= 1 else 0)
    return df


input = ["SCHG", "SCHL", "COW"]  # TODO - str or list of str
transformer = [
    fillna,
    filter_func,
    lambda df: df[["EDU", "COW"]],
]  # TODO - function, transformer-like, or list thereof
name = "Education and Worker Class"  # TODO - str
description = "1st dim: whether attended college; 2st dim: whether working with payment"  # TODO - str
feature = Feature(input, transformer, name=name, description=description)
