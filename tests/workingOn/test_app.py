import pytest
from timetabling import models

def test_index(client):
    # test the index route of the app
    response = client.get("/")
    assert response.status_code == 200 # check that the response is OK
    assert b"Timetabling App" in response.data # check that the response contains some text

def test_add_turma(client, db_session):
    # test the add_turma route of the app
    data = {
        "disciplina_id": 1,
        "professor_id": 1,
        "slot": 1
    }
    response = client.post("/add_turma", data=data)
    assert response.status_code == 302 # check that the response is a redirect
    assert response.location == "http://localhost/" # check that the redirect location is correct
    # check that the turma was added to the database
    turma = db_session.query(models.Turma).filter_by(disciplina_id=1, professor_id=1).first()
    assert turma is not None
