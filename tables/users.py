from sqlalchemy import Column, Integer, String, Boolean, DateTime
from config import Base
import datetime

class users(Base):
    __tablename__ = "akun"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    phone_number = Column(String)  # Corrected the typo here

    first_name = Column(String)
    last_name = Column(String)

    create_date = Column(DateTime, default=datetime.datetime.now())
    update_date = Column(DateTime)
