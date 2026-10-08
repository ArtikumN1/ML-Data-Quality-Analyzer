import pandas as pd


def check_numeric(df: pd.DataFrame) -> dict:
    """
    Проверяем числовые признаки:
        отрицательные значения
        выбросы через IQR
    """
    result = {}

    numeric_columns = df.select_dtypes(
        include = ["int64", "float64"]
    ).columns

    for column in numeric_columns:

        issues = {}

        series = df[column].dropna()


        negative_values = series[series < 0]

        if len(negative_values) > 0:
            issues["negative_values"] = (
                negative_values.tolist()
            )

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)

        iqr = q3 -q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 - 1.5 * iqr
        #print(column)
        #print("Q1:", q1)
        #print("Q3:", q3)
        #print("IQR:", iqr)
        #print("bounds:", lower_bound, upper_bound)

        outliers = series[
            (series < lower_bound) | 
            (series > upper_bound)
        ]


        if issues:
            result[column] = issues


    return result