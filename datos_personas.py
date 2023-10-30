from person_manager import PersonManager, Persona

class Alumno(PersonManager):
    def __init__(self, legajo):
        super().__init__()
        self.legajo = legajo

class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, sexo, cuil):
        super().__init__(nombre, apellido, edad, sexo)
        self.cuil = cuil

class AlumnoMateria:
    def __init__(self, alumno):
        self.alumno = alumno

manager = PersonManager()
alumno_materia = AlumnoMateria(manager)
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
12- Inscribir alumno a materia
13- Salir
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
        manager.agregar_materia()
        
    elif pregunta == "9":
        manager.mostrar_materias()
        
    elif pregunta == "10":
        manager.eliminar_materia()
        
    elif pregunta == "11":
        manager.modificar_materia()
    elif pregunta == "12":
        alumno_materia.inscribir()
    elif pregunta == "13":
        print("El programa terminó")
        break
    else:
        print("Opción incorrecta, elija una opción correcta: ")


