from person_manager import PersonManager
from materia_manager import MateriaManager

    
manager = PersonManager()
materia = MateriaManager()
while True:
    pregunta = input("""
1- Agregar persona 
2- Mostrar personas
3- Eliminar personas
4- Modificar personas
5- Agregar datos a excel
6- Cargar archivo
7- Obtener estadisticas
8- Agregar Materias
9- Mostrar Materias
10- Eliminar Materias
11- Modificar Materias
12- Salir
Elija una opción: """).lower()
        
    if pregunta == "1":
        manager.agregar_persona()
                   
    elif pregunta == "2":
        manager.mostrar_datos()
        
    elif pregunta == "3":
        manager.eliminar()
        
    elif pregunta == "4":
        manager.modificar()
        
    elif pregunta == "5":
        manager.agregar_excel()
        
    elif pregunta == "6":
        datos_personas = manager.cargar_excel()
    
    elif pregunta == "7":
        manager.obtener_estadisticas()
    
    elif pregunta == "8":
        materia.agregar_materia()
        
    elif pregunta == "9":
        materia.mostrar_materias()
        
    elif pregunta == "10":
        materia.eliminar()
        
    elif pregunta == "11":
        materia.modificar()
        
    elif pregunta == "12":
        print("El programa terminó")
        break
    else:
        print("Opción incorrecta, elija una opción correcta: ")


