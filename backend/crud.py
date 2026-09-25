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

def update_performance(db: Session, performance_id: int, performance: schemas.PerformanceUpdate):
    db_performance = db.query(models.Performance).filter(models.Performance.id == performance_id).first()
    if not db_performance:
        return None

    db_performance.category = performance.category
    db_performance.title = performance.title
    db_performance.watched_date = performance.watched_date
    db_performance.show_time = performance.show_time
    db_performance.seat = performance.seat
    db_performance.seat_type = performance.seat_type
    db_performance.memo = performance.memo

    db.query(models.PerformanceCast).filter(models.PerformanceCast.performance_id == performance_id).delete()

    for cast in performance.casts:
        db_cast = models.PerformanceCast(
            performance_id=performance_id,
            role_name=cast.role_name,
            cast_name=cast.cast_name,
        )
        db.add(db_cast)

    db.commit()
    db.refresh(db_performance)
    return db_performance