from sqlalchemy.orm import sessionmaker
from modelo import Compositor, Director, Interprete, motor, Obra

Session = sessionmaker(bind=motor)
sesion = Session()

def agregar_compositor(nombre):
    nuevo_compositor = Compositor(nombre=nombre)
    sesion.add(nuevo_compositor)
    sesion.commit()

def agregar_director(nombre):
    nuevo_director = Director(nombre=nombre)
    sesion.add(nuevo_director)
    sesion.commit()

def agregar_interprete(nombre, instrumento):
    nuevo_interprete = Interprete(nombre=nombre, instrumento=instrumento)
    sesion.add(nuevo_interprete)
    sesion.commit()

def agregar_obra(titulo, compositor_id, director_id, interprete_id):
    nueva_obra = Obra(titulo=titulo, compositor_id=compositor_id, director_id=director_id, interprete_id=interprete_id)
    sesion.add(nueva_obra)
    sesion.commit()

def listar_obras():
    obras = sesion.query(Obra).all()
    return obras
