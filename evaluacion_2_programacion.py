#Bienvenidos a la evaluacion 2 en GitHub!
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa():
    input("Presione Enter para continuar...")

def mostrar_menu():
    limpiar_pantalla()
    print("\nSistema de Gestión Escolar")
    print("1.Crear")
    print("2. Leer")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Salir")
