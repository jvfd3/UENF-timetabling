from timetabling import app # import the app object from the module
from fastapi.testclient import TestClient
import pytest
from timetabling.database import SessionLocal

# from database import SessionLocal

@pytest.fixture(scope="module")
def db():
    db = SessionLocal()
    yield db
    db.close()

client = TestClient(app.app) # create a client object by passing the app object

models = app.models

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

def test_read_table_index():
    response = client.get("/table")
    assert response.status_code == 200

def test_time_slot_add():
    response = client.post("/add", data={"turma_id": "TEST_A", "time_slot": "111"})
    assert response.status_code in (303, 200) 
    # assert response.headers["location"] == "/"

def test_added_time_slot(db):
    tt_TEST_A = db.query(models.TimeSlot).filter(models.TimeSlot.turma_id == "TEST_A").first()
    assert tt_TEST_A is not None

def test_time_slot_delete(db):
    tt_TEST_A = db.query(models.TimeSlot).filter(models.TimeSlot.turma_id == "TEST_A").first()
    assert tt_TEST_A is not None
 
    time_slot_id = tt_TEST_A.id
    response = client.get(f"/delete/{time_slot_id}")
    assert response.status_code in (200,302)
    assert db.query(models.TimeSlot).filter(models.TimeSlot.id == time_slot_id).first() is None

def test_map_timeslots_to_classes():
    time_slots = [
        models.TimeSlot(turma_id="A", slot=0),
        models.TimeSlot(turma_id="B", slot=1),
        models.TimeSlot(turma_id="C", slot=5),
        models.TimeSlot(turma_id="D", slot=6),
        models.TimeSlot(turma_id="E", slot=10),
        models.TimeSlot(turma_id="F", slot=11),
        models.TimeSlot(turma_id="G", slot=15),
        models.TimeSlot(turma_id="H", slot=16),
    ]
    expected_classes = {
        "08:00-10:00": {
            "mon": [time_slots[0]],
            "tue": [time_slots[1]],
            "wed": [],
            "thu": [],
            "fri": []
        },
        "10:00-12:00": {
            "mon": [time_slots[2]],
            "tue": [time_slots[3]],
            "wed": [],
            "thu": [],
            "fri": []
        },
        "14:00-16:00": {
            "mon": [time_slots[4]],
            "tue": [time_slots[5]],
            "wed": [],
            "thu": [],
            "fri": []
        },
        "16:00-18:00": {
            "mon": [time_slots[6]],
            "tue": [time_slots[7]],
            "wed": [],
            "thu": [],
            "fri": []
        }
    }
    actual_classes = app.map_timeslots_to_classes(time_slots)
    assert actual_classes == expected_classes

def test_professor_model(db):
    # create a new professor
    new_professor = models.Professor(nome="Alice")
    db.add(new_professor)
    db.commit()
    # query the professor by id
    professor = db.query(models.Professor).filter(models.Professor.id == new_professor.id).first()
    assert professor is not None
    assert professor.nome == "Alice"
    # update the professor name
    professor.nome = "Bob"
    db.commit()
    updated_professor = db.query(models.Professor).filter(models.Professor.id == new_professor.id).first()
    assert updated_professor.nome == "Bob"
    # delete the professor
    db.delete(professor)
    db.commit()
    deleted_professor = db.query(models.Professor).filter(models.Professor.id == new_professor.id).first()
    assert deleted_professor is None

def test_turma_model(db):
    # create a new disciplina and a new professor
    new_disciplina = models.Disciplina(nome="Math", code="MAT101")
    new_professor = models.Professor(nome="Alice")
    db.add(new_disciplina)
    db.add(new_professor)
    db.commit()
    # create a new turma with the disciplina and professor ids
    new_turma = models.Turma(disciplina_id=new_disciplina.id, professor_id=new_professor.id)
    db.add(new_turma)
    db.commit()
    # query the turma by id
    turma = db.query(models.Turma).filter(models.Turma.id == new_turma.id).first()
    assert turma is not None
    assert turma.disciplina_id == new_disciplina.id
    assert turma.professor_id == new_professor.id
    # query the disciplina and professor by using the backref attributes of the turma
    disciplina = turma.disciplina
    professor = turma.professor
    assert disciplina is not None
    assert disciplina.nome == "Math"
    assert disciplina.code == "MAT101"
    assert professor is not None
    assert professor.nome == "Alice"
