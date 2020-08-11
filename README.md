[![ballet](https://img.shields.io/static/v1?label=built%20with&message=ballet&color=FCDD35)](https://github.com/HDI-Project/ballet)
[![project chat](https://img.shields.io/badge/zulip-join_chat-brightgreen.svg)](https://ballet.zulipchat.com/join/donkqb7awjxmzypdbv62abgh/)
<a href="https://mybinder.org/v2/gh/HDI-Project/ballet-predict-census-income/master?urlpath=lab" target="_blank" rel="nofollow"><img src="https://mybinder.org/badge_logo.svg" style="max-width:100%;"></a>

# Predict Census Income

This is a collaborative predictive modeling project built on the [ballet framework](https://github.com/HDI-Project/ballet).

This project contains a feature engineering pipeline and associated models that can be used to **predict personal income from raw survey responses** to the US Census American Community Survey. The model built from features submitted by the community can then be used to optimize administration of the survey, direct public policy interventions, and assist empirical researchers.

## Join the collaboration

Are you interested in joining the collaboration?

### Getting started

First, get acquainted with the Ballet framework if you are not yet familiar.

1. Look over the [Ballet Contributor Guide](https://hdi-project.github.io/ballet/contributor_guide.html)
2. Look over the [Ballet Feature Engineering Guide](https://hdi-project.github.io/ballet/feature_engineering_guide.html)

Once you have done so, you can check out the features that are currently part of this project, in the contributed features directory ([`src/predict_census_income/features/contrib`](src/predict_census_income/features/contrib)).

### Your task

**Your task is to create and submit one feature to the project.**

1. The easiest way to get started is to launch an interactive Jupyter Lab session to hack on this repository. You can read more about this development workflow [here](https://hdi-project.github.io/ballet/contributor_guide.html#cloud-feature-development-workflow).

    <a href="https://mybinder.org/v2/gh/HDI-Project/ballet-predict-census-income/master?urlpath=lab" target="_blank" rel="nofollow" ><img src="https://mybinder.org/badge_logo.svg" style="max-width:100%;"></a>

2. Alternately, you can use your preferred tools and development environment to create and submit a feature from your own machine. You can read about the local development workflow [here](https://hdi-project.github.io/ballet/contributor_guide.html#local-feature-development-workflow).


## Dataset

### Input data

The input data is the raw survey responses to the 2018 US Census American Community Survey (ACS). This is known as the "Public Use Microdata Sample" because otherwise most numbers from the ACS are reported in aggregate.

* The data documentation can be viewed [here](https://mit-dai-ballet.s3.amazonaws.com/census/ACS2018_PUMS_README.pdf)
* The data dictionary can be viewed [here](https://mit-dai-ballet.s3.amazonaws.com/census/PUMS_Data_Dictionary_2018.pdf) in PDF form, or [here](https://mit-dai-ballet.s3.amazonaws.com/census/PUMS_Data_Dictionary_2018.csv) in CSV form.
* The dataset is created by merging the "household" and "person" parts of the survey. Thus one row of the dataset contains the responses for one person to both the household and person surveys. A person is identified by a unique `SERIALNO`. A set of "reasonable" rows is filtered as follows: (1) individuals older than 16 (2) personal income greater than $100 (3) hours worked in a typical week greater than 0.

The full script that minimally prepares the data is [here](.bin/split/main.py).

The resulting training dataset has 30085 rows (people) and 494 columns (raw).

### Prediction target

The prediction target is whether an individual respondent will earn more than $84,770 in 2018. Though a bit contrived, this comes from adapting the classic ML ["census"](https://archive.ics.uci.edu/ml/datasets/Census+Income) dataset to the modern era. The original prediction target is to

> determine whether a person makes over 50K a year.

Thus we adjust for inflation from 1994 to 2018.