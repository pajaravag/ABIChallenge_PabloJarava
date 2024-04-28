from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class PredictionSummary(models.Model):
    prediction = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.prediction


SummarySchema = pydantic_model_creator(PredictionSummary)
