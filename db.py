from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Contacts(Base):
  __tablename__ = 'Contacts_table'
  id = Column(Integer, primary_key=True)
  name = Column(String(255), nullable=False)
  surname = Column(String(255), nullable=False)
  country = Column(String(255), nullable=False)
  number = Column(Integer, nullable=False)
  email = Column(String(255), nullable=False)

engine = create_engine("sqlite:///contacts_db.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()