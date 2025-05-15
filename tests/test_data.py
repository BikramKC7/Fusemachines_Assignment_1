# aifellowship12factor/tests/test_main.py

from fastapi.testclient import TestClient
from api.currency_converter.main import app
from pytest import approx



client = TestClient(app)

def test_convert_usd_to_eur():
    with TestClient(app) as client:
        response = client.post("/convert", json={
            "amount": 100,
            "from_currency": "USD",
            "to_currency": "EUR"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["converted_amount"] == approx(90.0, rel=0.05)  # 5% relative tolerance

def test_invalid_currency_code():
    response = client.post("/convert", json={
        "amount": 100,
        "from_currency": "ABC",
        "to_currency": "XYZ"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid currency code or request"
