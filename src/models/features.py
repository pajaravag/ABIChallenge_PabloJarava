from typing import List, Literal

from pydantic import BaseModel


class Pclass(BaseModel):
    Pclass: float


class Sex(BaseModel):
    Sex: Literal["male", "female"]


class Age(BaseModel):
    Age: float


class SibSp(BaseModel):
    SibSp: float


class Parch(BaseModel):
    Parch: float


class Fare(BaseModel):
    Fare: float


class Embarked(BaseModel):
    Embarked: Literal["S", "C", "Q"]


class Features(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    pass


class PayloadFeatures(BaseModel):
    features: List[Features]


class SurvivedResponse(BaseModel):
    survived: List[Literal[0, 1]]
