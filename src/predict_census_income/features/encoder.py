from ballet.eng.misc import IdentityTransformer
from ballet.transformer import make_robust_transformer


def get_target_encoder(income_col='PINCP', income_threshold=50_000):
    """Get encoder for the prediction target

    Returns:
        transformer-like
    """

    # From Kaggle:
    # > The prediction task is to determine whether a person makes over $50K a
    # > year.
    # Note: this is not adjusted for inflation since 1994
    return make_robust_transformer([
        lambda y: y[income_col],
        lambda y: (y>income_threshold).astype(int),
    ])
