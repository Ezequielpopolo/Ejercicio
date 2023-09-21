from materia import Materia
class MateriaManager:
    def __innit__(self):
        self.datos_materias = []
    def agregar_materia(self):
        nombre = input("Ingresa tu nombre: ")
        profesor = input("Ingresa el profesor: ")
        horario = int(input("Ingresa el horario: "))
        materia = Materia(nombre,profesor,horario)
        self.datos_materias.append(materia)
        print("Persona agregada correctamente")
        
    def mostrar_materias(self):
        print("Indice Nombre Materia Horario")
        for index, materia in enumerate(self.datos_materias):
            print(f"{index}\t{materia.nombre}\t{materia.profesor}\t{materia.horario}")
            
    def eliminar(self):
        self.mostrar_materias()
        eliminar = int(input("Ingrese el índice de la tupla que desea eliminar: "))
        if 0 <= eliminar < len(self.datos_materias):
                self.datos_materias.pop(eliminar)
        else:
            print("Índice no válido. No se ha eliminado ninguna materia.")
        print("Datos eliminados correctamente") 
        return self.datos_materias
    
    def modificar(self):
        self.mostrar_materias()
        modificar = int(input("Ingrese el índice de la tupla que desea modificar: "))
        if 0 <= modificar < len(self.mostrar_materias):    
            materia = self.mostrar_materias[modificar]
            nombre_modificado = input("Ingresa tu nombre: ")           
            profesor_modificado = input("Ingresa tu apellido: ") 
            horario_modificada = int(input("Ingresa tu edad: "))
            materia.nombre = nombre_modificado
            materia.horario = profesor_modificado
            materia.edad = horario_modificada
        print("Datos modificados correctamente")
        return self.datos_materias