from ballet import Feature
from ballet.eng import BaseTransformer

input = [
    "RMSP",
    "AGEP",
    "CIT",
    "COW",
    "DEYE",
    "DEAR",
    "DDRS",
    "DREM",
    "DPHY",
    "DOUT",
    "HINS7",
    "HINS6",
    "HINS5",
    "HINS4",
    "HINS3",
    "HINS2",
    "HINS1",
    "MAR",
    "MIG",
    "SCHL",
    "SEX",
    "LANX",
]  # TODO - str or list of str


class fill_with_TreeReg(BaseTransformer):
    def fit(self, X, y=None):
        self.col_target = X.columns[0:1]
        self.cols_ok = X.columns[1:]
        self.rows_ok = (~X[self.col_target].isna()).values
        X_fit = X[self.cols_ok].iloc[self.rows_ok]
        Y_fit = X[self.col_target].iloc[self.rows_ok]
        from sklearn.tree import DecisionTreeRegressor

        self.clf_ = DecisionTreeRegressor(max_depth=40)
        self.clf_.fit(X_fit, Y_fit)
        return self

    def transform(self, X, y=None):
        return self.clf_.predict(X[self.cols_ok]).astype(int)


transformer = fill_with_TreeReg()
name = "FilledRMSP"
description = "the new RMSP is predicted using a regression tree with max_depth = 40"
feature = Feature(input, transformer, name=name, description=description)
