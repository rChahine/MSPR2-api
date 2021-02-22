import pytest
from api import app
from api.database import Base, engine
from api.models import User
from fastapi.testclient import TestClient
from sqlalchemy import insert

Base.metadata.drop_all(bind=engine)  # Clear database
Base.metadata.create_all(bind=engine)  # Regenerate database

stmt = (
    insert(User).
    values(
        identifiant='user',
        password="$2b$12$Gr3bUaIsvDYgKnTzC4xIHuA2KgmTX6jb/IAArzfq/JeIhz8ha41Ci"
    )
)

engine.connect().execute(stmt)

client = TestClient(app)


@pytest.fixture
def signin_body():
    """ returns values to signin route """

    return dict(
        login="user",
        password="test"
    )


@pytest.fixture
def signin(signin_body):
    """ signin an admin """

    r = client.post("/authentication", json=signin_body)
    return r.json()


@pytest.fixture
def client_auth_user(signin):
    """ add token in header for protected route """
    client.headers.update({"Authorization": signin["token"]})
    return client
