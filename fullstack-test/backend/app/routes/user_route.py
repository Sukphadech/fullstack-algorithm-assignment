from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_


from app.database import SessionLocal
from app.models.user_model import User
from app.schemas.user_schema import (
    UserCreate,
    UserUpdate,
    UserResponse
)


route = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
#Create user     
@route.post("/api/user", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()
    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )
    new_user = User(
        name = user.name,
        age = user.age,
        email = user.email,
        avatar_url = user.avatar_url
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

#Get all users 
@route.get("/api/user")
def get_users(
    q: str = "",
    start: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(User)
    if q:
        query = query.filter(
            or_(
                User.name.ilike(f"%{q}%"),
                User.email.ilike(f"%{q}%")
            )
        )
    total = query.count()
    
    users = query.offset(start).limit(limit).all()
    
    return{
        "total": total,
        "start": start,
        "limit": limit,
        "data": users
    }
    
#Get user detail by id     
@route.get("/api/user/{user_id}", response_model=UserResponse)
def det_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=4,
            detail="User not found"
        )
    return user

#Update user by id
@route.put("/api/user/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    updated_user: UserUpdate,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    existing_email = db.query(User).filter(
        User.email == updated_user.email,
        User.id != user_id
    ).first()
    
    if existing_email:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )
    user.name = updated_user.name
    user.age = updated_user.age
    user.email = updated_user.email
    user.avatar_url = updated_user.avatar_url
    
    db.commit()
    db.refresh(user)
    
    return user


#Delete user by id 
@route.delete("/api/user/{user_id}")
def delete_user(user_id: int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )  
    db.delete(user)
    db.commit()
    
    return {"message": "User deleted successfully"}