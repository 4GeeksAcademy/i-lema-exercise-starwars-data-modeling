import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Enum, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    subscription_date = Column(Date, nullable=False)
    character_favorites = relationship('CharacterFavorite', backref='user', lazy=True)
    planet_favorites = relationship('PlanetFavorite', backref='user', lazy=True)
    character_comments = relationship('CharacterComment', backref='user', lazy=True)
    planet_comments = relationship('PlanetComment', backref='user', lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    favorites = relationship('PlanetFavorite', backref='planet', lazy=True)
    comments = relationship('PlanetComment', backref='planet', lazy=True)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    favorites = relationship('CharacterFavorite', backref='character', lazy=True)
    comments = relationship('CharacterComment', backref='character', lazy=True)

class CharacterFavorite(Base):
    __tablename__ = 'character_favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)

class PlanetFavorite(Base):
    __tablename__ = 'planet_favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)

class CharacterComment(Base):
    __tablename__ = 'character_comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)

class PlanetComment(Base):
    __tablename__ = 'planet_comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

