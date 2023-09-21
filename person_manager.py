from persona import Persona
import pandas as pd
import numpy as np
class PersonManager:
    def __init__(self):   
     self.datos_personas = []
    
    def agregar_persona(self):
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        edad = int(input("Ingresa tu edad: "))
        sexo = input("Ingrese sexo F/M: ")
        persona = Persona(nombre, apellido, edad, sexo)
        self.datos_personas.append(persona)
        print("Persona agregada correctamente")
    
    def mostrar_datos(self):
        print("Indice Nombre Apellido Edad Sexo")
        for index, persona in enumerate(self.datos_personas):
            print(f"{index}\t{persona.nombre}\t{persona.apellido}\t{persona.edad}\t{persona.sexo}")

    
    def eliminar(self):
        self.mostrar_datos()
        eliminar = int(input("Ingrese el índice de la tupla que desea eliminar: "))
        if 0 <= eliminar < len(self.datos_personas):
                self.datos_personas.pop(eliminar)
        else:
            print("Índice no válido. No se ha eliminado ninguna persona.")
        print("Datos eliminados correctamente") 
        return self.datos_personas
    
    def modificar(self):
        self.mostrar_datos()
        modificar = int(input("Ingrese el índice de la tupla que desea modificar: "))
        if 0 <= modificar < len(self.datos_personas):    
            persona = self.datos_personas[modificar]
            nombre_modificado = input("Ingresa tu nombre: ")           
            apellido_modificado = input("Ingresa tu apellido: ") 
            edad_modificada = int(input("Ingresa tu edad: "))
            sexo_modificado = input("Ingrese el sexo: ")
            persona.nombre = nombre_modificado
            persona.apellido = apellido_modificado
            persona.edad = edad_modificada
            persona.sexo = sexo_modificado
        print("Datos modificados correctamente")
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
