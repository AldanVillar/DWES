def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")


def consultar_saldo(cuenta):
    print(f"\nTu saldo actual es: ${cuenta['saldo']:.2f}")


def ingresar_dinero(cuenta):
    while True:
        try:
            cantidad = float(input("Ingresa la cantidad a depositar: "))
            if cantidad > 0:
                cuenta["saldo"] += cantidad
                print(f"Depósito realizado con éxito. Nuevo saldo: ${cuenta['saldo']:.2f}")
                break
            else:
                print("La cantidad debe ser positiva.")
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")


def retirar_dinero(cuenta):
    while True:
        try:
            cantidad = float(input("Ingresa la cantidad a retirar: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que 0.")
            elif cantidad > cuenta["saldo"]:
                print("Saldo insuficiente.")
            else:
                cuenta["saldo"] -= cantidad
                print(f"Retiro exitoso. Nuevo saldo: ${cuenta['saldo']:.2f}")
                break
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")


def main():
    # Representar la cuenta
    cuenta = {"nombre": "Ana", "saldo": 1200.0}

    print(f"¡Bienvenida, {cuenta['nombre']}!")
    print("Simulador de Cajero Automático\n")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            consultar_saldo(cuenta)
        elif opcion == "2":
            ingresar_dinero(cuenta)
        elif opcion == "3":
            retirar_dinero(cuenta)
        elif opcion == "4":
            print("\nGracias por usar el cajero. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    main()