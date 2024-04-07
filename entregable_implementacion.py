from enum import Enum
from abc import ABCMeta, abstractmethod

######EXCEPCIONES########
'''
Las clases de excepciones definidas en el código son subclases de la clase Exception de Python. 
Estas clases de excepciones personalizadas se utilizan para manejar situaciones excepcionales específicas que pueden ocurrir durante la ejecución del programa. 
Se utilizan en los métodos de la clase Universidad para manejar situaciones como la adición de un estudiante/profesor/investigador que ya existe, 
la eliminación de un profesor/investigador que no existe, la asignación de un profesor a una asignatura que no existe, etc.
Gracias a estas excepciones, podremos capturar y tratar de forma adecuada diferentes errores que puedan ocurrir durante la ejecución del sistema
'''

class EstudianteExistenteError(Exception):
    def __init__(self, mensaje="El estudiante ya existe"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ProfesorExistenteError(Exception):
    def __init__(self, mensaje="El profesor ya existe"):
        super().__init__(mensaje)

class InvestigadorExistenteError(Exception):
    def __init__(self, mensaje="El investigador ya existe"):
        super().__init__(mensaje)

class AsignaturaExistenteError(Exception):
    def __init__(self, mensaje="La asignatura ya existe"):
        super().__init__(mensaje)

class EstudianteNoEncontradoError(Exception):
    def __init__(self, mensaje="El estudiante no se encuentra en la universidad."):
        super().__init__(mensaje)

class ProfesorNoExistenteError(Exception):
    def __init__(self, mensaje="El profesor titular no existe"):
        super().__init__(mensaje)

class InvestigadorNoExistenteError(Exception):
    def __init__(self, mensaje="El investigador no existe"):
        super().__init__(mensaje)

class AsignaturaNoExistenteError(Exception):
    def __init__(self, mensaje="La asignatura no existe"):
        super().__init__(mensaje)

class EstudianteAsignaturaError(Exception):
    def __init__(self, mensaje="El estudiante no está matriculado en esa asignatura"):
        super().__init__(mensaje)
        
########IMPLEMENTACION########

class TipoDepartamento(Enum): #al existir 3 tipos de departamentos, creamos un enumerado para reflejarlo
    DIIC = 0
    DITEC = 1
    DIS = 2
    CONGELADO = 3     

class Persona(metaclass=ABCMeta): #clase abstracta de la que heredaran todos los tipos de personas
    def __init__(self,nombre,dni,direccion,sexo):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo= sexo
        
    @abstractmethod
    def devuelveDatos(self):  #un metodo que tendran en comun para poder devolver la informacion de cada tipo de persona
        pass
    
class MiembroDepartamento(Persona): #hemos creado esta clase de la que heredaran profesor asociado e investigador ya que asi podremos englobar que todos ellos tienen un departamento 
    def __init__(self,nombre,dni,direccion,sexo,departamento):
        super().__init__(nombre,dni,direccion,sexo)
        self.departamento=departamento
        
    def cambiarDepartamento(self, nuevo_departamento):
        self.departamento = nuevo_departamento
        
    def devuelveDatos(self):
        return "Nombre: " +self.nombre+ " DNI:" +str(self.dni)+" Direccion: "+str(self.direccion)+" Sexo: " +str(self.sexo)+" Departamento: " +str(self.departamento)
    
class ProfesorAsociado(MiembroDepartamento): #hereda de miembro de departamento al poseer un departamento y esta clase a su vez tendra otros atributos propios
    def __init__(self,nombre,dni,direccion,sexo,departamento):
        super().__init__(nombre,dni,direccion,sexo,departamento)
        self.asignaturas=[]
        
    def cambiarDepartamento(self,nuevo_departamento):
        return super().cambiarDepartamento(nuevo_departamento)  
    
    def anadirAsignatura(self,asignatura):
        self.asignaturas.append(asignatura) 
        
    def devuelveDatos(self):
        return super().devuelveDatos()+" Asignaturas: "+str(self.asignaturas)

class Investigador(MiembroDepartamento): #hereda de miembro de departamento al poseer un departamento y ademas tiene un area que investigar
    def __init__(self,nombre,dni,direccion,sexo,departamento,area_invest):
        super().__init__(nombre,dni,direccion,sexo,departamento)
        self.area_invest=area_invest
        
    def cambiarDepartamento(self,nuevo_departamento):
        return super().cambiarDepartamento(nuevo_departamento)

    def devuelveDatos(self):
        return super().devuelveDatos()+" Área de Investigacion: "+str(self.area_invest)

class ProfesorTitular(Investigador):   #hereda de investigador ya que un profesor titular tambien tiene el rol de investigador por lo que hereda sus atributos
    def __init__(self,nombre,dni,direccion,sexo,departamento, area_invest):
        super().__init__ (nombre,dni,direccion,sexo,departamento,area_invest)
        self.asignaturas=[]
    
    def cambiarDepartamento(self,nuevo_departamento):
        return super().cambiarDepartamento(nuevo_departamento)
    
    def anadirAsignatura(self,asignatura):
        self.asignaturas.append(asignatura)

    def devuelveDatos(self):
        return super().devuelveDatos()+" Asignaturas: "+str(self.asignaturas)
        
        
class Estudiante(Persona): #hereda de persona 
    def __init__(self,nombre,dni,direccion,sexo):
        super().__init__(nombre,dni,direccion,sexo)
        self.asignaturas=[]
    
    def matricularAsignatura(self,asignatura):
        self.asignaturas.append(asignatura)
    
    def quitarMatriculaAsignatura(self,asignatura):
        self.asignaturas.remove(asignatura)

    def devuelveDatos(self):
        return "Nombre: " +self.nombre+ " DNI:" +str(self.dni)+" Direccion: "+str(self.direccion)+" Sexo: " +str(self.sexo)+" Asignaturas: " +str(self.asignaturas)
    
class Asignatura:
    def __init__(self, nombre_asignatura):
        self.nombre=nombre_asignatura
        self.profesor=None
        self.alumnos=[]
        
    def asignarProfesor(self, profesor):
        self.profesor = profesor
        
class Universidad: #Esta clase tiene la responsabilidad de gestionar diferentes aspectos de una universidad, como la gestión de estudiantes, profesores, investigadores, asignaturas, etc
    
    def __init__(self,nombre, direccion, codpostal):
        self.nombre=nombre
        self.direccion=direccion
        self.codpostal=codpostal
        self._miembrosdepartamento={TipoDepartamento.DIIC: [], TipoDepartamento.DITEC: [], TipoDepartamento.DIS: []}
        self._profesores=[]
        self._investigadores=[]
        self._alumnos=[]
        self._asignaturas=[]
    
    #creamos los metodos encargados de añadir y borrar miembros de departamento y estudiantes por separado
    #es importante comprobar antes de añadir a la universidad que esos estudiantes/profesores/investigadores no existan previamente para no insertarlos por duplicado
    def anadirEstudiante(self,nombre,dni,direccion,sexo):
        for e in self._alumnos:
            if e.dni==dni:
                raise EstudianteExistenteError()
        self._alumnos.append(Estudiante(nombre,dni,direccion,sexo))
    
    def borrarEstudiante(self,nombre,dni):
        for estudiante in self._alumnos:
            if (estudiante.nombre == nombre and estudiante.dni == dni):
                self._alumnos.remove(estudiante)
          
    def anadirProfesor(self,nombre,dni,direccion,sexo,departamento,area_invest=None): #ponemos area de investigacion como None para poder distinguir entre profesores asociados y titulares ya que profesores titulares poseen ese atributo y los asociados no
        for profesor in self._profesores:
            if profesor.nombre == nombre and profesor.dni==dni:
                raise ProfesorExistenteError()
        if area_invest:#si el profesor posee un area de investigacion que no es None, insertamos un profesorTitular
            profesor = ProfesorTitular(nombre, dni, direccion, sexo, departamento, area_invest)
            self._investigadores.append(profesor) #como los profesores titulares tambien son investigadores los añadimos a la lista de investigadores  
        else: #por el contrario, insertamos un profesor asociado
            profesor = ProfesorAsociado(nombre, dni, direccion, sexo, departamento)
                       
        self._miembrosdepartamento[departamento].append(MiembroDepartamento(nombre,dni,direccion,sexo,departamento))
        self._profesores.append(profesor)

    def anadirInvestigador(self, nombre, dni, direccion, sexo, departamento,area_invest):
        for investigador in self._investigadores:
            if investigador.nombre == nombre and investigador.dni==dni:
                raise InvestigadorExistenteError()

        investigador = Investigador(nombre, dni, direccion, sexo, departamento, area_invest)
        self._miembrosdepartamento[departamento].append(MiembroDepartamento(nombre,dni,direccion,sexo,departamento))
        self._investigadores.append(investigador)
        
    def borrarProfesor(self, nombre, dni):
        profesor_encontrado = None
        for profesor in self._profesores:
            if profesor.nombre == nombre and profesor.dni == dni:
                profesor_encontrado = profesor
                self._profesores.remove(profesor)
                break
        if profesor_encontrado:
            for departamento, miembros in self._miembrosdepartamento.items():
                for miembro in miembros:
                    if miembro.nombre == nombre:
                        self._miembrosdepartamento[departamento].remove(miembro)
        else:
            raise ProfesorNoExistenteError()

    def borrarInvestigador(self, nombre, dni):
        investigador_encontrado = None
        for investigador in self._investigadores:
            if investigador.nombre == nombre and investigador.dni == dni:
                investigador_encontrado = investigador
                self._investigadores.remove(investigador)
                break

        if investigador_encontrado:
            for departamento, miembros in self._miembrosdepartamento.items():
                for miembro in miembros:
                    if miembro.nombre == nombre:
                        self._miembrosdepartamento[departamento].remove(miembro)
        else:
            raise InvestigadorNoExistenteError()
    
    #creamos asignaturas y asignamos los profesores a ellas y matriculamos a los estudiantes
      
    def crearAsignatura(self,nombre_asignatura):
        for asignatura in self._asignaturas: #debemos comprobar si la asignatura ya existe para no volverla a insertar
            if asignatura.nombre==nombre_asignatura:
                raise AsignaturaExistenteError()
        self._asignaturas.append(Asignatura(nombre_asignatura))
    
    #debemos comprobar que los estudiantes/profesores existan para poder asignarle una asignatura
    def matricularEstudianteAsignatura(self, nombre,dni,nombre_asignatura):
        for asignatura in self._asignaturas:
            if asignatura.nombre==nombre_asignatura:
                for estudiante in self._alumnos:
                    if estudiante.nombre == nombre and estudiante.dni == dni:
                        estudiante.matricularAsignatura(asignatura.nombre)
                        return
        raise EstudianteNoEncontradoError()
                        
    def borrarEstudianteAsignatura(self, nombre,dni, asignatura):
        for estudiante in self._alumnos:
            if estudiante.nombre == nombre and estudiante.dni == dni:
                estudiante.quitarMatriculaAsignatura(asignatura)
                return
        raise EstudianteNoEncontradoError()
                
    def asignarProfesorAsignatura(self,nombre_profesor,nombre_asignatura):
        for asignatura in self._asignaturas:
            if nombre_asignatura==asignatura.nombre:
                for p in self._profesores:
                    if p.nombre==nombre_profesor:
                        asignatura.asignarProfesor(p.nombre)
                        p.anadirAsignatura(asignatura.nombre)
                        return
        raise ProfesorNoExistenteError()
    
    #listamos toda la informacion que llevamos hasta ahora                    
    def listadoInvestigadores(self):
        print("LISTADO INVESTIGADORES")
        for i in self._investigadores:
            print("\t",i.devuelveDatos())

    def listadoProfesores(self):
        print("LISTADO PROFESORES")
        for p in self._profesores:
            print("\t", p.devuelveDatos())
        print ()

    def listadoEstudiantes(self):
        print("LISTADO ESTUDIANTES")
        for e in self._alumnos:
            print("\t", e.devuelveDatos())
        print ()
        
    
    def listadoMiembrosDepartamento(self, departamento):
        if departamento not in self._miembrosdepartamento:
            print("Departamento no válido.")
        print ()

        print(f"LISTADO MIEMBROS DEL DEPARTAMENTO {departamento}")
        for miembro in self._miembrosdepartamento[departamento]:
            print("\t",miembro.devuelveDatos())
        print ()
    
    def listadoInformacionAsignatura(self,nombre_asignatura): #listamos tanto la asignatura como sus profesores y estudiantes
        print("LISTADO DE INFORMACION EN LA ASIGNATURA: ", nombre_asignatura)
        for asignatura in self._asignaturas:
            if asignatura.nombre == nombre_asignatura:
                print("\t", "Profesor: ", asignatura.profesor)
                print("\t", "Estudiantes:")
                for estudiante in self._alumnos:
                    if nombre_asignatura in estudiante.asignaturas:
                        print("\t", estudiante.devuelveDatos())
        print()
    
    #todos los miembros de departamento tienen el derecho de cambiar su departamento ya sean profesores o investigadores         
    def cambiarDepartamentoMiembro(self, nombre, dni, nuevo_departamento):
        miembro_encontrado = None
        for departamento, miembros in self._miembrosdepartamento.items():
            for miembro in miembros:
                if miembro.nombre == nombre and miembro.dni == dni:
                    miembro_encontrado = miembro
                    miembros.remove(miembro)  # Removemos el miembro del departamento actual

        if miembro_encontrado:
            miembro_encontrado.cambiarDepartamento(nuevo_departamento)  # Cambiamos el departamento del miembro
            self._miembrosdepartamento[nuevo_departamento].append(miembro_encontrado)  # Agregamos al nuevo departamento

            # Actualizamos la lista de profesores
            for profesor in self._profesores:
                if profesor.nombre==nombre:
                    profesor.cambiarDepartamento(nuevo_departamento)
                    
        else:
            print("No se encontró ningún miembro con ese nombre y DNI.")
