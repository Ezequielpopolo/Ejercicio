import pandas as pd
import numpy as np
datos_personas = []
def agregar():    
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = int(input("Ingresa tu edad: "))
    datos_personas.append([nombre,apellido,edad])
    print("Datos agregados correctamente")
    return datos_personas

def eliminar():
    for index, persona in enumerate(datos_personas):
            print(f"{index} {persona}")
    eliminar = int(input("Ingrese el índice de la tupla que desea eliminar: "))
    if 0 <= eliminar < len(datos_personas):
            datos_personas.pop(eliminar)
    else:
        print("Índice no válido. No se ha eliminado ninguna persona.")
    print("Datos eliminados correctamente") 
    return datos_personas

def modificar():
    for index, persona in enumerate(datos_personas):
            print(f"{index} {persona}")
    modificar = int(input("Ingrese el índice de la tupla que desea modificar: "))
    for i, p in enumerate(persona):
        print(f"{i} {p}")
    if 0 <= modificar < len(datos_personas):    
        nombre_modificado = input("Ingresa tu nombre: ")           
        apellido_modificado = input("Ingresa tu apellido: ") 
        edad_modificada = int(input("Ingresa tu edad: "))
        persona[0] = nombre_modificado
        persona[1] = apellido_modificado
        persona[2] = edad_modificada
    print("Datos modificados correctamente")
    return datos_personas

def agregar_excel():
    df = pd.DataFrame(datos_personas,columns=["Nombre","Apellido","Edad"])
    archivo_excel = "ejercicio_datos\\datos.xlsx"
    df.to_excel(archivo_excel, index=False)
    print("Datos agregados correctamente")
    return datos_personas

def cargar_excel():
    archivo = pd.read_excel("ejercicio_datos\\datos.xlsx")
    datos_personas = archivo.to_numpy().tolist()
    print("Datos cargados correctamente")
    return datos_personas
        
while True:
    pregunta = input("""
1- Agregar persona 
2- Mostrar personas
3- Eliminar personas
4- Modificar personas
5- Agregar datos a excel
6- Cargar archivo
7- Salir
Elija una opción: """).lower()
        
    if pregunta == "1":
        agregar()
            
    elif pregunta == "2":
        print(datos_personas)
        
    elif pregunta == "3":
        eliminar()
        
    elif pregunta == "4":
        modificar()
        
    elif pregunta == "5":
        agregar_excel()
        
    elif pregunta == "6":
        datos_personas = cargar_excel()
    
    elif pregunta == "7":
        print("El programa terminó")
        break
    else:
        print("Opción incorrecta, elija una opción correcta: ")


