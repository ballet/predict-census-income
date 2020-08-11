from ballet.eng.misc import IdentityTransformer
from ballet.transformer import make_robust_transformer


# $50,000 in January 1994 adjusted via CPI-U to January 2018 dollars.
INCOME_THRESHOLD = 84_770


def get_target_encoder(income_col='PINCP', income_threshold=INCOME_THRESHOLD):
    """Get encoder for the prediction target

    Returns:
        transformer-like
    """

    # From Kaggle:
    # > The prediction task is to determine whether a person makes over $50K a
    # > year.
    # We adjust to 2018 dollars abovee.
    return make_robust_transformer([
        lambda y: y[income_col],
        lambda y: (y>income_threshold).astype(int),
    ])
