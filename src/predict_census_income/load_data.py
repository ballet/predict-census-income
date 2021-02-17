import pandas as pd
from ballet.project import load_config
from ballet.util.io import load_table_from_config
from funcy import some, where


def load_data(input_dir=None):
    """Load data"""
    if input_dir is not None:
        config = load_config()
        tables = config.get('data.tables')

        entities_table_name = config.get('data.entities_table_name')
        entities_config = some(where(tables, name=entities_table_name))
        X = load_table_from_config(input_dir, entities_config)

        targets_table_name = config.get('data.targets_table_name')
        targets_config = some(where(tables, name=targets_table_name))
        y = load_table_from_config(input_dir, targets_config)
    else:
        root = 'https://mit-dai-ballet.s3.amazonaws.com/census'
        X = pd.read_csv(root + '/train/entities.csv.gz')
        y = pd.read_csv(root + '/train/targets.csv.gz')

    return X, y
