#juego de puedra papel o tijeras hecho por Aurora Matamoros
import random

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Jugar Piedra, Papel o Tijeras")
    print("2. Salir")

def obtener_eleccion_usuario():
    print("\nElige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijeras")
    opcion = input("Tu elección (1-3): ")
    if opcion == '1':
        return "piedra"
    elif opcion == '2':
        return "papel"
    elif opcion == '3':
        return "tijeras"
    else:
        print("Opción inválida. Intenta de nuevo.")
        return None

def obtener_eleccion_maquina():
    return random.choice(["piedra", "papel", "tijeras"])

def determinar_ganador(usuario, maquina):
    if usuario == maquina:
        return "Empate"
    elif (usuario == "piedra" and maquina == "tijeras") or \
         (usuario == "papel" and maquina == "piedra") or \
         (usuario == "tijeras" and maquina == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"

def jugar():
    usuario = None
    while usuario is None:
        usuario = obtener_eleccion_usuario()
    maquina = obtener_eleccion_maquina()
    print(f"\nTu elección: {usuario}")
    print(f"Elección de la máquina: {maquina}")
    resultado = determinar_ganador(usuario, maquina)
    print(f"Resultado: {resultado}")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1 o 2): ")
    if opcion == '1':
        jugar()
    elif opcion == '2':
        print("¡Gracias por jugar! Hasta la próxima.")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")
