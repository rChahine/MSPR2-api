from os import read
import magic
from api.database import engine


def test_upload(client_auth):

    mime = magic.Magic(mime=True)
    with open("tests/test.csv", "rb") as f:
        _file = {"file": ("test", f, mime.from_file("tests/test.csv"))}
        send_file = client_auth.post("/upload", files=_file)
        assert send_file.status_code == 200
        assert send_file.json() == {"detail": "File imported"}

    with engine.connect() as c:

        result = c.execute("select * from file_upload")

        for r in result:
            assert r['id'] == 1
            assert r['id_user'] == 1
            assert r['nom'] == "test"

        result = c.execute("select * from data")

        for r in result:
            assert r['id'] == 1
            assert r['id_file'] == 1
            assert r['uniquId'] == "test1"
            assert r['information'] == "puit-fout"
            assert r['valeur'] == "test-testatzet"
