from fastapi import APIRouter, Depends
from models.users import ResponseSchema, TokenResponse, Login, Register
from sqlalchemy.orm import Session
from config import get_db
from passlib.context import CryptContext
from repository.users import UsersRepo, JWTRepo
from tables.users import users

router = APIRouter(
    tags=["Authentication"]  # Gunakan list
)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('/signup')
async def signup(request: Register, db: Session = Depends(get_db)):
    try:
        hashed_password = pwd_context.hash(request.password)  # Hash the password
        _user = users(
            username=request.username,
            password=hashed_password,  # Save hashed password
            email=request.email,
            phone_number=request.phone_number,
            first_name=request.first_name,
            last_name=request.last_name,
        )
        UsersRepo.insert(db, _user)
        return ResponseSchema(code="200", status="ok", message="Success save data").dict()
    except Exception as error:
        print(error.args)
        return ResponseSchema(code="500", status="error", message="Internal server error").dict()


@router.post('/login')
async def login(request: Login, db: Session = Depends(get_db)):
    try:
        _user = UsersRepo.find_by_username(db, request.username)

        if not _user or not pwd_context.verify(request.password, _user.password):  # Verify hashed password
            return ResponseSchema(code="400", status="Bad request", message="Invalid username or password").dict()

        token = JWTRepo.generate_token({"sub": _user.username})
        return ResponseSchema(
            code="200",
            status="ok",
            message="Success login",
            result=TokenResponse(access_token=token, token_type="bearer").dict()
        ).dict()
    except Exception as error:
        error_message = str(error.args)
        print(error_message)
        return ResponseSchema(code="500", status="error", message="Internal server error").dict()


