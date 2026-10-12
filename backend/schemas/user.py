from pydantic import BaseModel, EmailStr,field_validator

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_password_length(cls, value: str) -> str:
        if len(value.encode("utf-8")) > 72:
            raise ValueError("Password must not exceed 72 bytes")
        return value
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str