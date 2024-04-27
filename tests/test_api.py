from tests.conftest import test_app  # noqa


def test_health(test_app):  # noqa
    response = test_app.get("/health")
    assert response.status_code == 200


def test_predict(test_app):  # noqa
    payload = {
        "features": [
            {
                "Pclass": 3,
                "Sex": "male",
                "Age": 34.5,
                "SibSp": 0,
                "Parch": 0,
                "Fare": 7.8292,
                "Embarked": "Q",
            }
        ]
    }

    response = test_app.post("/predict", json=payload)

    assert response.status_code == 200
    assert response.json() == {"survived": [0]}
