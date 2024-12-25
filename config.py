from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL =  'postgresql://postgres:FhyRNQXnDIQQkgbJgjLYiMGZDmSbzXGG@junction.proxy.rlwy.net:13199/railway'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally : db.close()

#jwt
SECRET_KEY="naik_anjing_aja_enak_123"
ALGORITHM = "HS256"
ACCES_TOKEN_EXPIRED_MINUTES = 30
