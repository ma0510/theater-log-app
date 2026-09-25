from pydantic import BaseModel
from datetime import date
from typing import List, Optional
from models import Category, ShowTime


class CastCreate(BaseModel):
    role_name: str
    cast_name: str


class PerformanceCreate(BaseModel):
    category: Category
    title: str
    watched_date: date
    show_time: ShowTime
    seat: str
    seat_type: str
    memo: Optional[str] = None
    casts: List[CastCreate]


class CastResponse(CastCreate):
    id: int

    class Config:
        from_attributes = True


class PerformanceResponse(PerformanceCreate):
    id: int
    casts: List[CastResponse]

class PerformanceUpdate(BaseModel):
    category: Category
    title: str
    watched_date: date
    show_time: ShowTime
    seat: str
    seat_type: str
    memo: Optional[str] = None
    casts: List[CastCreate]