from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .errors import AppError
from .models import User
from .schemas import RegisterRequest
from .security import hash_password


def register_user(db: Session, data: RegisterRequest) -> User:
    if db.scalar(select(User).where(User.email == data.email)):
        raise AppError(409, "EMAIL_EXISTS", "Email đã được đăng ký")

    user = User(
        full_name=data.full_name,
        email=data.email,
        password_hash=hash_password(data.password),
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError:  # 2 request dang ky cung luc
        db.rollback()
        raise AppError(409, "EMAIL_EXISTS", "Email đã được đăng ký")
    db.refresh(user)
    return user
