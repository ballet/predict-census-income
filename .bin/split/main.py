#!/usr/bin/env python3

import pathlib
import shutil
import tempfile

import pandas as pd
from pypums import ACS
from sklearn.model_selection import train_test_split


def download_data(dst: pathlib.Path):
    dst.mkdir(exist_ok=True, parents=True)

    survey = ACS(
        year=2018, state="Massachusetts", survey="1-Year", person_or_household="person",
    )

    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d)
        survey.download_data(data_directory=d, extract=True)
        src = d.joinpath("interim", "ACS_18", "MA")
        for p in src.iterdir():
            shutil.move(str(p), str(dst))


cwd = pathlib.Path.cwd()
download_data(cwd)

SEED = 11

INCOME_VARS = [
    "INTP",  # interest income
    "OIP",  # all other income
    "PAP",  # public assistance income
    "RETP",  # retirement income
    "SEMP",  # self-employment income
    "SSIP",  # supplementary social security income
    "SSP",  # social security income
    "WAGP",  # wages or salary income
    "PERNP",  # total person's earnings
    "PINCP",  # total person's income
    # from household files
    # 'FINCP', # family income
    # 'HINCP', # household income
]

OTHER_INCOME_VARS = [
    "FINTP",  # interest income allocation flag
    "FOIP",  # other income allocation flag
    "FPAP",  # public assistance income allocation flag
    "FPINCP",  # total person's income allocation flag
    "FRETP",  # retirement income allocation flag
    "FSEMP",  # self-employment income allocation flag
    "FSSIP",  # supplementary social security income allocation flag
    "FSSP",  # social security income allocation flag
    "FWAGP",  # wages and salary income allocation flag
    # from household files
    # 'GRPIP', # gross rent as a percentage of household income
    # 'OCPIP', # selected monthly owner costs as a percentage of household income
    # 'FFINCP', # family income allocation flag
    # 'FHINCP', # household income allocation flag
]


input = "psam_p25.csv"
X_df = pd.read_csv(input)
y_df = X_df[INCOME_VARS]
X_df = X_df.drop(INCOME_VARS + OTHER_INCOME_VARS, axis=1)

# TODO may need to split households, not people to avoid leakage
X_df_tr, X_df_val, y_df_tr, y_df_val = train_test_split(
    X_df, y_df, random_state=SEED, shuffle=True
)

# save
cwd.joinpath("train").mkdir()
cwd.joinpath("val").mkdir()
X_df_tr.to_csv(cwd / "train" / "entities.csv", index=False)
X_df_val.to_csv(cwd / "val" / "entities.csv", index=False)
y_df_tr.to_csv(cwd / "train" / "targets.csv", index=False)
y_df_val.to_csv(cwd / "val" / "targets.csv", index=False)

print("done")
