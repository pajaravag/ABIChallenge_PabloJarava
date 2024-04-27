import pickle
from functools import lru_cache

import pandas as pd
from sklearn.pipeline import Pipeline

from src.constants import COLUMNS, PIPELINE_PATH


@lru_cache
def load_pipeline() -> Pipeline:
    """This function reads the pickled pipeline from the model directory
    Returns:
        Pipeline: trained pipeline
    """
    return pickle.load(open(PIPELINE_PATH, "rb"))


def transform(data: dict) -> pd.DataFrame:
    """This function takes in the request payload, transforms it into a dataframe,
    Parameters:
        data (dict): request payload
    Returns:
        pd.DataFrame: transformed data
    """

    pipeline = load_pipeline()
    data = pd.DataFrame(data["features"])
    data = check_schema(data)
    data = pipeline.transform(data)
    return data


def check_schema(data: pd.DataFrame) -> pd.DataFrame:
    """This function checks the schema of the data and returns the required columns
    Parameters:
        data (pd.DataFrame): input data
    Returns:
        pd.DataFrame: data with required columns
    """

    data = data[COLUMNS]
    return data
