import random

def obtener_resultado(jugador, cpu, reglas):
    if jugador == cpu:
        return 0
    elif cpu in reglas[jugador]:
        return 1
    else:
        return -1


def jugar_ronda(opciones, reglas):
    # Pedir jugada del usuario
    while True:
        jugador = input(f"Elige tu jugada {opciones}: ").lower()
        if jugador in opciones:
            break
        print("Opción no válida. Intenta de nuevo.")

    # Jugada de la CPU
    cpu = random.choice(opciones)

    print(f"\nTú eliges: {jugador}")
    print(f"La CPU elige: {cpu}")

    resultado = obtener_resultado(jugador, cpu, reglas)

    if resultado == 0:
        print("¡Empate!\n")
    elif resultado == 1:
        print("¡Ganas esta ronda!\n")
    else:
        print("Gana la CPU esta ronda.\n")

    return resultado


def jugar_partida():
    print("Bienvenido a Piedra, Papel, Tijera, Lagarto, Spock\n")
    print("Reglas:")
    print("  ✂️ Tijera corta papel y decapita lagarto.")
    print("  📄 Papel cubre piedra y refuta Spock.")
    print("  🪨 Piedra aplasta tijera y aplasta lagarto.")
    print("  🦎 Lagarto envenena Spock y devora papel.")
    print("  🖖 Spock vaporiza piedra y rompe tijera.\n")

    opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]

    reglas = {
        "tijera": ["papel", "lagarto"],
        "papel": ["piedra", "spock"],
        "piedra": ["tijera", "lagarto"],
        "lagarto": ["spock", "papel"],
        "spock": ["piedra", "tijera"]
    }

    # Mejor de N
    while True:
        try:
            n = int(input("¿A cuántas rondas quieres jugar? (debe ser un número impar ≥ 1): "))
            if n >= 1 and n % 2 == 1:
                break
            else:
                print("⚠Debe ser un número impar mayor o igual que 1.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

    rondas_necesarias = n // 2 + 1
    victorias_jugador = 0
    victorias_cpu = 0

    print(f"\nPrimero en ganar {rondas_necesarias} rondas será el vencedor.\n")

    # Bucle de rondas
    while victorias_jugador < rondas_necesarias and victorias_cpu < rondas_necesarias:
        resultado = jugar_ronda(opciones, reglas)
        if resultado == 1:
            victorias_jugador += 1
        elif resultado == -1:
            victorias_cpu += 1

        print(f"Marcador → Tú: {victorias_jugador} | CPU: {victorias_cpu}\n")

    # Resultado final
    if victorias_jugador > victorias_cpu:
        print("¡Felicidades! Ganaste la partida.\n")
    else:
        print("La CPU gana la partida. ¡Suerte la próxima vez!\n")


def main():
    while True:
        jugar_partida()
        otra = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if otra != "s":
            print("Gracias por jugar. ¡Hasta pronto!")
            break
        print("\n------------------------------\n")

if __name__ == "__main__":
    main()