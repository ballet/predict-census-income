import click
from sklearn.metrics import classification_report

from predict_census_income.api import api
from predict_census_income.models import train, predict
from predict_census_income.models.logistic_regression import (
    create_logistic_regression_model)

models = {
    'logistic_regression': create_logistic_regression_model,
}


@click.command()
@click.argument('train_dir',
                type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.argument('test_dir',
                type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option('--model',
              type=click.Choice(list(models.keys()), case_sensitive=False),
              default='logistic_regression')
@click.option('--row', type=int, default=None, help='integer index of rows')
def main(train_dir, test_dir, model, row):
    create_model = models[model]
    X_df, y_df = api.load_data(train_dir)
    model, encoder = train(X_df, y_df, create_model)

    X_df_test, y_df_test = api.load_data(test_dir)
    y_test = encoder.transform(y_df_test)

    if row is not None:
        x = X_df_test.iloc[row:row+1]
        y_true = y_test.iloc[row:row+1].item()
        y_pred = predict(model, x).item()
        print(f'Row {row}: Predicted {y_pred}, actual {y_true}')
    else:
        x = X_df_test
        y_true = y_test
        y_pred = predict(model, x)
        report = classification_report(
            y_true, y_pred, target_names=['Low income', 'High income'])
        print(report)


if __name__ == '__main__':
    main()
