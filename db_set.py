import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Leader(Base):
    __tablename__ = 'leader'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    leader_id = Column(Integer, ForeignKey('leader.id'))
    leader = relationship(Leader)
    question = Column(String(250), nullable=False)
    answer = Column(String(250), nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    done = Column(Boolean, unique=False, default=False)
    useranswer = Column(String(250), nullable=False)

engine = create_engine('sqlite:///sarah.db?check_same_thread=False')
Base.metadata.create_all(engine)
