from typing import List, Literal

from pydantic import BaseModel


class Pclass_(BaseModel):
    Pclass: float


class Sex_(BaseModel):
    Sex: Literal["male", "female"]


class Age_(BaseModel):
    Age: float


class SibSp_(BaseModel):
    SibSp: float


class Parch_(BaseModel):
    Parch: float


class Fare_(BaseModel):
    Fare: float


class Embarked_(BaseModel):
    Embarked: Literal["S", "C", "Q"]


class Features(Pclass_, Sex_, Age_, SibSp_, Parch_, Fare_, Embarked_):
    pass


class PayloadFeatures(BaseModel):
    features: List[Features]


class SurvivedResponse(BaseModel):
    survived: List[Literal[0, 1]]
