import pytest
from run import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    body = response.get_data(as_text=True)
    assert "Geräteausleihe Microservice is running" in body


def test_healthz(client):
    response = client.get("/healthz")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_pdf_generation_basic(client):
    response = client.get("/pdf?borrower=Test&device=MacBook")
    assert response.status_code == 200
    assert response.mimetype == "application/pdf"
    assert "attachment" in response.headers.get("Content-Disposition", "")


def test_pdf_generation_full_parameters(client):
    response = client.get("/pdf?borrower=Max%20Mustermann&device=HP%20Elitebook%20860%20G6&staff=IT%20Support%20TBZ")
    assert response.status_code == 200
    assert response.mimetype == "application/pdf"
    assert "TBZ_Quittung" in response.headers.get("Content-Disposition", "")


def test_pdf_generation_empty_parameters(client):
    response = client.get("/pdf?borrower=&device=&staff=")
    assert response.status_code == 200
    assert response.mimetype == "application/pdf"
