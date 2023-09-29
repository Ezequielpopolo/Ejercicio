from materia import Materia
class MateriaManager:
    def __init__(self):
        self.datos_materias = []
        self.contador_id = 0
    def agregar_materia(self):
        nombre = input("Ingresa tu nombre: ")
        profesor = input("Ingresa el profesor: ")
        horario = (input("Ingresa el horario: "))
        
        id = self.contador_id
        self.contador_id +=1
        materia = Materia(id,nombre,profesor,horario)
        self.datos_materias.append(materia)
        print("Materia agregada correctamente")
    
    def mostrar_materias(self):
        print("ID Nombre Materia Horario")
        for materia in self.datos_materias:
            print(f"{materia.id}\t{materia.nombre}\t{materia.profesor}\t{materia.horario}")
            
    def eliminar(self):
        self.mostrar_materias()
        eliminar_id = int(input("Ingrese el ID de la materia que desea eliminar: "))
        
        materia_a_eliminar = None
        for materia in self.datos_materias:
            if materia.id == eliminar_id:
                materia_a_eliminar = materia
                break

        if materia_a_eliminar is not None:
            self.datos_materias.remove(materia_a_eliminar)
            print("Materia eliminada correctamente.")
        else:
            print("ID no válido. No se ha eliminado ninguna materia.")
        return self.datos_materias
    
    def modificar(self):
        self.mostrar_materias()
        modificar_id = int(input("Ingrese el ID de la materia que desea modificar: "))
        
        if 0 <= modificar_id < len(self.datos_materias):    
            materia = self.datos_materias[modificar_id]
            nombre_modificado = input("Ingresa el nuevo nombre: ")           
            profesor_modificado = input("Ingresa el nuevo profesor: ") 
            horario_modificado = input("Ingresa el nuevo horario: ")

            materia.nombre = nombre_modificado
            materia.profesor = profesor_modificado
            materia.horario = horario_modificado

            print("Datos modificados correctamente")
        else:
            print("ID no válido. No se realizaron modificaciones.")

        return self.datos_materias