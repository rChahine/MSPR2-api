import pytest
from fastapi.testclient import TestClient
from sqlalchemy import insert

from api import app
from api.authentication.models import User
from api.database import Base, engine

Base.metadata.drop_all(bind=engine)  # Clear database
Base.metadata.create_all(bind=engine)  # Regenerate database

stmt = insert(User).values(
    identifiant="administrateur",
    password="$2a$04$PuoNFmToF5Xoa6H.Z00.kOuzd2.OYvT/kimCy5f28A5PuDtcjh3nu",
)

engine.connect().execute(stmt)

client = TestClient(app)


@pytest.fixture
def signin_body():
    """ returns values to signin route """

    return dict(identifiant="administrateur", password="1Adm!n!strateur")


@pytest.fixture
def signin(signin_body):
    """ signin an admin """

    r = client.post("/authentication", json=signin_body)
    return r.json()


@pytest.fixture
def client_auth(signin):
    """ add token in header for protected route """
    client.headers.update({"Authorization": signin["token"]})
    return client
