#!/usr/bin/env python3

import gzip
import pathlib
import shutil
import tempfile

try:
    import boto3
except ImportError:
    boto3 = None
import click
import pandas as pd
from pypums import ACS
from sklearn.model_selection import train_test_split


cwd = pathlib.Path.cwd()

SEED = 11

INCOME_VARS = [
    # from person file
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
    # from household file
    'FINCP',  # family income
    'HINCP',  # household income
]

OTHER_INCOME_VARS = [
    # from person file
    "FINTP",  # interest income allocation flag
    "FOIP",  # other income allocation flag
    "FPAP",  # public assistance income allocation flag
    "FPINCP",  # total person's income allocation flag
    "FRETP",  # retirement income allocation flag
    "FSEMP",  # self-employment income allocation flag
    "FSSIP",  # supplementary social security income allocation flag
    "FSSP",  # social security income allocation flag
    "FWAGP",  # wages and salary income allocation flag
    # from household file
    'GRPIP',  # gross rent as a percentage of household income
    'OCPIP',  # selected monthly owner costs as a % of household income
    'FFINCP',  # family income allocation flag
    'FHINCP',  # household income allocation flag
]


def download_data(dst: pathlib.Path):
    dst.mkdir(exist_ok=True, parents=True)

    person = ACS(
        year=2018,
        state="Massachusetts",
        survey="1-Year",
        person_or_household="person",
    )

    household = ACS(
        year=2018,
        state="Massachusetts",
        survey="1-Year",
        person_or_household="household",
    )

    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d)
        person.download_data(data_directory=d, extract=True)
        household.download_data(data_directory=d, extract=True)
        src = d.joinpath("interim", "ACS_18", "MA")
        for p in src.iterdir():
            if not dst.joinpath(p.name).exists():
                shutil.move(str(p), str(dst))
            else:
                print(f'skipping {p.name} (already exists in dst)')


def merge(person: pd.DataFrame, household: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(
        left=person,
        right=household,
        how='left',
        on='SERIALNO'
    )


def prepare(df, save=True):
    # From Kaggle:
    # > A set of reasonably clean records was extracted using the following
    # > conditions: ((AAGE>16) && (AGI>100) && (AFNLWGT>1) && (HRSWK>0)).
    # In PUMS, variables are named AGEP for age, PINCP for personal income from
    # all source, and WKHP for hours worked in a typical week over the past 12
    # months. The weight variable (AFNLWGT) is not relevant to this micro data.
    mask = (df['AGEP'] > 16) & (df['PINCP'] > 100) & (df['WKHP'] > 0)
    print(f'Filtering {mask.sum()} relevant rows out of {len(df)} total')
    df = df.loc[mask]

    y_df = df[INCOME_VARS]
    X_df = df.drop(INCOME_VARS + OTHER_INCOME_VARS, axis=1)

    # TODO may need to split households, not people to avoid leakage
    X_df_tr, X_df_val, y_df_tr, y_df_val = train_test_split(
        X_df, y_df, random_state=SEED, shuffle=True
    )

    if save:
        cwd.joinpath("train").mkdir(exist_ok=True)
        cwd.joinpath("val").mkdir(exist_ok=True)
        X_df_tr.to_csv(cwd / "train" / "entities.csv", index=False)
        X_df_val.to_csv(cwd / "val" / "entities.csv", index=False)
        y_df_tr.to_csv(cwd / "train" / "targets.csv", index=False)
        y_df_val.to_csv(cwd / "val" / "targets.csv", index=False)

    return X_df_tr, X_df_val, y_df_tr, y_df_val


def compress(src):
    for split in ['train', 'val']:
        for table in ['entities', 'targets']:
            filename = src / split / f'{table}.csv'
            with filename.open('rb') as fin:
                with gzip.open(filename.with_suffix('.csv.gz'), 'wb') as fout:
                    shutil.copyfileobj(fin, fout)


def upload(src):
    if boto3 is None:
        raise NotImplementedError

    s3 = boto3.client('s3')
    bucket = 'mit-dai-ballet'

    # TODO - upload docs
    pass

    # upload files
    for split in ['train', 'val']:
        for table in ['entities', 'targets']:
            for suffix in ['.csv', '.csv.gz']:
                filename = src / split / (table + suffix)
                objectname = f'census/{split}/{table}{suffix}'
                s3.upload_file(str(filename), bucket, objectname)


@click.command()
@click.option('-u', '--upload', '_upload',
              is_flag=True, default=False, help='upload files to s3')
def main(_upload):
    download_data(cwd)
    person_file = "psam_p25.csv"
    person = pd.read_csv(person_file)
    household_file = "psam_h25.csv"
    household = pd.read_csv(household_file)
    df = merge(person, household)
    prepare(df)
    compress(cwd)
    if _upload:
        upload(cwd)
    print("done")


if __name__ == '__main__':
    main()
