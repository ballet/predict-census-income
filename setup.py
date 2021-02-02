from setuptools import setup, find_packages

requirements = [
    'ballet==0.8.0',
]

setup(
    name='predict_census_income',
    version='0.1.0-dev',
    packages=find_packages(where='src', include=('predict_census_income', 'predict_census_income.*')),
    package_dir={'': 'src'},
    install_requires=requirements,

    # metadata
    author='Micah Smith',
    author_email='micahs@mit.edu',
    description='A data science project built on the Ballet framework',
    url='https://github.com/HDI-Project/ballet-predict-census-income',
)
