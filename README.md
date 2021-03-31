[![ballet](https://img.shields.io/static/v1?label=built%20with&message=ballet&color=FCDD35)](https://ballet.github.io)
[![project chat](https://badges.gitter.im/ballet-project/predict-census-income.svg)](https://gitter.im/ballet-project/predict-census-income?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
<a href="https://mybinder.org/v2/gh/HDI-Project/ballet-predict-census-income/master?urlpath=lab" target="_blank" rel="nofollow"><img src="https://ballet.github.io/ballet/_static/launch-assemble.svg" style="max-width:100%;"></a>

# Predict Census Income

This is a collaborative predictive modeling project built on the [ballet framework](https://ballet.github.io).

This project contains a feature engineering pipeline and associated models that can be used to **predict personal income from raw survey responses** to the US Census American Community Survey. The model built from features submitted by the community can then be used to optimize administration of the survey, direct public policy interventions, and assist empirical researchers.

[**See dates/times for upcoming virtual collaboration hours**](#virtual-collaboration-hours), opportunities to work at the same time as other collaborators and ask/answer questions in the chat.

## Join the collaboration

Are you interested in joining the collaboration?

### Your task

**Your task is to create and submit one feature to the project.**

1. The easiest way to get started and hack on this repository is to launch Assemblé, a interactive development environment built on top of Jupyter Lab and hosted in the cloud. You can read more about this development workflow [here](https://hdi-project.github.io/ballet/contributor_guide.html#cloud-feature-development-workflow).

    <a href="https://mybinder.org/v2/gh/HDI-Project/ballet-predict-census-income/master?urlpath=lab" target="_blank" rel="nofollow"><img src="https://hdi-project.github.io/ballet/_static/launch-assemble.svg" style="max-width:100%;"></a>

2. Alternately, you can use your preferred tools and development environment to create and submit a feature from your own machine. You can read about the local development workflow [here](https://hdi-project.github.io/ballet/contributor_guide.html#local-feature-development-workflow).

### Getting started

First, get acquainted with the Ballet framework if you are not yet familiar.

- Look over the [Ballet Contributor Guide](https://hdi-project.github.io/ballet/contributor_guide.html)
- Look over the [Ballet Feature Engineering Guide](https://hdi-project.github.io/ballet/feature_engineering_guide.html)
- Check out the features that are currently part of this project, in the contributed features directory ([`src/predict_census_income/features/contrib`](src/predict_census_income/features/contrib)).
- Check out the [Analysis.ipynb](notebooks/Analysis.ipynb) notebook for some starter code

### Virtual collaboration hours

We are hosting several Virtual Collaboration Hours (VCH) in which we will work together on feature engineering and help each other with ideas and implementation. The VCH will start with a short video presentation aimed at beginners introducing Ballet and this predict-census-income project, with an opportunity for Q&A. Then, we will split off to work and will be chatting in the [Gitter chat](https://gitter.im/ballet-project/predict-census-income).

Schedule (check back here to confirm!)

- [Wed, Sep 9 5pm-6pm ET](./docs/vch-event-0.ics)
- [Sun, Sep 13, 1pm-2pm ET](./docs/vch-event-1.ics)
- [Wed, Sep 16, 8am-9am ET](./docs/vch-event-2.ics)
- [Mon, Sep 21, 5pm-6pm ET](./docs/vch-event-3.ics)
- [Sat, Oct 3, 11am-12pm ET](./docs/vch-event-4.ics)

You can also see [a recording of a recent VCH](https://www.youtube.com/watch?v=heeRkRtnN1s).

## Dataset

### Input data

The input data is the raw survey responses to the 2018 US Census American Community Survey (ACS). This is known as the "Public Use Microdata Sample" because otherwise most numbers from the ACS are reported in aggregate.

* The data documentation can be viewed [here](https://mit-dai-ballet.s3.amazonaws.com/census/ACS2018_PUMS_README.pdf)
* The data dictionary can be viewed [here](https://mit-dai-ballet.s3.amazonaws.com/census/PUMS_Data_Dictionary_2018.pdf) in PDF form, or [here](https://mit-dai-ballet.s3.amazonaws.com/census/PUMS_Data_Dictionary_2018.csv) in CSV form.
* Many additional resources about the ACS can be viewed [here](https://acsdatacommunity.prb.org/acs-data-products--resources/).
* The dataset is created by merging the "household" and "person" parts of the survey. Thus one row of the dataset contains the responses for one person to both the household and person surveys. A person is identified by a unique `SERIALNO`. A set of "reasonable" rows is filtered as follows: (1) individuals older than 16 (2) personal income greater than $100 (3) hours worked in a typical week greater than 0.

The full script that minimally prepares the data is [here](.bin/split/main.py).

The resulting training dataset has 30085 rows (people) and 494 columns (raw).

### Prediction target

The prediction target is whether an individual respondent will earn more than $84,770 in 2018. Though a bit contrived, this comes from adapting the classic ML ["census"](https://archive.ics.uci.edu/ml/datasets/Census+Income) dataset to the modern era. The original prediction target is to

> determine whether a person makes over 50K a year.

Thus we adjust for inflation from 1994 to 2018.

## Getting help

* Read over Ballet's [Frequently Asked Questions](https://hdi-project.github.io/ballet/faq.html) page
* Join the project chat:
    [![project chat](https://badges.gitter.im/ballet-project/predict-census-income.svg)](https://gitter.im/ballet-project/predict-census-income?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

## Usage

To use the feature engineering pipeline:

```python
from predict_census_income.api import api
X_df, y_df = api.load_data()
pipeline = api.pipeline
features = pipeline.fit_transform(X_df, y_df)
```


To use a sample model:

```python
from predict_census_income.models import train, predict
from predict_census_income.models.logistic_regression import create_logistic_regression_model
X_df, y_df = api.load_data()
model, encoder = train(X_df, y_df, create_logistic_regression_model)  # loads the pipeline/encoder automatically
predict(model, X_df)  # make predictions on training data
```
