class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

    def mostrar_info(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"Título: {self.titulo} | Estado: {estado}\nDescripción: {self.descripcion}"

    def marcar_completada(self):
        self.completada = True

    def editar(self, nuevo_titulo, nueva_descripcion):
        self.titulo = nuevo_titulo
        self.descripcion = nueva_descripcion


def crear_tarea(tareas):
    titulo = input("Ingresa el título de la tarea: ").strip()
    descripcion = input("Ingresa la descripción: ").strip()
    if titulo == "":
        print("El título no puede estar vacío.")
        return
    tarea = Tarea(titulo, descripcion)
    tareas.append(tarea)
    print(f"Tarea '{titulo}' creada correctamente.")


def mostrar_todas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
    else:
        print("\n=== LISTA DE TAREAS ===")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea.mostrar_info()}\n")


def marcar_completada(tareas):
    if not tareas:
        print("No hay tareas que marcar.")
        return
    titulo = input("Ingresa el título de la tarea a marcar como completada: ").strip().lower()
    for tarea in tareas:
        if tarea.titulo.lower() == titulo:
            tarea.marcar_completada()
            print(f"La tarea '{tarea.titulo}' ha sido marcada como completada.")
            return
    print("No se encontró ninguna tarea con ese título.")


def editar_tarea(tareas):
    if not tareas:
        print("No hay tareas para editar.")
        return
    titulo = input("✏️ Ingresa el título de la tarea a editar: ").strip().lower()
    for tarea in tareas:
        if tarea.titulo.lower() == titulo:
            nuevo_titulo = input("Nuevo título: ").strip()
            nueva_desc = input("Nueva descripción: ").strip()
            tarea.editar(nuevo_titulo, nueva_desc)
            print(f"La tarea '{nuevo_titulo}' fue actualizada correctamente.")
            return
    print("No se encontró ninguna tarea con ese título.")


def eliminar_tarea(tareas):
    if not tareas:
        print("No hay tareas para eliminar.")
        return
    titulo = input("🗑Ingresa el título de la tarea a eliminar: ").strip().lower()
    for tarea in tareas:
        if tarea.titulo.lower() == titulo:
            tareas.remove(tarea)
            print(f"La tarea '{tarea.titulo}' ha sido eliminada.")
            return
    print("No se encontró ninguna tarea con ese título.")

def main():
    tareas = []

    print("Bienvenido/a al Gestor de Tareas (POO básica)")

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Crear tarea")
        print("2. Mostrar todas")
        print("3. Marcar como completada")
        print("4. Editar tarea")
        print("5. Eliminar tarea")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ").strip()

        if opcion == "1":
            crear_tarea(tareas)
        elif opcion == "2":
            mostrar_todas(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            editar_tarea(tareas)
        elif opcion == "5":
            eliminar_tarea(tareas)
        elif opcion == "6":
            print("¡Gracias por usar el Gestor de Tareas! Hasta pronto.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
