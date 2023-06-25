from fastapi import FastAPI, Depends, Request, Form, status
from fastapi.staticfiles import StaticFiles  # Just to add Favicon

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session



templates = Jinja2Templates(directory="templates")

app = FastAPI()
import pytest
from fastapi.testclient import TestClient



@pytest.fixture
def client():
    """Create a test client using the FastAPI app"""
    with TestClient(app) as client:
        yield client


def test_time_slot_add_table(client):
    """Unit test for the time_slot_add_table function"""
    # Make a POST request to the /table/add endpoint
    response = client.post("/table/add", data={"turma_id": "123", "time_slot": "1"})

    # Assert that the response status code is 303 (SEE OTHER)
    assert response.status_code == 303

    # Assert that the response redirects to the correct URL
    assert response.headers["location"] == "/table"

    # Optionally, you can also assert other aspects of the response, such as the response body or any database changes
