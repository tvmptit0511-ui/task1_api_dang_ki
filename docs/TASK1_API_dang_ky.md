# TASK1 API dang ky
Người thực hiện: Trần Văn Mỹ  |  Dự án: Gia sư AI  |  Công nghệ: Python, FastAPI, MySQL

## Task 1 – API đăng ký (3 điểm)
**Endpoint:** `POST /api/auth/register`  |  **Content-Type:** `application/json`

**Request**
```json
{
  "full_name": "Trần Văn Mỹ",
  "email": "my@example.com",
  "password": "Abcdef1@",
  "confirm_password": "Abcdef1@"
}
```
**Response thành công – 201**
```json
{
  "success": true,
  "message": "Đăng ký thành công",
  "data": { "id": 1, "full_name": "Trần Văn Mỹ", "email": "my@example.com",
            "role": "student", "status": "active", "created_at": "2026-11-09T03:00:00" }
}
```
Không bao giờ trả `password` hay `password_hash` về client.

**Mã lỗi**
| HTTP | code | Khi nào |
|---|---|---|
| 400 | INVALID_JSON | Body không phải JSON hợp lệ |
| 409 | EMAIL_EXISTS | Email đã tồn tại (không phân biệt hoa/thường) |
| 422 | VALIDATION_ERROR | Dữ liệu sai, kèm `errors` theo từng trường |

**Lỗi 422 mẫu**
```json
{ "success": false, "code": "VALIDATION_ERROR", "message": "Dữ liệu đăng ký không hợp lệ",
  "errors": { "email": ["Email không hợp lệ"], "password": ["Mật khẩu tối thiểu 8 ký tự"] } }
```
**Luồng xử lý:** Router → Pydantic validate → Service (kiểm tra email trùng, băm mật khẩu, lưu DB) → 201.
**CSDL:** bảng `users` (`sql/001_create_users.sql`), email có UNIQUE KEY, lưu `password_hash`.
