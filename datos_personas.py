from person_manager import PersonManager, Persona
from materia_manager import MateriaManager, Materia

class Alumno(PersonManager):
    def __init__(self, legajo):
        super().__init__()
        self.legajo = legajo

class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, sexo, cuil):
        super().__init__(nombre, apellido, edad, sexo)
        self.cuil = cuil

class AlumnoMateria:
    def __init__(self, alumno, materia_manager):
        self.alumno = alumno
        self.materia_manager = materia_manager
        self.materias_inscritas = []

    def inscribir(self):
        for persona in self.alumno.datos_personas:
            print(f"{persona.id}\t{persona.nombre}\t{persona.apellido}\t{persona.edad}\t{persona.sexo}")
        id_alumno = input("Ingrese el id del alumno que desea inscribir: ")
        
        for materia in self.materia_manager.datos_materias:
            print(f"{materia.id}\t{materia.nombre}\t{materia.profesor}\t{materia.horario}")
        id_alumno = int(input("Ingrese el id del alumno que desea inscribir: "))
        id_materia = int(input("Ingrese el id de la materia que quiere inscribir al alumno: "))

        alumno_encontrado = next((alumno for alumno in self.alumno.datos_personas if alumno.id == id_alumno), None)
        materia_encontrada = next((materia for materia in self.materia_manager.datos_materias if materia.id == id_materia), None)

        
        if alumno_encontrado is not None and materia_encontrada is not None:
            self.materias_inscritas.append(materia_encontrada)
            print(f"Alumno {alumno_encontrado.nombre} inscrito en la materia {materia_encontrada.nombre}.")
        else:
            print("ID de alumno o materia no válido. No se realizó la inscripción.")
manager = PersonManager()
materia = MateriaManager()
alumno_materia = AlumnoMateria(manager, materia)
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
        materia.agregar_materia()
        
    elif pregunta == "9":
        materia.mostrar_materias()
        
    elif pregunta == "10":
        materia.eliminar()
        
    elif pregunta == "11":
        materia.modificar()
    elif pregunta == "12":
        alumno_materia.inscribir()
    elif pregunta == "13":
        print("El programa terminó")
        break
    else:
        print("Opción incorrecta, elija una opción correcta: ")


