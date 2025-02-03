import re
import mysql.connector

from connection import conn, cursor, Abrir_conexion
from servicios import mostrar_servicios, verificar_id_servicio

COLOR_HEADER = "\033[95m"
COLOR_BLUE = "\033[94m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"

conn = Abrir_conexion()
if conn:
    cursor = conn.cursor()

def verificar_id_profesor(id_profesor):
    # Verificar si el id_profesor existe en la base de datos
    if conn:
        cursor.execute("SELECT COUNT(*) FROM Profesor WHERE dni = %s", (id_profesor,))
        resultado = cursor.fetchone()
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
        
def eliminar_gimnasio(id_gimnasio):
    try:
        if not verificar_id_gimnasio(id_gimnasio):
            print(f"{COLOR_RED}❌ El ID {id_gimnasio} no existe en la base de datos.{COLOR_RESET}")
            return

        confirmar = input(f"⚠️ ¿SEGURO QUE DESEAS ELIMINAR EL GIMNASIO CON ID: {id_gimnasio}? (sí/no): ").strip().lower()
        
        if confirmar in ['sí', 'si']:
            cursor.execute("DELETE FROM Gimnasio WHERE id_gimnasio = %s", (id_gimnasio,))
            conn.commit()  # Confirmar los cambios en la base de datos
            print(f"{COLOR_RED}✅ Gimnasio con ID {id_gimnasio} eliminado exitosamente.{COLOR_RESET}")
        else:
            print(f"{COLOR_YELLOW}❗ Operación cancelada por el usuario.{COLOR_RESET}")

    except mysql.connector.Error as err:
        print(f"{COLOR_RED}⚠️ Error al eliminar el gimnasio: {err}{COLOR_RESET}")
    except Exception as e:
        print(f"{COLOR_RED}⚠️ Error inesperado: {e}{COLOR_RESET}")

def modificar_gimnasio():
    try:
        mostrar_gimnasios()
        id_gimnasio = input("Ingrese el ID del gimnasio a modificar: ").strip()

        # Verificar si el gimnasio existe
        if not verificar_id_gimnasio(id_gimnasio):
            print(f"{COLOR_RED}❌ El gimnasio con ID {id_gimnasio} no existe.{COLOR_RESET}")
            return

        # Obtener datos actuales del gimnasio
        cursor.execute("SELECT nombre, descripcion, Id_servicio, profesor_a_cargo FROM Gimnasio WHERE id_gimnasio = %s", (id_gimnasio,))
        gimnasio_actual = cursor.fetchone()

        if gimnasio_actual:
            print("\nDatos actuales del gimnasio:")
            print(f"1️⃣ Nombre: {gimnasio_actual[0]}")
            print(f"2️⃣ Descripción: {gimnasio_actual[1]}")
            print(f"3️⃣ ID del Servicio: {gimnasio_actual[2]}")
            print(f"4️⃣ Profesor a Cargo: {gimnasio_actual[3]}")

            # Actualización de nombre
            actualizar_nombre = input("\n¿Desea actualizar el nombre? (sí/no): ").strip().lower()
            if actualizar_nombre in ['sí', 'si']:
                nuevo_nombre = input("Ingrese el nuevo nombre del gimnasio: ").strip()
                while not nuevo_nombre:
                    print("❗ El nombre no puede estar vacío.")
                    nuevo_nombre = input("Ingrese el nuevo nombre del gimnasio: ")
            else:
                nuevo_nombre = gimnasio_actual[0]

            # Actualización de descripción
            actualizar_descripcion = input("\n¿Desea actualizar la descripción? (sí/no): ").strip().lower()
            if actualizar_descripcion in ['sí', 'si']:
                nueva_descripcion = input("Ingrese la nueva descripción del gimnasio: ").strip()
                while not nueva_descripcion:
                    print("❗ La descripción no puede estar vacía.")
                    nueva_descripcion = input("Ingrese la nueva descripción del gimnasio: ")
            else:
                nueva_descripcion = gimnasio_actual[1]

            # Actualización del servicio
            actualizar_servicio = input("\n¿Desea actualizar el servicio? (sí/no): ").strip().lower()
            if actualizar_servicio in ['sí', 'si']:
                mostrar_servicios()
                nuevo_id_servicio = input("Seleccione el nuevo ID del servicio: ").strip()
                while not nuevo_id_servicio.isdigit() or not verificar_id_servicio(nuevo_id_servicio):
                    print("❗ El ID del servicio no es válido o no existe.")
                    nuevo_id_servicio = input("Ingrese un ID de servicio válido: ")
            else:
                nuevo_id_servicio = gimnasio_actual[2]

            # Actualización del profesor a cargo
            actualizar_profesor = input("\n¿Desea actualizar el profesor a cargo? (sí/no): ").strip().lower()
            if actualizar_profesor in ['sí', 'si']:
                nuevo_profesor_a_cargo = seleccionar_profesor()
            else:
                nuevo_profesor_a_cargo = gimnasio_actual[3]

            # Confirmar cambios
            print("\nDatos actualizados del gimnasio:")
            print(f"✅ Nombre: {nuevo_nombre}")
            print(f"✅ Descripción: {nueva_descripcion}")
            print(f"✅ ID del Servicio: {nuevo_id_servicio}")
            print(f"✅ Profesor a Cargo: {nuevo_profesor_a_cargo}")

            confirmar = input("\n¿Desea guardar los cambios? (sí/no): ").strip().lower()
            if confirmar in ['sí', 'si']:
                cursor.execute("""
                    UPDATE Gimnasio 
                    SET nombre = %s, descripcion = %s, Id_servicio = %s, profesor_a_cargo = %s
                    WHERE id_gimnasio = %s
                """, (nuevo_nombre, nueva_descripcion, nuevo_id_servicio, nuevo_profesor_a_cargo, id_gimnasio))

                conn.commit()  # Guardar cambios
                print(f"{COLOR_GREEN}✅ Gimnasio modificado exitosamente.{COLOR_RESET}")
            else:
                print(f"{COLOR_YELLOW}❗ Modificación cancelada. No se realizaron cambios.{COLOR_RESET}")
        else:
            print(f"{COLOR_RED}❌ No se pudo obtener la información del gimnasio.{COLOR_RESET}")

    except mysql.connector.Error as err:
        print(f"{COLOR_RED}⚠️ Error al modificar el gimnasio: {err}{COLOR_RESET}")
    except Exception as e:
        print(f"{COLOR_RED}⚠️ Error inesperado: {e}{COLOR_RESET}")

def mostrar_gimnasios():
    if conn:
        cursor.execute("SELECT * FROM Gimnasio")
        
        resultados = cursor.fetchall()

        # Mostrar los resultados
        for fila in resultados:
            print('ID:',fila[0],'\nNombre:',fila[1],'\nDescripcion:',fila[2], '\nid servicio:',fila[3], '\nid profesor:',fila[4],'\n')

    else:
        print("No se pudo establecer la conexión.")

def verificar_id_gimnasio(id_gimnasio):
    try:
        if conn.is_connected():
            # Asegura que el ID sea un número entero
            if not str(id_gimnasio).isdigit():
                return False

            cursor.execute("SELECT COUNT(*) FROM Gimnasio WHERE Id_gimnasio = %s", (id_gimnasio,))
            resultado = cursor.fetchone()

            return resultado[0] > 0  # Devuelve True si el servicio existe
        else:
            print("⚠️ Conexión a la base de datos no está activa.")
    except mysql.connector.Error as err:
        print(f"⚠️ Error en la consulta SQL: {err}")
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")

    return False


def seleccionar_profesor():
    try:
        if conn.is_connected():  # Verifica si la conexión sigue activa
            cursor.execute("SELECT * FROM ver_profesor")
            resultados = cursor.fetchall()
            
            if resultados:
                print("\n📋 Lista de Profesores Disponibles:")
                for fila in resultados:
                    print(f'ID: {fila[0]}, Nombre: {fila[1]}, Cargo: {fila[2]}')

                confirmacion = input("¿Quieres seleccionar un profesor existente? (sí/no): ").strip().lower()
                if confirmacion in ["sí", "si"]:
                    dni = input("0 para ingresar un nuevo profesor\nIngrese el ID del profesor: ").strip()
                    while not dni.isdigit() or not verificar_id_profesor(dni):
                        print("0 para ingresar un nuevo profesor\n❌ El ID del profesor no es válido o no existe. Inténtalo de nuevo.")
                        dni = input("Ingrese el ID del profesor: ").strip()
                    
                    if dni != 0 :                
                        return dni
                    
    except mysql.connector.Error as err:
        print(f"⚠️ Error de base de datos: {err}")
    except Exception as e:
        print(f"⚠️ Ocurrió un error inesperado: {e}")

    return new_profesor()