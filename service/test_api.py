import pytest
from run import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Geräteausleihe Microservice is running" in response.data

def test_pdf_generation_basic(client):
    response = client.get("/pdf?borrower=Test&device=MacBook")
    assert response.status_code == 200
    assert response.mimetype == "application/pdf"
    assert "attachment" in response.headers.get("Content-Disposition", "")

def test_pdf_generation_full_parameters(client):
    response = client.get("/pdf?borrower=Max%20Mustermann&device=HP%20Elitebook%20860%20G6&staff=IT-Support%20TBZ")
    assert response.status_code == 200
    assert response.mimetype == "application/pdf"
    assert "TBZ_Quitt" in response.headers.get("Content-Disposition", "")

def test_pdf_generation_empty_parameters(client):
    response = client.get("/pdf?borrower=&device=&staff=")
    assert response.status_code == 200
    assert response.mimetype == "application/pdf"

def test_pdf_generation_special_characters(client):
    response = client.get("/pdf?borrower=Test/User<>Name&device=Device|Name")
    assert response.status_code == 200
    assert response.mimetype == "application/pdf"

def test_pdf_generation_unicode(client):
    response = client.get("/pdf?borrower=Müller%20François&device=Zürich%20Laptop")
    assert response.status_code == 200
    assert response.mimetype == "application/pdf"
