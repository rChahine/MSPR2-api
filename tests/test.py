def test_auth(client_auth_admin):
    data = client_auth_admin.get('user/me').json()

    assert data["username"] == "user"
