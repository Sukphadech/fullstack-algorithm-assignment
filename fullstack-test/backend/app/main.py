from fastapi import FastAPI
from app.database import engine, Base
from app.models.user_model import User
from app.routes.user_route import route as user_router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router)

@app.get("/")
def root():
    return {"message":"Backed is running"}