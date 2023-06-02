# conftest.py

import pytest
from timetabling import app, database
import tempfile
import os

@pytest.fixture(scope="module")
def client():
    # create a test client for the Flask app
    # app.config["TESTING"] = True
    client = app.test_client()
    yield client # return the client object to the test functions

@pytest.fixture(scope="module")
def db_session():
    # create a temporary file for the test database
    db_file = tempfile.NamedTemporaryFile(delete=False)
    db_url = f"sqlite:///{db_file.name}"
    # create the engine and the tables
    engine = database.create_engine(db_url, connect_args={"check_same_thread": False})
    database.Base.metadata.create_all(engine)
    # create the session object
    session = database.SessionLocal()
    yield session # return the session object to the test functions
    # close the session and delete the temporary file
    session.close()
    os.unlink(db_file.name)
