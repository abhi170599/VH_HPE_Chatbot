from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base

""" define the models to be used """

class User(Base):

    __tablename__ = 'users'
    id          = Column(Integer,primary_key=True)
    username    = Column(String(50),unique=True)
    password    = Column(String(128))

    def __init__(self,username=None,password=None):
        self.username = username
        self.password = password 

    def __repr__(self):
        return '<User %r>'%(self.username)


class Chathead(Base):

    __tablename__ = 'chatheads'
    id       = Column(Integer,primary_key=True)
    user_id  = Column(Integer,ForeignKey('users.id'))


class Message(Base):

    __tablename__ = 'messages'
    id       = Column(Integer,primary_key=True)
    message  = Column(Text)
    user     = Column(Integer,ForeignKey('users.id'))
    chat     = Column(Integer,ForeignKey('chatheads.id'))
    from_bot = Column(Integer)