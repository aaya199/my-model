from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)


def test_health_returns_healthy():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_predict_returns_200():
    customer = {
        "tenure_months": 35,
        "monthly_charges": 121.08,
        "contract": "month-to-month",
        "internet_service": "fiber",
        "support_calls": 1,
    }

    response = client.post("/predict", json=customer)

    assert response.status_code == 200


def test_predict_returns_probability():
    customer = {
        "tenure_months": 35,
        "monthly_charges": 121.08,
        "contract": "month-to-month",
        "internet_service": "fiber",
        "support_calls": 1,
    }

    response = client.post("/predict", json=customer)

    assert response.status_code == 200

    data = response.json()

    assert "churn_probability" in data
    assert isinstance(data["churn_probability"], (int, float))


def test_probability_is_between_zero_and_one():
    customer = {
        "tenure_months": 35,
        "monthly_charges": 121.08,
        "contract": "month-to-month",
        "internet_service": "fiber",
        "support_calls": 1,
    }

    response = client.post("/predict", json=customer)

    assert response.status_code == 200

    probability = response.json()["churn_probability"]

    assert 0 <= probability <= 1


def test_predict_rejects_missing_fields():
    customer = {
        "tenure_months": 35,
        "monthly_charges": 121.08,
    }

    response = client.post("/predict", json=customer)

    assert response.status_code == 422


def test_predict_rejects_negative_tenure():
    customer = {
        "tenure_months": -5,
        "monthly_charges": 121.08,
        "contract": "month-to-month",
        "internet_service": "fiber",
        "support_calls": 1,
    }

    response = client.post("/predict", json=customer)

    assert response.status_code == 422