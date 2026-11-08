from app.security import hash_password, validate_password_strength, verify_password


def test_mat_khau_manh():
    assert validate_password_strength("Abcdef1@") == []


def test_mat_khau_yeu():
    assert len(validate_password_strength("abc")) >= 3
    assert any("chữ hoa" in m for m in validate_password_strength("abcdefgh1@"))
    assert any("ký tự đặc biệt" in m for m in validate_password_strength("Abcdefgh1"))
    assert any("khoảng trắng" in m for m in validate_password_strength("Abc def1@"))


def test_hash_khac_nhau_moi_lan_va_verify():
    h1, h2 = hash_password("Abcdef1@"), hash_password("Abcdef1@")
    assert h1 != h2 and h1 != "Abcdef1@" and h1.startswith("$2")
    assert verify_password("Abcdef1@", h1)
    assert not verify_password("Sai-mat-khau1", h1)
    assert not verify_password(None, h1)
    assert not verify_password("Abcdef1@", "khong-phai-hash")
