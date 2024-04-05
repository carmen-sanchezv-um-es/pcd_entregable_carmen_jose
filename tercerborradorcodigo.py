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
        self.profesor = profesor
        
            
class Universidad:
    def __init__(self,nombre, direccion, codpostal):
        self.nombre=nombre
        self.direccion=direccion
        self.codpostal=codpostal
        self.miembros_departamento={TipoDepartamento.DIIC: [], TipoDepartamento.DITEC: [], TipoDepartamento.DIS: []}
        self.profesores_titulares=[]
        self.profesores_asociados=[]
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
        for profesor in self.profesores_titulares:
            if profesor.nombre == nombre and profesor.dni==dni:
                print("El profesor titular ya existe")
                return
        profesor = ProfesorTitular(nombre, dni, direccion, sexo, departamento, area_invest)
        self.miembros_departamento[departamento].append(MiembroDepartamento(nombre,dni,direccion,sexo,departamento))
        self.profesores_titulares.append(profesor)
        #como los profesores titulares tambien son investigadores los añadimos a la lista de investigadores 
        self.investigadores.append(profesor)
        
    def anadirProfesorAsociado(self,nombre,dni,direccion,sexo,departamento):
        for profesor in self.profesores_asociados:
            if profesor.nombre == nombre and profesor.dni==dni:
                print("El profesor asociado ya existe")
                return
        profesor = ProfesorAsociado(nombre, dni, direccion, sexo, departamento)
        self.miembros_departamento[departamento].append(MiembroDepartamento(nombre,dni,direccion,sexo,departamento))
        self.profesores_asociados.append(profesor)
    
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
            
    def crearAsignatura(self,nombre_asignatura):
        for asignatura in self.asignaturas:
            if asignatura.nombre==nombre_asignatura:
                print("La asignatura ya existe")
            else:
                self.asignatura.append(Asignatura(nombre_asignatura))
    
    def matricularEstudianteAsignatura(self, nombre,dni,asignatura):
        for estudiante in self.alumnos:
            if estudiante.nombre == nombre and estudiante.dni == dni:
                estudiante.matricularAsignatura(asignatura)
            else:
                print("El estudiante no se encuentra en la universidad.")

    def borrarEstudianteAsignatura(self, nombre,dni, asignatura):
        for estudiante in self.alumnos:
            if estudiante.nombre == nombre and estudiante.dni == dni:
                estudiante.quitarMatriculaAsignatura(asignatura)
            else:
                print("El estudiante no se encuentra en la universidad.")
                
    def asignarProfesorAsignatura(self,nombre_profesor,nombre_asignatura):
        for asignatura in self.asignaturas:
            if nombre_asignatura==asignatura.nombre:
                for pa in self.profesores_asociados:
                    for pt in self.profesores_titulares:
                        if nombre_profesor==pa.nombre or nombre_profesor==pt.nombre:
                            nombre_asignatura.asignarProfesor(nombre_profesor)

    def listadoInvestigadores(self):
        print("LISTADO INVESTIGADORES")
        for i in self.investigadores:
            print(i.devuelveDatos())

    def listadoProfesoresTitulares(self):
        print("LISTADO PROFESORES TITULARES")
        for p in self.profesores_titulares:
            print(p.devuelveDatos())
            
    def listadoProfesoresAsociados(self):
        print("LISTADO PROFESORES ASOCIADOS")
        for p in self.profesores_asociados:
            print(p.devuelveDatos())
    
    def listadoEstudiantes(self):
        print("LISTADO ESTUDIANTES")
        for e in self.alumnos:
            print(e.devuelveDatos())
    
    def listadoMiembrosDepartamento(self, departamento):
        if departamento not in self.miembros_departamento:
            print("Departamento no válido.")
            return

        print(f"LISTADO MIEMBROS DEL DEPARTAMENTO {departamento}")
        for miembro in self.miembros_departamento[departamento]:
            print(miembro.devuelveDatos())
    
    def listadoInformacionAsignatura(self,nombre_asignatura):
        for a in self.asignaturas:
            for estudiante in self.estudiantes:
                if a.nombre==nombre_asignatura:
                    if nombre_asignatura in estudiante.asignatura:
                        print(f"Listado de de informacion en la asignatura {nombre_asignatura}")
                        print(str(estudiante.devuelveDatos())+str(nombre_asignatura.profesor))
                
                
universidad=Universidad("Universidad de Murcia", "Espinardo","30800")               
             
universidad.anadirEstudiante("carmen","238126","Avenida","M")
universidad.anadirProfesorAsociado("adolfo","23888","Avenida","V",TipoDepartamento.DIIC)

universidad.crearAsignatura("MATEMATICAS")
universidad.asignarProfesorAsignatura("MATEMATICAS", "adolfo")
universidad.matricularEstudianteAsignatura("carmen","238126","MATEMATICAS")

universidad.listadoProfesoresAsociados()
universidad.listadoEstudiantes()
universidad.listadoInformacionAsignatura("MATEMATICAS")