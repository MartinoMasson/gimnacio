import mysql.connector
from connection import conn, cursor, Abrir_conexion

# Colores ANSI
COLOR_HEADER = "\033[95m"
COLOR_BLUE = "\033[94m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"

conn = Abrir_conexion()
if conn:
    cursor = conn.cursor()

def new_service():
    nombre = input("Ingrese el nombre del servicio: ")
    costo = input("Ingrese el costo del servicio: ")
    descripcion = input("Ingrese la descripcion del servicio: ")
    
    try:
        cursor.execute("insert into Servicio (nombre, costo, descripcion) values (%s, %s, %s)", (nombre, costo, descripcion))
    
        conn.commit()
        print("Gimnasio agregada exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al insertar datos: {err}")

 
def actualizar_servicio():
    mostrar_servicios()
    id_servicio = input("Ingrese el ID del servicio a actualizar: ").strip()
    
    # Verificar si el ID de servicio existe
    if not verificar_id_servicio(id_servicio):
        print(f"El servicio con ID {id_servicio} no existe.")
        return

    # Inicializamos variables para evitar errores si no se actualiza algo
    nuevo_nombre = None
    nuevo_costo = None
    nueva_descripcion = None

    # Confirmar si se desea actualizar el nombre
    confirmar_nombre = input(f"\n¿Desea editar el nombre del servicio con ID {id_servicio}? (sí/no): ").strip().lower()
    if confirmar_nombre in ['sí', 'si']:
        nuevo_nombre = input("Ingrese el nuevo nombre del servicio: ").strip()
        while not nuevo_nombre:
            print("❗ El nombre no puede estar vacío.")
            nuevo_nombre = input("Ingrese el nuevo nombre del servicio: ")
    else:
        # Si no se quiere actualizar el nombre, se mantiene el nombre actual
        cursor.execute("SELECT nombre FROM Servicio WHERE id_servicio = %s", (id_servicio,))
        nuevo_nombre = cursor.fetchone()[0]

    # Confirmar si se desea actualizar el costo
    confirmar_costo = input(f"\n¿Desea editar el costo del servicio con ID {id_servicio}? (sí/no): ").strip().lower()
    if confirmar_costo in ['sí', 'si']:
        while True:
            nuevo_costo = input("Ingrese el nuevo costo del servicio: ").strip()
            if nuevo_costo.isdigit() and int(nuevo_costo) > 0:
                nuevo_costo = int(nuevo_costo)
                break
            else:
                print("Por favor, ingrese un costo válido (número positivo).")
    else:
        # Si no se quiere actualizar el costo, se mantiene el costo actual
        cursor.execute("SELECT costo FROM Servicio WHERE id_servicio = %s", (id_servicio,))
        nuevo_costo = cursor.fetchone()[0]

    # Confirmar si se desea actualizar la descripción
    confirmar_descripcion = input(f"\n¿Desea editar la descripción del servicio con ID {id_servicio}? (sí/no): ").strip().lower()
    if confirmar_descripcion in ['sí', 'si']:
        nueva_descripcion = input("Ingrese la nueva descripción del servicio: ").strip()
        while not nueva_descripcion:
            print("❗ La descripción no puede estar vacía.")
            nueva_descripcion = input("Ingrese la nueva descripción del servicio: ")
    else:
        # Si no se quiere actualizar la descripción, se mantiene la descripción actual
        cursor.execute("SELECT descripcion FROM Servicio WHERE id_servicio = %s", (id_servicio,))
        nueva_descripcion = cursor.fetchone()[0]

    # Confirmar cambios
    print("\nDatos actualizados del servicio:")
    print(f"✅ Nombre: {nuevo_nombre}")
    print(f"✅ Costo: {nuevo_costo}")
    print(f"✅ Descripción: {nueva_descripcion}")

    confirmar = input("\n¿Desea guardar los cambios? (sí/no): ").strip().lower()
    if confirmar in ['sí', 'si']:
        try:
            cursor.execute("""
                UPDATE Servicio
                SET nombre = %s, costo = %s, descripcion = %s
                WHERE id_servicio = %s
            """, (nuevo_nombre, nuevo_costo, nueva_descripcion, id_servicio))
            conn.commit()  # Guardar cambios
            print(f"{COLOR_GREEN}✅ Servicio modificado exitosamente.{COLOR_RESET}")
        except mysql.connector.Error as err:
            print(f"{COLOR_RED}⚠️ Error al modificar el servicio: {err}{COLOR_RESET}")
    else:
        print(f"{COLOR_YELLOW}❗ Modificación cancelada. No se realizaron cambios.{COLOR_RESET}")


def mostrar_servicios():
    if conn:
        cursor.execute("SELECT * FROM Servicio")
        
        resultados = cursor.fetchall()

        # Mostrar los resultados
        for fila in resultados:
            print('ID:',fila[0],'\nNombre:',fila[1],'\nCosto: $',fila[2],'\nDescripcion:',fila[3],'\n')
            
    else:
        print("No se pudo establecer la conexión.")

def verificar_id_servicio(id_servicio):
    if conn and id_servicio.isdigit():
        cursor.execute("SELECT COUNT(*) FROM Servicio WHERE Id_servicio = %s", (id_servicio,))
        resultado = cursor.fetchone()
        return resultado[0] > 0 
    
    return False


def eliminar_servicio(id_servicio):
    print(id_servicio)
    try:
        if not verificar_id_servicio(id_servicio):
            print(f"{COLOR_RED}❌ El ID {id_servicio} no existe en la base de datos.{COLOR_RESET}")
            return

        confirmar = input(f"⚠️ ¿SEGURO QUE DESEAS ELIMINAR EL GIMNASIO CON ID: {id_servicio}? (sí/no): ").strip().lower()
        
        if confirmar in ['sí', 'si']:
            cursor.execute("DELETE FROM Servicio WHERE id_servicio = %s", (id_servicio,))
            conn.commit()  # Confirmar los cambios en la base de datos
            print(f"{COLOR_RED}✅ Gimnasio con ID {id_servicio} eliminado exitosamente.{COLOR_RESET}")
        else:
            print(f"{COLOR_YELLOW}❗ Operación cancelada por el usuario.{COLOR_RESET}")

    except mysql.connector.Error as err:
        print(f"{COLOR_RED}⚠️ Error al eliminar el gimnasio: {err}{COLOR_RESET}")
    except Exception as e:
        print(f"{COLOR_RED}⚠️ Error inesperado: {e}{COLOR_RESET}")