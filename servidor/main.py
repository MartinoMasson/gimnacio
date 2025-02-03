from connection import conn,cursor,cerrar_conexion
from gimnasio import new_gym, eliminar_gimnasio,modificar_gimnasio,mostrar_gimnasios, verificar_id_gimnasio
from servicios import new_service,actualizar_servicio,mostrar_servicios, verificar_id_servicio, eliminar_servicio

import os

# Función para limpiar la pantalla según el sistema operativo
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Colores ANSI
COLOR_HEADER = "\033[95m"
COLOR_BLUE = "\033[94m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"

def mostrar_menu():
    limpiar_pantalla()
    print(f"{COLOR_HEADER}{'='*40}")
    print(f"{COLOR_BLUE}{'📋  MENÚ DE GESTIÓN DE GIMNASIOS':^40}")
    print(f"{COLOR_HEADER}{'='*40}{COLOR_RESET}")
    print(f"{COLOR_GREEN}1. 🧑‍💼 Agregar cliente")
    print("2. 🏋️  Eliminar gimnasio")
    print("3. ✏️  Modificar gimnasio")
    print("4. ➕ Agregar servicio")
    print("5. 🔄 Actualizar servicio")
    print("6. ❌ eliminar servicio")
    print("7. 📊 Mostrar servicios")
    print("8. 🏢 Mostrar gimnasios")
    print(f"{COLOR_RED}9. 🚪 Salir{COLOR_RESET}")
    print(f"{COLOR_HEADER}{'='*40}{COLOR_RESET}")

def main():
    while True:
        mostrar_menu()
        opcion = input(f"{COLOR_YELLOW}Seleccione una opción: {COLOR_RESET}")
        
        if opcion == "1":
            print(f"{COLOR_GREEN}Opción seleccionada: Agregar cliente{COLOR_RESET}")
            new_gym()
        elif opcion == "2":
            print(f"{COLOR_GREEN}Opción seleccionada: Eliminar gimnasio{COLOR_RESET}")
            mostrar_gimnasios()

            id_gimnasio = input("0 para cancelar la operación\nIngrese el ID del gimnasio que desea eliminar: ").strip()

            # Validación del ID
            while id_gimnasio != "0" and not verificar_id_gimnasio(id_gimnasio):
                print("❌ El ID del gimnasio no es válido o no existe. Inténtalo de nuevo.")
                id_gimnasio = input("0 para cancelar la operación\nIngrese el ID del gimnasio que desea eliminar: ").strip()

            # Verificación final antes de eliminar
            if id_gimnasio != "0":
                    eliminar_gimnasio(id_gimnasio)
            else:
                print(f"{COLOR_YELLOW}❗ Operación cancelada por el usuario.{COLOR_RESET}")
        elif opcion == "3":
            print(f"{COLOR_GREEN}Opción seleccionada: Modificar gimnasio{COLOR_RESET}")
            modificar_gimnasio()
        elif opcion == "4":
            print(f"{COLOR_GREEN}Opción seleccionada: Agregar servicio{COLOR_RESET}")
            new_service()
        elif opcion == "5":
            print(f"{COLOR_GREEN}Opción seleccionada: Actualizar servicio{COLOR_RESET}")
            actualizar_servicio()
        elif opcion == "6":
            print(f"{COLOR_GREEN}Opción seleccionada: Eliminar servicio{COLOR_RESET}")
            mostrar_servicios()

            id_servicio = input("0 para cancelar la operación\nIngrese el ID del servicio que desea eliminar: ").strip()
            while id_servicio != "0" and not verificar_id_servicio(id_servicio):
                print("❌ El ID del servicio no es válido o no existe. Inténtalo de nuevo.")
                id_servicio = input("0 para cancelar la operación\nIngrese el ID del servicio que desea eliminar: ").strip()

            # Verificación final antes de eliminar
            if id_servicio != "0":
                    eliminar_servicio(id_servicio)
            else:
                print(f"{COLOR_YELLOW}❗ Operación cancelada por el usuario.{COLOR_RESET}")
        elif opcion == "7":
            print(f"{COLOR_GREEN}Opción seleccionada: Mostrar servicios{COLOR_RESET}")
            mostrar_servicios()
        elif opcion == "8":
            print(f"{COLOR_GREEN}Opción seleccionada: Mostrar gimnasios{COLOR_RESET}")
            mostrar_gimnasios()
        elif opcion == "9":
            print(f"{COLOR_RED}Saliendo del programa. ¡Hasta luego! 👋{COLOR_RESET}")
            cerrar_conexion(conn,cursor)
            break
        else:
            print(f"{COLOR_RED}❌ Opción inválida. Intente de nuevo.{COLOR_RESET}")
        
        input(f"\n{COLOR_YELLOW}Presione Enter para continuar...{COLOR_RESET}")

if __name__ == "__main__":
    main()