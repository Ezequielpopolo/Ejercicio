from persona import Persona
from materia import Materia
import pandas as pd
import numpy as np
class PersonManager:
    def __init__(self):   
     self.datos_personas = []
     self.datos_materias = []
     self.materias_inscritas = []
     self.contador_id = 0
     
    def agregar_persona(self):
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        edad = input("Ingresa tu edad: ")
        sexo = input("Ingresa tu sexo F/M")
        id = self.contador_id
        self.contador_id +=1
        persona = Persona(id,nombre,apellido,edad,sexo)
        self.datos_personas.append(persona)
        print("Persona agregada correctamente")

    def mostrar_datos(self):
        print("ID Nombre Apellido Edad Sexo")
        for persona in self.datos_personas:
            print(f"{persona.id}\t{persona.nombre}\t{persona.apellido}\t{persona.edad}\t{persona.sexo}")

    
    def eliminar(self):
        self.mostrar_datos()
        eliminar_id = int(input("Ingrese el ID de la persona que desea eliminar: "))
        
        materia_a_eliminar = None
        for materia in self.datos_personas:
            if materia.id == eliminar_id:
                materia_a_eliminar = materia
                break

        if materia_a_eliminar is not None:
            self.datos_personas.remove(materia_a_eliminar)
            print("Persona eliminada correctamente.")
        else:
            print("ID no válido. No se ha eliminado ninguna persona.")
        return self.datos_personas
    
    def modificar(self):
        self.mostrar_datos()
        modificar_id = int(input("Ingrese el ID de la materia que desea modificar: "))
        
        if 0 <= modificar_id < len(self.datos_personas):    
            materia = self.datos_personas[modificar_id]
            nombre_modificado = input("Ingresa el nuevo nombre: ")   
            apellido_modificado = input("Ingrese su apellido")        
            edad_modificada = input("Ingresa su edad: ") 
            sexo_modificado = input("Ingrese su sexo F/M")

            materia.nombre = nombre_modificado
            materia.apellido = apellido_modificado
            materia.edad = edad_modificada
            materia.sexo = sexo_modificado

            print("Datos modificados correctamente")
        else:
            print("ID no válido. No se realizaron modificaciones.")

        return self.datos_personas
       
    def agregar_excel(self):
        df = pd.DataFrame([vars(persona) for persona in self.datos_personas])
        archivo_excel = "datos.xlsx"
        df.to_excel(archivo_excel, index=False)
        print("Datos agregados correctamente")
    
    def cargar_excel(self):

        archivo = pd.read_excel("datos.xlsx")
        self.datos_personas = [Persona(row['nombre'], row['apellido'], row['edad'], row['sexo']) for _, row in archivo.iterrows()]
        print("Datos cargados correctamente desde Excel")
        return self.datos_personas


   
    def obtener_estadisticas(self):
        cantidad_personas = len(self.datos_personas)
        cantidad_mujeres = sum(1 for persona in self.datos_personas if persona.sexo.lower() == "f")
        cantidad_hombres = cantidad_personas - cantidad_mujeres

        print(f"Hay un total de: {cantidad_personas} personas")
        print(f"Hay un total de: {cantidad_hombres} hombres")
        print(f"Hay un total de: {cantidad_mujeres} mujeres")

        persona_mas_joven = min(self.datos_personas, key=lambda x: x.edad)
        print(f"La persona más joven es: {persona_mas_joven.nombre} {persona_mas_joven.apellido} con {persona_mas_joven.edad} años.")
        
        persona_mas_vieja = max(self.datos_personas, key=lambda x: x.edad)
        print(f"La persona más vieja es: {persona_mas_vieja.nombre} {persona_mas_vieja.apellido} con {persona_mas_vieja.edad} años.")
        

    def agregar_materia(self):
        nombre = input("Ingresa tu nombre: ")
        profesor = input("Ingresa el profesor: ")
        horario = (input("Ingresa el horario: "))
        
        id = self.contador_id
        self.contador_id +=1
        materia = Materia(id,nombre,profesor,horario)
        self.datos_materias.append(materia)
        print(self.datos_materias)
        print("Materia agregada correctamente")
    
    def mostrar_materias(self):
        print("ID Nombre Materia Horario")
        for materia in self.datos_materias:
            print(f"{materia.id}\t{materia.nombre}\t{materia.profesor}\t{materia.horario}")
            
    def eliminar_materia(self):
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
    
    def modificar_materia(self):
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
      
    def inscribir(self):
        for persona in self.alumno.datos_personas:
            print(f"{persona.id}\t{persona.nombre}\t{persona.apellido}\t{persona.edad}\t{persona.sexo}")
        id_alumno = input("Ingrese el id del alumno que desea inscribir: ")
        
        for materia in self.materia_manager.datos_materias:
            print(f"{materia.id}\t{materia.nombre}\t{materia.profesor}\t{materia.horario}")
        id_materia = int(input("Ingrese el id de la materia que quiere inscribir al alumno: "))

        alumno_encontrado = next((alumno for alumno in self.manager.datos_personas if alumno.id == id_alumno), None)
        materia_encontrada = next((materia for materia in self.materia_manager.datos_materias if materia.id == id_materia), None)
        print(alumno_encontrado)
        print(materia_encontrada)
        
        if alumno_encontrado is not None and materia_encontrada is not None:
            self.materias_inscritas.append(materia_encontrada)
            print(f"Alumno {alumno_encontrado.nombre} inscrito en la materia {materia_encontrada.nombre}.")
        else:
            print("ID de alumno o materia no válido. No se realizó la inscripción.")
