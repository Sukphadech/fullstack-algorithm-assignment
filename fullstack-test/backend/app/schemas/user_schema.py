from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    age: int
    email: EmailStr
    avatar_url: Optional[str] = None
    
class UserUpdate(BaseModel):
    name: str
    age: int
    email: EmailStr
    avatar_url: Optional[str] = None
    
class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr
    avatar_url: Optional[str] 
    
class Config:
    from_attributes = True
    
    