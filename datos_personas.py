import pandas as pd
import numpy as np

class Persona:
    def __init__(self,nombre,apellido,edad,sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.edad} años, Sexo: {self.sexo}"
    
class PersonManager:    
    datos_personas = []      
    @staticmethod
    def agregar_persona():
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        edad = int(input("Ingresa tu edad: "))
        sexo = input("Ingrese sexo F/M: ")
        persona = Persona(nombre, apellido, edad, sexo)
        PersonManager.datos_personas.append(persona)
        print("Persona agregada correctamente")
    @staticmethod
    def mostrar_datos():
        print("Indice Nombre Apellido Edad Sexo")
        for index, persona in enumerate(PersonManager.datos_personas):
            print(f"{index}\t{persona.nombre}\t{persona.apellido}\t{persona.edad}\t{persona.sexo}")

    @staticmethod
    def eliminar():
        PersonManager.mostrar_datos()
        eliminar = int(input("Ingrese el índice de la tupla que desea eliminar: "))
        if 0 <= eliminar < len(PersonManager.datos_personas):
                PersonManager.datos_personas.pop(eliminar)
        else:
            print("Índice no válido. No se ha eliminado ninguna persona.")
        print("Datos eliminados correctamente") 
        return PersonManager.datos_personas
    @staticmethod
    def modificar():
        PersonManager.mostrar_datos()
        modificar = int(input("Ingrese el índice de la tupla que desea modificar: "))
        if 0 <= modificar < len(PersonManager.datos_personas):    
            persona = PersonManager.datos_personas[modificar]
            nombre_modificado = input("Ingresa tu nombre: ")           
            apellido_modificado = input("Ingresa tu apellido: ") 
            edad_modificada = int(input("Ingresa tu edad: "))
            sexo_modificado = input("Ingrese el sexo: ")
            persona.nombre = nombre_modificado
            persona.apellido = apellido_modificado
            persona.edad = edad_modificada
            persona.sexo = sexo_modificado
        print("Datos modificados correctamente")
        return PersonManager.datos_personas
    @staticmethod    
    def agregar_excel():
        df = pd.DataFrame([vars(persona) for persona in PersonManager.datos_personas])
        archivo_excel = "datos.xlsx"
        df.to_excel(archivo_excel, index=False)
        print("Datos agregados correctamente")
    @staticmethod
    def cargar_excel():

        archivo = pd.read_excel("datos.xlsx")
        PersonManager.datos_personas = [Persona(row['nombre'], row['apellido'], row['edad'], row['sexo']) for _, row in archivo.iterrows()]
        print("Datos cargados correctamente desde Excel")
        return PersonManager.datos_personas


    @staticmethod
    def obtener_estadisticas():
        cantidad_personas = len(PersonManager.datos_personas)
        cantidad_mujeres = sum(1 for persona in PersonManager.datos_personas if persona.sexo.lower() == "f")
        cantidad_hombres = cantidad_personas - cantidad_mujeres

        print(f"Hay un total de: {cantidad_personas} personas")
        print(f"Hay un total de: {cantidad_hombres} hombres")
        print(f"Hay un total de: {cantidad_mujeres} mujeres")

        persona_mas_joven = min(PersonManager.datos_personas, key=lambda x: x.edad)
        print(f"La persona más joven es: {persona_mas_joven.nombre} {persona_mas_joven.apellido} con {persona_mas_joven.edad} años.")
        
        persona_mas_vieja = max(PersonManager.datos_personas, key=lambda x: x.edad)
        print(f"La persona más vieja es: {persona_mas_vieja.nombre} {persona_mas_vieja.apellido} con {persona_mas_vieja.edad} años.")

while True:
    pregunta = input("""
1- Agregar persona 
2- Mostrar personas
3- Eliminar personas
4- Modificar personas
5- Agregar datos a excel
6- Cargar archivo
7- Obtener estadisticas
8- Salir
Elija una opción: """).lower()
        
    if pregunta == "1":
        PersonManager.agregar_persona()
                   
    elif pregunta == "2":
        PersonManager.mostrar_datos()
        
    elif pregunta == "3":
        PersonManager.eliminar()
        
    elif pregunta == "4":
        PersonManager.modificar()
        
    elif pregunta == "5":
        PersonManager.agregar_excel()
        
    elif pregunta == "6":
        datos_personas = PersonManager.cargar_excel()
    
    elif pregunta == "7":
        PersonManager.obtener_estadisticas()
    elif pregunta == "8":
        print("El programa terminó")
        break
    else:
        print("Opción incorrecta, elija una opción correcta: ")


