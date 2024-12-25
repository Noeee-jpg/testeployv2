from typing import Generic, Optional, TypeVar
from pydantic.generics import GenericModel
from pydantic import BaseModel, Field

T = TypeVar("T")

#login
class Login(BaseModel):
    username : str
    password : str

#register
class Register(BaseModel):
    username: str
    password: str
    email: str
    phone_number: str  # Corrected the typo here

    first_name: str
    last_name: str


#response model
class ResponseSchema(BaseModel):
    code :str
    status : str
    message :str
    result : Optional[T] = None

#token
class TokenResponse(BaseModel):
    access_token : str
    token_type : str