class Materia:
    def __init__(self,id,nombre,profesor,horario):
        self.id = id
        self.nombre = nombre
        self.profesor = profesor
        self.horario = horario
    def __str__(self):
        return f"{self.id},{self.nombre} {self.profesor}, {self.horario}"
