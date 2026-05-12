from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, unique=True, nullable=False)
    avatar_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    updated_at = Column(DateTime, 
                        default=datetime.utcnow,
                        onupdate=datetime.utcnow
                        )