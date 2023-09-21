class Materia:
    def __self__(self,nombre,profesor,horario):
        self.nombre = nombre
        self.profesor = profesor
        self.horario = horario
    def __str__(self):
        return f"{self.nombre} {self.profesor}, {self.horario}"
    