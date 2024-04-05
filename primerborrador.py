from enum import Enum
from abc import ABCMeta, abstractmethod

class TipoDepartamento(Enum):
    DIIC = 0
    DITEC = 1
    DIS = 2
    CONGELADO = 3     

class Persona(metaclass=ABCMeta): 
    def __init__(self,nombre,dni,direccion,sexo):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo= sexo
        
    @abstractmethod
    def devuelveDatos(self):
        pass
    
class MiembroDepartamento(Persona):
    def __init__(self,nombre,dni,direccion,sexo,departamento):
        super().__init__(nombre,dni,direccion,sexo)
        self.departamento=departamento
        
    def devuelveDatos(self):
        return "Nombre: " + self.nombre + "\n" + \
               "DNI:" + str(self.dni) + "\n" + \
               "Direccion: " + str(self.direccion) + "\n" + \
               "Sexo: " + str(self.sexo) + "\n" + \
               "Departamento: " + str(self.departamento)
    
class ProfesorAsociado(MiembroDepartamento):
    def __init__(self,nombre,dni,direccion,sexo,departamento):
        super().__init__(nombre,dni,direccion,sexo,departamento)
        self.asignaturas=[]
        
    def devuelveDatos(self):
        return super().devuelveDatos()+"\n" + \
        "Asignaturas: "+str(self.asignaturas)

class Investigador(MiembroDepartamento):
    def __init__(self,nombre,dni,direccion,sexo,departamento,area_invest):
        super().__init__(nombre,dni,direccion,sexo,departamento)
        self.area_invest=area_invest
        
    def devuelveDatos(self):
        return super().devuelveDatos()+"\n" + \
        "Área de Investigacion: "+str(self.area_invest)

class ProfesorTitular(Investigador):
    def __init__(self,nombre,dni,direccion,sexo,departamento, area_invest):
        super().__init__ (nombre,dni,direccion,sexo,departamento,area_invest)
        self.asignaturas=[]

    def devuelveDatos(self):
        return super().devuelveDatos()+"\n" + \
        "Asignaturas: "+str(self.asignaturas)
        
        
class Estudiante(Persona):
    def __init__(self,nombre,dni,direccion,sexo):
        super().__init__(nombre,dni,direccion,sexo)
        self.asignaturas=[]
    
    def matricularAsignatura(self,asignatura):
        self.asignaturas.append(asignatura)
        
    def quitarMatriculaAsignatura(self,asignatura):
        self.asignaturas.remove(asignatura)

    def devuelveDatos(self):
        return "Nombre: " + self.nombre + "\n" + \
               "DNI:" + str(self.dni) + "\n" + \
               "Direccion: " + str(self.direccion) + "\n" + \
               "Sexo: " + str(self.sexo) + "\n" + \
               "Asignaturas: " + str(self.asignaturas)

class Asignatura:
    def __init__(self, nombre_asignatura):
        self.nombre=nombre_asignatura
        self.profesor=None
        self.alumnos=[]
        
    def asignarProfesor(self, profesor):
        if isinstance(profesor, ProfesorTitular) or isinstance(profesor, ProfesorAsociado):
            self.profesor = profesor
        else:
            print("Error: El objeto no es un ProfesorTitular ni un ProfesorAsociado.")