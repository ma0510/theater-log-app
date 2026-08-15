from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
import crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 開発中はすべて許可(本番では絞る)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Hello, theater-log-app!"}


@app.post("/performances", response_model=schemas.PerformanceResponse)
def create_performance(performance: schemas.PerformanceCreate, db: Session = Depends(get_db)):
    return crud.create_performance(db, performance)


@app.get("/performances", response_model=List[schemas.PerformanceResponse])
def read_performances(db: Session = Depends(get_db)):
    return crud.get_performances(db)


@app.get("/performances/{performance_id}", response_model=schemas.PerformanceResponse)
def read_performance(performance_id: int, db: Session = Depends(get_db)):
    return crud.get_performance(db, performance_id)