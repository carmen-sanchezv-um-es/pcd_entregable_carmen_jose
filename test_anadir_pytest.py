import pytest
from entregable_implementacion import *

'''
Las clases de excepciones definidas en el código son subclases de la clase Exception de Python. 
Estas clases de excepciones personalizadas se utilizan para manejar situaciones excepcionales específicas que pueden ocurrir durante la ejecución del programa
y estas clases son utilizadas en los métodos de la clase Universidad para manejar situaciones como:
añadir un estudiante/profesor/investigador que ya existe, la eliminación de un profesor/investigador que no existe, la asignación de un profesor a una asignatura que no existe etc.
Ademas tambien comprobamos que cuando añadimos un estudiante/profesor/investigador se añade correctamente ya que la longitud de la lista de cada uno se incrementa y a su vez que cuando borramos a un
profesor/estudiante/investigador se elimina correctamente
'''

class TestUniversidad:

    @pytest.fixture
    def universidad(self):
        return Universidad("Mi Universidad", "Dirección de la universidad", "12345")

    def test_anadir_estudiante(self, universidad):
        universidad.anadirEstudiante("Juan", "12345678A", "Dirección de Juan", "M")
        assert len(universidad._alumnos) == 1

    def test_borrar_estudiante(self, universidad):
        universidad.anadirEstudiante("Juan", "12345678A", "Dirección de Juan", "M")
        universidad.borrarEstudiante("Juan", "12345678A")
        assert len(universidad._alumnos) == 0

    def test_anadir_profesor(self, universidad):
        universidad.anadirProfesor("Pedro", "87654321Z", "Dirección de Pedro", "H", TipoDepartamento.DIIC)
        assert len(universidad._profesores) == 1

    def test_borrar_profesor(self, universidad):
        universidad.anadirProfesor("Pedro", "87654321Z", "Dirección de Pedro", "H", TipoDepartamento.DIIC)
        universidad.borrarProfesor("Pedro", "87654321Z")
        assert len(universidad._profesores) == 0

    def test_anadir_investigador(self, universidad):
        universidad.anadirInvestigador("Ana", "98765432X", "Dirección de Ana", "M", TipoDepartamento.DIS, "IA")
        assert len(universidad._investigadores) == 1

    def test_borrar_investigador(self, universidad):
        universidad.anadirInvestigador("Ana", "98765432X", "Dirección de Ana", "M", TipoDepartamento.DIS, "IA")
        universidad.borrarInvestigador("Ana", "98765432X")
        assert len(universidad._investigadores) == 0

    def test_crear_asignatura(self, universidad):
        universidad.crearAsignatura("Matemáticas")
        assert len(universidad._asignaturas) == 1

    def test_matricular_estudiante_asignatura(self, universidad):
        universidad.anadirEstudiante("Juan", "12345678A", "Dirección de Juan", "M")
        universidad.crearAsignatura("Matemáticas")
        universidad.matricularEstudianteAsignatura("Juan", "12345678A", "Matemáticas")
        assert universidad._alumnos[0].asignaturas == ["Matemáticas"]

    def test_asignar_profesor_asignatura(self, universidad):
        universidad.anadirProfesor("Pedro", "87654321Z", "Dirección de Pedro", "H", TipoDepartamento.DIIC)
        universidad.crearAsignatura("Matemáticas")
        universidad.asignarProfesorAsignatura("Pedro", "Matemáticas")
        assert universidad._asignaturas[0].profesor == "Pedro"

    def test_cambiar_departamento_miembro(self, universidad):
        universidad.anadirProfesor("Pedro", "87654321Z", "Dirección de Pedro", "H", TipoDepartamento.DIIC)
        universidad.cambiarDepartamentoMiembro("Pedro", "87654321Z", TipoDepartamento.DIS)
        assert universidad._miembrosdepartamento[TipoDepartamento.DIS][0].nombre == "Pedro"

    def test_borrar_estudiante_no_existente(self,universidad):
        universidad.borrarEstudiante("Juan", "12345678A")  # Intentar borrar un estudiante que no está en la lista
        assert len(universidad._alumnos) == 0  # Verificar que no se haya borrado ningún estudiante


    def test_borrar_profesor_no_existente(self,universidad):
        universidad.borrarProfesor( "Pedro", "87654321Z")  # Intentar borrar un profesor que no está en la lista
        assert len(universidad._profesores) == 0  # Verificar que no se haya borrado ningún profesor


    def test_borrar_investigador_no_existente(self,universidad):
        universidad.borrarInvestigador("Ana", "98765432X")  # Intentar borrar un investigador que no está en la lista
        assert len(universidad._investigadores) == 0  # Verificar que no se haya borrado ningún investigador