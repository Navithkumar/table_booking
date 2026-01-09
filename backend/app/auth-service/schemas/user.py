from pydantic import BaseModel, EmailStr, Field, field_validator


def validate_bcrypt_length(password: str) -> str:
    if len(password.encode("utf-8")) > 72:
        raise ValueError("Password must be at most 72 bytes (bcrypt limit)")
    return password


class RegisterSchema(BaseModel):
    email: EmailStr
    name: str
    password: str = Field(min_length=8)

    @field_validator("email")
    @classmethod
    def normalize_email(cls, v: str) -> str:
        return v.lower()

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        return validate_bcrypt_length(v)


class LoginSchema(BaseModel):
    email: EmailStr
    password: str

    @field_validator("email")
    @classmethod
    def normalize_email(cls, v: str) -> str:
        return v.lower()

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        return validate_bcrypt_length(v)


class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"
