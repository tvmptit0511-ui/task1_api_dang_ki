from app.models import User

BODY = {"full_name": "Trần Văn Mỹ", "email": "my@example.com",
        "password": "Abcdef1@", "confirm_password": "Abcdef1@"}
URL = "/api/auth/register"


def test_201_thanh_cong_khong_tra_password(client):
    r = client.post(URL, json=BODY)
    assert r.status_code == 201
    d = r.json()["data"]
    assert d["email"] == "my@example.com" and d["role"] == "student"
    assert "password" not in d and "password_hash" not in d


def test_mat_khau_trong_db_da_bam(client, db_session):
    client.post(URL, json=BODY)
    u = db_session.query(User).filter_by(email="my@example.com").one()
    assert u.password_hash.startswith("$2") and u.password_hash != BODY["password"]


def test_409_email_trung_khong_phan_biet_hoa_thuong(client):
    client.post(URL, json=BODY)
    r = client.post(URL, json={**BODY, "email": "MY@Example.com"})
    assert r.status_code == 409 and r.json()["code"] == "EMAIL_EXISTS"


def test_422_du_lieu_sai(client):
    r = client.post(URL, json={**BODY, "email": "x", "password": "123"})
    assert r.status_code == 422
    errs = r.json()["errors"]
    assert "email" in errs and "password" in errs


def test_422_confirm_khong_khop(client):
    r = client.post(URL, json={**BODY, "confirm_password": "Khac1@abc"})
    assert r.status_code == 422
    assert r.json()["errors"]["confirm_password"] == ["Mật khẩu xác nhận không khớp"]


def test_422_thieu_truong_va_sai_kieu(client):
    r = client.post(URL, json={"full_name": 123})
    assert r.status_code == 422
    assert {"full_name", "email", "password", "confirm_password"} <= set(r.json()["errors"])


def test_400_json_hong(client):
    r = client.post(URL, content="{bad", headers={"Content-Type": "application/json"})
    assert r.status_code == 400 and r.json()["code"] == "INVALID_JSON"
