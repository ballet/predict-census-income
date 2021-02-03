from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


def create_logistic_regression_model(pipeline):
    return Pipeline([
        ('feature_engineering_pipeline', pipeline),
        ('scaler', StandardScaler()),
        ('lr', LogisticRegression()),
    ])
