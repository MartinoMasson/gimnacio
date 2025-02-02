import mysql.connector
from connection import conn, cursor, Abrir_conexion

conn = Abrir_conexion()
if conn:
    cursor = conn.cursor()

def new_service():
    nombre = input("Ingrese el nombre del servicio: ")
    costo = input("Ingrese el costo del servicio: ")
    descripcion = input("Ingrese la descripcion del servicio: ")
    
    try:
        cursor.execute("insert into Servicio (nombre, costo, descripcion) values (%s, %s)", (nombre, costo, descripcion))
    
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
    nuevo_costo = None
    nueva_descripcion = None

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

    # Confirmar si se desea actualizar la descripción
    confirmar_desc = input(f"\n¿Desea editar la descripción del servicio con ID {id_servicio}? (sí/no): ").strip().lower()
    if confirmar_desc in ['sí', 'si']:
        nueva_descripcion = input("Ingrese la nueva descripción del servicio: ").strip()

    # Si no hay cambios, salir de la función
    if nuevo_costo is None and nueva_descripcion is None:
        print("No se realizaron cambios.")
        return

    try:
        # Actualizar solo los campos que se modificaron
        if nuevo_costo is not None:
            cursor.execute("UPDATE Servicio SET costo = %s WHERE id_servicio = %s", (nuevo_costo, id_servicio))    

        if nueva_descripcion:
            cursor.execute("UPDATE Servicio SET descripcion = %s WHERE id_servicio = %s", (nueva_descripcion, id_servicio))    

        conn.commit()
        print("Servicio actualizado exitosamente.")

    except mysql.connector.Error as err:
        print(f"Error al actualizar el servicio: {err}")

def mostrar_servicios():
    if conn:
        cursor.execute("SELECT * FROM Servicio")
        
        resultados = cursor.fetchall()

        # Mostrar los resultados
        for fila in resultados:
            print('ID:',fila[0],', Nombre: $',fila[1],', Costo: $',fila[2],', Descripcion:',fila[3],)
            
    else:
        print("No se pudo establecer la conexión.")

def verificar_id_servicio(id_servicio):
    if conn:
        cursor.execute("SELECT COUNT(*) FROM Servicio WHERE Id_servicio = %s", (id_servicio,))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        return resultado[0] > 0  # Devuelve True si el servicio existe
    return False