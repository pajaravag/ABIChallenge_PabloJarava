import pickle
from functools import lru_cache
from typing import List, Literal

import pandas as pd
from xgboost import XGBClassifier

from src.constants import MODEL_PATH
from src.pipeline.data import transform


@lru_cache
def read_model() -> XGBClassifier:
    """This function reads the pickled model from the model directory
    Returns:
        XGBClassifier: trained model
    """
    model = pickle.load(open(MODEL_PATH, "rb"))
    return model


def predict(data: pd.DataFrame) -> List[Literal[0, 1]]:
    """This function takes in the Dataframe, and returns the model's prediction
    Parameters:
        data (pd.Dataframe): Dataframe to be predicted
    Returns:
        List[Literal[0, 1]]: model's prediction
    """
    model = read_model()
    df = transform(data)
    return model.predict(df).tolist()
