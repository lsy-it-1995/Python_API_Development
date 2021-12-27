from app import schemas
import pytest
from jose import jwt
from app.config import settings
# def test_root(client):
#     respond = client.get("/")
#     print(respond.json().get('message'))
#     assert respond.json().get('message') == "hello world!!!!"
#     assert respond.status_code == 200



def test_create_user(client):
    res = client.post("/users/",json={"email": "2123@gmail.com","password": "password123"})
    user_data = schemas.UserOut(**res.json())
    assert user_data.email == "2123@gmail.com"
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user['email'],"password": test_user['password']})
    assert res.status_code == 200
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
@pytest.mark.parametrize("email, password, status_code",[
    ('123@gmail.com', 'pass', 403),
    ('ahuiggfgfha@gmail.com', '1561564', 403),
    ('123@gmail.com', 'pasdass', 403),
    (None, 'pasdass', 422),
    ('1@gmail.com', None, 422),
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data = {"username": email, "password":password})
    assert res.status_code == status_code
    # assert res.json().get('detail') == "Invalid credentials"