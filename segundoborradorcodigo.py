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
        
    def cambiarDepartamento(self, nuevo_departamento):
        self.departamento = nuevo_departamento
        
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
        self.profesor = profesor
        
            
class Universidad:
    def __init__(self,nombre, direccion, codpostal):
        self.nombre=nombre
        self.direccion=direccion
        self.codpostal=codpostal
        self.miembros_departamento={TipoDepartamento.DIIC: [], TipoDepartamento.DITEC: [], TipoDepartamento.DIS: []}
        self.profesores=[]
        self.investigadores=[]
        self.alumnos=[]
        self.asignaturas=[]
    
    def anadirEstudiante(self,nombre,dni,direccion,sexo):
        for e in self.alumnos:
            if e.nombre==nombre:
                print("El estudiante ya existe")
                return
        self.alumnos.append(Estudiante(nombre,dni,direccion,sexo))
    
    def borrarEstudiante(self,nombre,dni,direccion,sexo):
        for estudiante in self.alumnos:
            if (estudiante.nombre == nombre and estudiante.dni == dni and
                    estudiante.direccion == direccion and estudiante.sexo == sexo):
                self.estudiantes.remove(estudiante)
            else:
                print("El alumno que quiere borrar no existe")
                
    def anadirProfesorTitular(self,nombre,dni,direccion,sexo,departamento,area_invest):
        for profesor in self.profesores:
            if profesor.nombre == nombre and profesor.dni==dni:
                print("El profesor titular ya existe")
                return
        profesor = ProfesorTitular(nombre, dni, direccion, sexo, departamento, area_invest)
        self.miembros_departamento[departamento].append(MiembroDepartamento(nombre,dni,direccion,sexo,departamento))
        self.profesores.append(profesor)
        #como los profesores titulares tambien son investigadores los añadimos a la lista de investigadores 
        self.investigadores.append(profesor)
        
    def anadirProfesorAsociado(self,nombre,dni,direccion,sexo,departamento):
        for profesor in self.profesores:
            if profesor.nombre == nombre and profesor.dni==dni:
                print("El profesor asociado ya existe")
                return
        profesor = ProfesorAsociado(nombre, dni, direccion, sexo, departamento)
        self.miembros_departamento[departamento].append(MiembroDepartamento(nombre,dni,direccion,sexo,departamento))
        self.profesores.append(profesor)
    
    def anadirInvestigador(self, nombre, dni, direccion, sexo, departamento,area_invest):
        for investigador in self.investigadores:
            if investigador.nombre == nombre and investigador.dni==dni:
                print("El investigador ya existe")
                return

        investigador = Investigador(nombre, dni, direccion, sexo)
        self.miembros_departamento[departamento].append(MiembroDepartamento(nombre,dni,direccion,sexo,departamento,area_invest))
        self.investigadores.append(investigador)
        
    def borrarProfesorTitular(self, nombre, dni):
        profesor_encontrado = None
        for profesor in self.profesores_titulares:
            if profesor.nombre == nombre and profesor.dni == dni:
                profesor_encontrado = profesor
                self.profesores_titulares.remove(profesor)
                break

        if profesor_encontrado:
            for departamento, miembros in self.miembros_departamento.items():
                for miembro in miembros:
                    if miembro.nombre == nombre:
                        self.miembros_departamento[departamento].remove(miembro)
        else:
            print("El profesor titular no existe")

    def borrarProfesorAsociado(self, nombre, dni):
        profesor_encontrado = None
        for profesor in self.profesores_asociados:
            if profesor.nombre == nombre and profesor.dni == dni:
                profesor_encontrado = profesor
                self.profesores_asociados.remove(profesor)
                break

        if profesor_encontrado:
            for departamento, miembros in self.miembros_departamento.items():
                for miembro in miembros:
                    if miembro.nombre == nombre:
                        self.miembros_departamento[departamento].remove(miembro)
        else:
            print("El profesor asociado no existe")

    def borrarInvestigador(self, nombre, dni):
        investigador_encontrado = None
        for investigador in self.investigadores:
            if investigador.nombre == nombre and investigador.dni == dni:
                investigador_encontrado = investigador
                self.investigadores.remove(investigador)
                break

        if investigador_encontrado:
            for departamento, miembros in self.miembros_departamento.items():
                for miembro in miembros:
                    if miembro.nombre == nombre:
                        self.miembros_departamento[departamento].remove(miembro)
        else:
            print("El investigador no existe")