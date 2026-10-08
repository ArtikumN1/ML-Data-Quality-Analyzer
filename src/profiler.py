import pandas as pd


class DatasetProfiler:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def get_basic_info(self):
        return {
            "rows": self.df.shape[0],
            "columns": self.df.shape[1],
            "column_names": list(self.df.columns)
        }

    def get_dtypes(self):
        return self.df.dtypes.to_dict()

    def detect_feature_types(self):
        feature_types = {}

        for column in self.df.columns:
            dtype = self.df[column].dtype

            if dtype in ["int", "float64"]:
                feature_types[column] = "numeric"

            elif dtype == "object":

                unique_ratio = (
                    self.df[column].nunique() / len(self.df)
                )

                if unique_ratio > 0.5:
                    feature_types[column] = "text"
                else:
                    feature_types[column] = "categorical"
        return feature_types