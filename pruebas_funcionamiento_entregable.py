
from entregable_implementacion import *

##########PRUEBAS DE FUNCIONAMIENTO#############

# Creamos la universidad
universidad = Universidad("Universidad de Murcia", "Campus de Espinardo", "12345")

# Añadimos profesores tanto titulares como asociados
universidad.anadirProfesor("Juan Pérez", "12345678A", "Calle 111", "V", TipoDepartamento.DIIC, "Ciencia de Datos")
universidad.anadirProfesor("Ana García", "11111111X", "Calle 222", "M", TipoDepartamento.DIIC, "Redes de Computadoras")
universidad.anadirProfesor("Carlos Ruiz", "22222222Y", "Calle 333", "V", TipoDepartamento.DIS, "Inteligencia Artificial")
universidad.anadirProfesor("María Gómez", "87654321B", "Calle 444", "M", TipoDepartamento.DITEC)
universidad.anadirProfesor("Elena Vázquez", "33333333Z", "Calle 555", "M", TipoDepartamento.DITEC)

# Añadimos investigadores
universidad.anadirInvestigador("Pedro López", "98765432C", "Calle 666", "V", TipoDepartamento.DIS, "Inteligencia Artificial")
universidad.anadirInvestigador("Miguel Fernández", "44444444W", "Calle 777", "V", TipoDepartamento.DITEC, "Seguridad Informática")
universidad.anadirInvestigador("Sara López", "55555555V", "Calle 888", "M", TipoDepartamento.DIS, "Procesamiento de Imágenes")

# Añadimos estudiantes
universidad.anadirEstudiante("Laura Martínez", "34567890D", "Calle 999", "M")
universidad.anadirEstudiante("David Martínez", "66666666U", "Calle 121", "V")
universidad.anadirEstudiante("Lucía Pérez", "77777777T", "Calle 123", "M")
universidad.anadirEstudiante("Javier Rodríguez", "88888888S", "Calle 124", "V")
universidad.anadirEstudiante("Marina Sánchez", "99999999R", "Calle 000", "M")

# Creamos asignaturas
universidad.crearAsignatura("Matemáticas")
universidad.crearAsignatura("Física")
universidad.crearAsignatura("Programación Avanzada")
universidad.crearAsignatura("Bases de Datos")

# Asignamos los profesores a las asignaturas
universidad.asignarProfesorAsignatura("Juan Pérez", "Matemáticas")
universidad.asignarProfesorAsignatura("Ana García", "Física")
universidad.asignarProfesorAsignatura("Carlos Ruiz", "Programación Avanzada")
universidad.asignarProfesorAsignatura("María Gómez", "Bases de Datos")

# Matriculamos los estudiantes en las asignaturas, algunos en varias
universidad.matricularEstudianteAsignatura("Laura Martínez", "34567890D", "Matemáticas")
universidad.matricularEstudianteAsignatura("David Martínez", "66666666U", "Física")
universidad.matricularEstudianteAsignatura("David Martínez", "66666666U", "Matemáticas")
universidad.matricularEstudianteAsignatura("Lucía Pérez", "77777777T", "Programación Avanzada")
universidad.matricularEstudianteAsignatura("Lucía Pérez", "77777777T", "Matemáticas")
universidad.matricularEstudianteAsignatura("Javier Rodríguez", "88888888S", "Física")
universidad.matricularEstudianteAsignatura("Javier Rodríguez", "88888888S", "Bases de Datos")
universidad.matricularEstudianteAsignatura("Marina Sánchez", "99999999R", "Programación Avanzada")
universidad.matricularEstudianteAsignatura("Marina Sánchez", "99999999R", "Física")

# Listamos personas
universidad.listadoInvestigadores() #como podemos observar aqui aparecen tanto los miembros de departamento que son solo investigadores como los profesores titulares que investigan
universidad.listadoProfesores()
universidad.listadoEstudiantes()

#Listamos la informacion de las asignaturas
universidad.listadoInformacionAsignatura("Matemáticas")
universidad.listadoInformacionAsignatura("Física")
universidad.listadoInformacionAsignatura("Programación Avanzada")

# Listamos los miembros de los distintos departamentos
universidad.listadoMiembrosDepartamento(TipoDepartamento.DIIC)
universidad.listadoMiembrosDepartamento(TipoDepartamento.DIS)
universidad.listadoMiembrosDepartamento(TipoDepartamento.DITEC)

#Observamos que todos los listados se muestran bien con toda la informacion requerida
#Ahora hacemos otras pruebas

#Borramos profesor
universidad.borrarProfesor("Elena Vázquez", "33333333Z")

#Borramos alumno
universidad.borrarEstudiante("Marina Sánchez", "99999999R")
universidad.borrarEstudiante("Laura Martínez", "34567890D")

#Borramos a un alumno de una asignatura
universidad.borrarEstudianteAsignatura("David Martínez", "66666666U", "Matemáticas")

#Borramos investigador
universidad.borrarInvestigador("Sara López", "55555555V")

#Cambiamos miembros de departamento de departamento
universidad.cambiarDepartamentoMiembro("Juan Pérez", "12345678A", TipoDepartamento.DIS)
universidad.cambiarDepartamentoMiembro("Carlos Ruiz", "22222222Y", TipoDepartamento.DIIC)

#Volvemos a mostrar los listados para ver que los cambios se han efectuado correctamente

# Listamos personas
universidad.listadoInvestigadores()
universidad.listadoProfesores()
universidad.listadoEstudiantes()

#Listamos la informacion de las asignaturas
universidad.listadoInformacionAsignatura("Matemáticas")
universidad.listadoInformacionAsignatura("Física")
universidad.listadoInformacionAsignatura("Programación Avanzada")
universidad.listadoInformacionAsignatura("Bases de Datos")

# Listamos los miembros de los distintos departamentos
universidad.listadoMiembrosDepartamento(TipoDepartamento.DIIC)
universidad.listadoMiembrosDepartamento(TipoDepartamento.DIS)
universidad.listadoMiembrosDepartamento(TipoDepartamento.DITEC)

#Observamos que en los listados de estudiantes como de informacion de asignaturas ya no aparecen las estudiantes "Marina Sánchez" y "Laura Martinez"
#Observamos que en los listados de profesores como de informacion de asignaturas ya no aparece la profesora "Elena Vázquez"
#Observamos que en los listados de investigadores ya no aparece la investigadora "Sara López"
#Observamos que cuando volvemos a listar los miembros de departamento de los diferentes departamentos "Juan Pérez" y "Carlos Ruiz" aparecen con sus departamentos cambiados, cuando listamos los profesores, tambien vemos que su informacion aparece cambiada
#Observamos que el estudiante "David Martínez" ya no aparece matriculado en la asignatura de "Matemáticas" ya que hemos borrado su asignatura, no aparece esta ni en el listado de estudiantes ni cuando mostramos la informacion de la asignatura de matemáticas