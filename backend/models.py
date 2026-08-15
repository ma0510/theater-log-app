import enum
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base


class Category(str, enum.Enum):
    SHIKI = "ミュージカル（劇団四季）"
    MUSICAL_OTHER = "ミュージカル（その他）"
    KABUKI = "歌舞伎"
    OTHER = "その他"


class ShowTime(str, enum.Enum):
    MATINEE = "マチネ"
    SOIREE = "ソワレ"
    DAY_PART = "昼の部"
    NIGHT_PART = "夜の部"
    PART1 = "1部"
    PART2 = "2部"
    PART3 = "3部"


class Performance(Base):
    __tablename__ = "performances"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(Enum(Category))       # カテゴリ
    title = Column(String)                  # 公演名
    watched_date = Column(Date)             # 日付
    show_time = Column(Enum(ShowTime))      # 上演時間
    seat = Column(String)                   # 座席
    seat_type = Column(String)              # 席種
    memo = Column(String, nullable=True)    # 感想

    casts = relationship("PerformanceCast", back_populates="performance", cascade="all, delete-orphan")


class PerformanceCast(Base):
    __tablename__ = "performance_casts"

    id = Column(Integer, primary_key=True, index=True)
    performance_id = Column(Integer, ForeignKey("performances.id"))
    role_name = Column(String)   # 役名
    cast_name = Column(String)   # キャスト

    performance = relationship("Performance", back_populates="casts")