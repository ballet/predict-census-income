from predict_census_income.api import api


def train(X_df, y_df, create_model):
    """Create and train model on given training data

    create_model should be a callable that takes the feature engineering
    pipeline and produces a sklearn estimator (probably a Pipeline).
    """
    pipeline = api.pipeline
    encoder = api.encoder
    y = encoder.fit_transform(y_df)

    model = create_model(pipeline)
    model.fit(X_df, y)
    return model, encoder


def predict(model, x):
    return model.predict(x)
