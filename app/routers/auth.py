from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import RegisterRequest, UserOut
from ..services import register_user

router = APIRouter(prefix="/api/auth", tags=["Auth"])


# Dung `def` (khong async) vi bam bcrypt ton CPU -> FastAPI se chay trong threadpool.
@router.post("/register", status_code=201, summary="Đăng ký tài khoản")
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    user = register_user(db, payload)
    return {
        "success": True,
        "message": "Đăng ký thành công",
        "data": UserOut.model_validate(user),
    }
