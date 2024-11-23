#!/usr/bin/env python3
""" User Module
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """User Class"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    hashed_password = Column(String)
    session_id = Column(String)
    reset_token = Column(String)

    def __repr__(self):
        return ("<User(id='%d', email='%s', hashed_password='%s', session_id='%s'" + 
                "reset_token='%s')>" % (self.id, self.email, self.hashed_password,
                self.session_id, self.reset_token))
