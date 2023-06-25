import pytest
from fastapi.testclient import TestClient

#from main import app
from timetabling import app, database

client = TestClient(app)

def test_time_slot_edit():
    # Prepare test data
    time_slot_id = 1
    turma_id = "123"
    time_slot = "10"

    # Perform the PUT request
    response = client.put(
        f"/edit/{time_slot_id}",
        data={"turma_id": turma_id, "time_slot": time_slot},
    )

    # Verify the response
    assert response.status_code == 303  # HTTP 303 See Other
    assert response.headers["location"] == "/"

    # You can perform additional assertions based on your specific requirements
    # For example, check if the time slot was updated in the database
