import pandas as pd


def check_missing(df: pd.DataFrame) -> dict:
    """
    Проверяем пропущенные значения в DataFrame
    Возвращает информацию о колонках с пропусками
    """
    missing_count = df.isna().sum()

    missing_percentage = (missing_count / len(df) * 100)

    result = {}

    for column in df.columns:
        if missing_count[column] > 0:
            result[column] = {
                "count": int(missing_count[column]),
                "percentage": round(
                    missing_percentage[column],
                    2
                )
            }
    return result