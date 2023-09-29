class Persona:
    def __init__(self,nombre,apellido,edad,sexo,id):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.id = id
    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.edad} años, Sexo: {self.sexo}"