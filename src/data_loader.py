import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """
    Тут мы загрузили Csv-файл и вернули pandas DataFrame
    """
    df = pd.read_csv(path)

    return df