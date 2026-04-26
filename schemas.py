from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


# Used when CREATING a user (incoming data)
class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6)


# Used when UPDATING a user (all fields optional)
class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=6)


# Used when RETURNING a user (outgoing data)
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True  # allows converting DB model to Pydantic model


# Used for LOGIN
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# JWT Token response
class Token(BaseModel):
    access_token: str
    token_type: str


# Data stored inside the JWT token
class TokenData(BaseModel):
    id: Optional[int] = None