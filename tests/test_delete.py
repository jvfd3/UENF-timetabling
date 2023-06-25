import pytest
from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from timetabling import app, get_db
from timetabling.models import TimeSlot
from timetabling.database import engine, Base

# Cria as tabelas no banco de dados de teste
Base.metadata.create_all(bind=engine)

# Define um cliente de teste
client = TestClient(app)


@pytest.fixture(scope="module")
def test_db():
    # Cria uma sessão de banco de dados de teste
    db = Session(bind=engine)
    try:
        # Executa as migrações iniciais
        Base.metadata.create_all(bind=engine)
        yield db
    finally:
        # Limpa o banco de dados e fecha a sessão
        Base.metadata.drop_all(bind=engine)
        db.close()


def test_time_slot_delete(test_db):
    # Insere um registro de exemplo no banco de dados
    time_slot = TimeSlot(turma_id="123", slot=1)
    test_db.add(time_slot)
    test_db.commit()

    # Faz uma requisição DELETE para a rota de exclusão
    response = client.get(f"/delete/{time_slot.id}")

    # Verifica se o código de status da resposta é 302 (redirecionamento)
    assert response.status_code == status.HTTP_302_FOUND

    # Verifica se o registro foi removido do banco de dados
    deleted_time_slot = test_db.query(TimeSlot).get(time_slot.id)
    assert deleted_time_slot is None
