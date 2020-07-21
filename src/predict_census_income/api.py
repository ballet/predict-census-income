from ballet.project import FeatureEngineeringProject

import predict_census_income as package
from predict_census_income.features.encoder import get_target_encoder
from predict_census_income.load_data import load_data


api = FeatureEngineeringProject(
    package=package,
    encoder=get_target_encoder(),
    load_data=load_data,
)
