from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Compositor(Base):
    __tablename__ = 'compositores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))

class Director(Base):
    __tablename__ = 'directores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))

class Interprete(Base):
    __tablename__ = 'interpretes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    instrumento = Column(String(255))

class Obra(Base):
    __tablename__ = 'obras'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(255))
    compositor_id = Column(Integer, ForeignKey('compositores.id'))
    director_id = Column(Integer, ForeignKey('directores.id'))
    interprete_id = Column(Integer, ForeignKey('interpretes.id'))

    compositor = relationship("Compositor")
    director = relationship("Director")
    interprete = relationship("Interprete")

motor = create_engine('sqlite:///base_de_datos_musical.db')
Base.metadata.create_all(motor)
