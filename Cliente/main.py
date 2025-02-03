import os

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
    print(f"{COLOR_BLUE}{'📋 MENÚ DE GESTIÓN DE GIMNASIOS Y ALUMNOS':^40}")
    print(f"{COLOR_HEADER}{'='*40}{COLOR_RESET}")
    
    print(f"{COLOR_GREEN}1. 📚 Gestión de Alumnos")
    print(f"{COLOR_GREEN}2. 🏋️‍♂️ Gestión de Gimnasios")
    print(f"{COLOR_RED}3. 🚪 Salir{COLOR_RESET}")
    print(f"{COLOR_HEADER}{'='*40}{COLOR_RESET}")

def menu_alumnos():
    limpiar_pantalla()
    print(f"{COLOR_HEADER}{'='*40}")
    print(f"{COLOR_BLUE}{'📚 MENÚ DE ALUMNOS':^40}")
    print(f"{COLOR_HEADER}{'='*40}{COLOR_RESET}")
    print(f"{COLOR_GREEN}1. Listar alumnos")
    print(f"{COLOR_GREEN}2. Agregar alumno")
    print(f"{COLOR_GREEN}3. Eliminar alumno")
    print(f"{COLOR_GREEN}4. Editar alumno")
    print(f"{COLOR_RED}5. Volver al menú principal{COLOR_RESET}")
    print(f"{COLOR_HEADER}{'='*40}{COLOR_RESET}")

def menu_gimnasios():
    limpiar_pantalla()
    print(f"{COLOR_HEADER}{'='*40}")
    print(f"{COLOR_BLUE}{'🏋️‍♂️ MENÚ DE GIMNASIOS':^40}")
    print(f"{COLOR_HEADER}{'='*40}{COLOR_RESET}")
    print(f"{COLOR_GREEN}1. Listar gimnasios")
    print(f"{COLOR_GREEN}2. Agregar gimnasio")
    print(f"{COLOR_GREEN}3. Eliminar gimnasio")
    print(f"{COLOR_GREEN}4. Editar gimnasio")
    print(f"{COLOR_RED}5. Volver al menú principal{COLOR_RESET}")
    print(f"{COLOR_HEADER}{'='*40}{COLOR_RESET}")

def main():
    while True:
        mostrar_menu()
        opcion = input(f"{COLOR_YELLOW}Seleccione una opción: {COLOR_RESET}")
        
        if opcion == "1":
            while True:
                menu_alumnos()
                opcion_alumno = input(f"{COLOR_YELLOW}Seleccione una opción de alumno: {COLOR_RESET}")
                
                if opcion_alumno == "1":
                    print(f"{COLOR_GREEN}Opción seleccionada: Listar alumnos{COLOR_RESET}")
                    #listar_alumnos()
                elif opcion_alumno == "2":
                    print(f"{COLOR_GREEN}Opción seleccionada: Agregar alumno{COLOR_RESET}")
                    #agregar_alumno()
                elif opcion_alumno == "3":
                    print(f"{COLOR_GREEN}Opción seleccionada: Eliminar alumno{COLOR_RESET}")
                    #eliminar_alumno()
                elif opcion_alumno == "4":
                    print(f"{COLOR_GREEN}Opción seleccionada: Editar alumno{COLOR_RESET}")
                    #editar_alumno()
                elif opcion_alumno == "5":
                    break  # Volver al menú principal
                else:
                    print(f"{COLOR_RED}❌ Opción inválida. Intente de nuevo.{COLOR_RESET}")
                input(f"\n{COLOR_YELLOW}Presione Enter para continuar...{COLOR_RESET}")
                    

        elif opcion == "2":
            while True:
                menu_gimnasios()
                opcion_gimnasio = input(f"{COLOR_YELLOW}Seleccione una opción de gimnasio: {COLOR_RESET}")
                
                if opcion_gimnasio == "1":
                    print(f"{COLOR_GREEN}Opción seleccionada: Listar gimnasios{COLOR_RESET}")
                    #listar_gimnasios()
                elif opcion_gimnasio == "2":
                    print(f"{COLOR_GREEN}Opción seleccionada: Agregar gimnasio{COLOR_RESET}")
                    #agregar_gimnasio()
                elif opcion_gimnasio == "3":
                    print(f"{COLOR_GREEN}Opción seleccionada: Eliminar gimnasio{COLOR_RESET}")
                    #eliminar_gimnasio()
                elif opcion_gimnasio == "4":
                    print(f"{COLOR_GREEN}Opción seleccionada: Editar gimnasio{COLOR_RESET}")
                    #editar_gimnasio()
                elif opcion_gimnasio == "5":
                    break  # Volver al menú principal
                else:
                    print(f"{COLOR_RED}❌ Opción inválida. Intente de nuevo.{COLOR_RESET}")
                input(f"\n{COLOR_YELLOW}Presione Enter para continuar...{COLOR_RESET}")

        elif opcion == "3":
            print(f"{COLOR_RED}Saliendo del programa. ¡Hasta luego! 👋{COLOR_RESET}")
            break
        else:
            print(f"{COLOR_RED}❌ Opción inválida. Intente de nuevo.{COLOR_RESET}")
        
        input(f"\n{COLOR_YELLOW}Presione Enter para continuar...{COLOR_RESET}")

if __name__ == "__main__":
    main()

