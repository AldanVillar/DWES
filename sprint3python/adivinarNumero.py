import random

def jugar():
    print("¡Bienvenido al juego de 'Adivina el número'!")
    print("El programa pensará un número entre 1 y un máximo que tú elijas.")
    print("Intenta adivinarlo con la menor cantidad de intentos posible.\n")

    # Elegir nivel de dificultad
    while True:
        nivel = input("Elige un nivel de dificultad (facil / medio / dificil): ").lower()

        if nivel == "facil":
            max_num = 50
            break
        elif nivel == "medio":
            max_num = 100
            break
        elif nivel == "dificil":
            max_num = 500
            break
        else:
            print("Nivel no válido. Por favor, escribe 'facil', 'medio' o 'dificil'.")

    # Generar número secreto
    numero_secreto = random.randint(1, max_num)
    intentos = 0

    print(f"\nHe pensado un número entre 1 y {max_num}. ¡Adivina cuál es!\n")

    # Bucle principal del juego
    while True:
        try:
            intento = int(input("Ingresa tu número: "))
            if intento < 1 or intento > max_num:
                print(f"El número debe estar entre 1 y {max_num}.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
            continue

        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo.")
        elif intento > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
            break

def main():
    while True:
        jugar()
        otra = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if otra != "s":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        print("\n------------------------------\n")

if __name__ == "__main__":
    main()