from pydantic import BaseModel, EmailStr, Field, field_validator


class RegisterSchema(BaseModel):
    role: int | None
    email: EmailStr
    name: str
    password: str = Field(min_length=8)


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"
