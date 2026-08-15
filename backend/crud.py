from sqlalchemy.orm import Session
import models
import schemas


def create_performance(db: Session, performance: schemas.PerformanceCreate):
    db_performance = models.Performance(
        category=performance.category,
        title=performance.title,
        watched_date=performance.watched_date,
        show_time=performance.show_time,
        seat=performance.seat,
        seat_type=performance.seat_type,
        memo=performance.memo,
    )
    db.add(db_performance)
    db.commit()
    db.refresh(db_performance)

    for cast in performance.casts:
        db_cast = models.PerformanceCast(
            performance_id=db_performance.id,
            role_name=cast.role_name,
            cast_name=cast.cast_name,
        )
        db.add(db_cast)
    db.commit()
    db.refresh(db_performance)

    return db_performance


def get_performances(db: Session):
    return db.query(models.Performance).all()


def get_performance(db: Session, performance_id: int):
    return db.query(models.Performance).filter(models.Performance.id == performance_id).first()