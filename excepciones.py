#GESTION DE EXCEPCIONES

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