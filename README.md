# Task 1 – API đăng ký (3 điểm)
Bản **đầy đủ, chạy được** (FastAPI + MySQL). API đăng ký cần dữ liệu đã kiểm tra (Task 2) và mật khẩu đã băm (Task 3) nên 2 module đó được kèm sẵn để chạy.

| Loại | File |
|---|---|
| **Của Task 1** | `app/routers/auth.py`, `app/services.py`, `app/models.py`, `app/database.py`, `app/main.py`, `sql/001_create_users.sql`, `tests/test_register_api.py` |
| Phụ thuộc Task 2 | `app/schemas.py`, `app/errors.py`, `app/error_handlers.py` |
| Phụ thuộc Task 3 | `app/security.py` |

## Chạy
```bash
python -m venv venv && source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                                  # sửa user/password MySQL
mysql -u root -p < sql/001_create_users.sql
uvicorn app.main:app --reload                         # Swagger: http://localhost:8000/docs
python -m pytest -q                                   # test không cần MySQL
```
