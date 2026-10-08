import pandas as pd


def check_numeric(df: pd.DataFrame) -> dict:

    result = {}

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns


    for column in numeric_columns:

        issues = {}

        series = df[column].dropna()


        # отрицательные значения
        negative_values = series[series < 0]

        if not negative_values.empty:
            issues["negative_values"] = (
                negative_values.tolist()
            )


        # IQR
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr


        outliers = series[
            (series < lower_bound) |
            (series > upper_bound)
        ]


        if not outliers.empty:
            issues["outliers"] = (
                outliers.tolist()
            )


        if issues:
            result[column] = issues


    return result