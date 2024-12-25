from typing import Generic, Optional, TypeVar
from pydantic import BaseModel, Field

# Tentukan TypeVar
T = TypeVar('T')

# Model untuk Generic
class MyModel(BaseModel, Generic[T]):
    value: T


# Model untuk login
class Login(BaseModel):
    username: str
    password: str


# Model untuk register
class Register(BaseModel):
    username: str
    password: str
    email: str
    phone_number: str  # Corrected typo

    first_name: str
    last_name: str


# Response model
class ResponseSchema(BaseModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T] = None


# Model untuk token
class TokenResponse(BaseModel):
    access_token: str
    token_type: str
