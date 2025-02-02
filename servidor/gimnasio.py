import re
import mysql.connector

from connection import conn, cursor
from servicios import mostrar_servicios, verificar_id_servicio



def verificar_id_profesor(id_profesor):
    # Verificar si el id_profesor existe en la base de datos
    if conn:
        cursor.execute("SELECT COUNT(*) FROM Profesor WHERE Id_profesor = %s", (id_profesor,))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        return resultado[0] > 0  # Devuelve True si el profesor existe
    return False

def validar_email(email):
    # Utilizando una expresión regular para validar el formato del correo electrónico
    patron_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron_email, email) is not None

def new_profesor():
    dni = input("Ingrese el dni del profesor: ")
    while not dni or int(dni) <= 0:
        print("El dni no puede estar vacío.")
        dni = input("Ingrese el dni del profesor: ")
    
    nombre = input("Ingrese el nombre del profesor: ")
    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese el nombre del profesor: ")

    apellido = input("Ingrese el apellido del profesor: ")
    while not apellido:
        print("El apellido no puede estar vacío.")
        apellido = input("Ingrese el apellido del profesor: ")

    email = input("Ingrese el correo electrónico del profesor: ")
    while not validar_email(email):
        print("El correo electrónico no es válido. Por favor, ingrese un correo electrónico válido.")
        email = input("Ingrese el correo electrónico del profesor: ") 



    # Mostrar los datos antes de confirmar
    print("\nDatos del nuevo profesor a agregar:")
    print(f"Dni: {dni}")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Email: {email}")

    
    # Confirmar si desea agregar el nuevo profesor
    confirmar = input("\n¿Desea agregar este profesor? (sí/no): ").strip().lower()
    
    if confirmar == 'sí' or confirmar == 'si':
        print("\nProfesor agregado correctamente.")
        try:
            # Consulta para insertar los datos
            cursor.execute("INSERT INTO Persona (dni, nombre, apellido, email, clave, tipo) VALUES (%s, %s, %s, %s, %s, %s)", (dni, nombre, apellido, email, '1232456', "P"))
            cursor.execute("INSERT INTO Profesor (dni, cargo) VALUES (%s, %s)", (dni, "JEFE"))
            # Confirmar la inserción
            conn.commit()
            print("Persona agregada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al insertar datos: {err}")
        
        return dni
    else:
        print("\nOperación cancelada. El profesor no ha sido agregado.")
        return None

def new_gym():
    nombre = input("Ingrese el nombre del gimnasio: ")
    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese el nombre del gimnasio: ")

    descripcion = input("Ingrese la descripción del gimnasio: ")
    while not descripcion:
        print("La descripción no puede estar vacía.")
        descripcion = input("Ingrese la descripción del gimnasio: ")

    mostrar_servicios()
    id_servicio = input("Seleccione el ID del servicio: ")
    while not id_servicio.isdigit() or not verificar_id_servicio(id_servicio):
        print("El ID del servicio no es válido o no existe. Por favor, ingrese un ID de servicio válido.")
        id_servicio = input("Ingrese el ID del servicio: ")

    print("\nDatos del gimnasio a agregar:")
    print(f"Nombre: {nombre}")
    print(f"Descripción: {descripcion}")
    print(f"Servicio nro: {id_servicio}")
    
    # Confirmar si desea agregar el gimnasio
    confirmar = input("\n¿Desea agregar este gimnasio? (sí/no): ").strip().lower()
     
    if confirmar == 'sí' or confirmar == 'si':
        print("Registre el profesor a cargo: ")
        profesor_a_cargo = seleccionar_profesor()
        if profesor_a_cargo:
            try:
                cursor.execute("INSERT INTO Gimnasio (nombre, descripcion, Id_servicio, profesor_a_cargo) VALUES (%s, %s, %s, %s)", (nombre, descripcion, id_servicio, profesor_a_cargo))
                conn.commit()
                print("Gimnasio agregado exitosamente.")
            except mysql.connector.Error as err:
                print(f"Error al insertar datos: {err}")
        else:
            print("\nGimnasio no fue agregado porque no se agregó un profesor.")
    else:
        print("\nOperación cancelada. El gimnasio no ha sido agregado.")
        
def eliminar_gimnasio(id):
    confirmar = input(f"\n¿SEGURO QUE DESEAS ELIMINAR EL GIMNACIO CON ID: {id}? (sí/no): ").strip().lower() 
    if (confirmar == 'sí' or confirmar == 'si') and verificar_id_gimnasio(id):
        cursor.execute("DELETE FROM Gimnasio WHERE id_gimnasio = %s", (id))

def modificar_gimnasio(gimnasios):
    mostrar_gimnasios()
    id_gimnasio = input("Ingrese el ID del gimnasio a modificar: ")
    if id_gimnasio in gimnasios:
        gimnasio = new_gym()
        gimnasios[id_gimnasio] = gimnasio
        print("Gimnasio modificado exitosamente.")
    else:
        print("Gimnasio no encontrado.")

def mostrar_gimnasios():
    if conn:
        cursor.execute("SELECT * FROM Gimnasio")
        
        resultados = cursor.fetchall()

        # Mostrar los resultados
        for fila in resultados:
            print('ID:',fila[0],', Nombre: $',fila[1],', Descripcion:',fila[2], ', id servicio:',fila[3], ', id profesor:',fila[4])

    else:
        print("No se pudo establecer la conexión.")

def verificar_id_gimnasio(id):
    if conn:
        cursor.execute("SELECT COUNT(*) FROM Gimnasio WHERE Id_servicio = %s", (id))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        return resultado[0] > 0  # Devuelve True si el servicio existe
    return False

def seleccionar_profesor():
    if cursor:
        cursor.execute("SELECT * FROM ver_profesor")
        resultados = cursor.fetchall()
        
        if len(resultados) > 0:
            for fila in resultados:
                print('ID:',fila[0],', Nombre: $',fila[1],', Cargo: $',fila[2])

            confirmacion = input("¿Quieres seleccionar un profesor existente?(si/no): ")
            if confirmacion == "sí" or confirmacion == "si":
                id_alumno = input("quiere el ID del servicio: ")
            
                while not id_alumno.isdigit() or not verificar_id_profesor(id_alumno):
                    print("El ID del profesor no es válido o no existe. Por favor, ingrese un ID de profesor válido.")
                    id_alumno = input("Ingrese el ID del profesor: ")
            
                return id_alumno
        
    return new_profesor()
