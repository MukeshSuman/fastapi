from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, DB_SERVICE

database_url = URL.create(
    DB_SERVICE,
    username=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB_NAME,
)

db_url = DB_SERVICE + "://" + DB_USERNAME + ":" + DB_PASSWORD + "@" + DB_HOST + "/" + DB_NAME

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

metadata = Base.metadata


def get_dbase():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
