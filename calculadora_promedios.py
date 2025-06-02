def ingresar_calificaciones():
    """
    Solicita al usuario ingresar materias y sus calificaciones.
    Devuelve dos listas: una con los nombres de las materias y otra con las calificaciones.
    """
    materias = []
    calificaciones = []

    print("Ingresar materias y calificaciones (entre 0 y 10). Escribir 'fin' para terminar.")

    while True:
        materia = input("Nombre de la materia: ").strip()
        if materia.lower() == "fin":
            break
        if not materia:
            print("El nombre de la materia no puede estar vacío.")
            continue
        if materia in materias:
            print("La materia ya fue ingresada.")
            continue

        try:
            nota = float(input(f"Calificación para {materia}: "))
            if 0 <= nota <= 10:
                materias.append(materia)
                calificaciones.append(nota)
            else:
                print("La calificación debe estar entre 0 y 10.")
        except ValueError:
            print("Entrada inválida. Ingresar un número.")

    return materias, calificaciones


def calcular_promedio(calificaciones):
    if not calificaciones:
        return None
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral):
    """
    Clasifica cada calificación como 'Aprobado' o 'Reprobado' según el umbral.
    """
    return ["Aprobado" if nota >= umbral else "Reprobado" for nota in calificaciones]


def encontrar_extremos(calificaciones):
    """
    Retorna los índices de la calificación máxima y mínima.
    """
    if not calificaciones:
        return None, None
    max_i = calificaciones.index(max(calificaciones))
    min_i = calificaciones.index(min(calificaciones))
    return max_i, min_i


def mostrar_resultados(materias, calificaciones, estados, promedio, umbral):
    print("\nResultados por materia:")
    for i in range(len(materias)):
        print(f"{materias[i]}: {calificaciones[i]:.2f} - {estados[i]}")

    print(f"\nPromedio general: {promedio:.2f}")
    print(f"Umbral de aprobación: {umbral:.1f}")

    max_i, min_i = encontrar_extremos(calificaciones)
    if max_i is not None:
        print(f"Materia con mayor nota: {materias[max_i]} ({calificaciones[max_i]:.2f})")
        print(f"Materia con menor nota: {materias[min_i]} ({calificaciones[min_i]:.2f})")


def main():
    materias, calificaciones = ingresar_calificaciones()

    if not materias:
        print("No se ingresaron datos.")
        return

    umbral = 5.0
    promedio = calcular_promedio(calificaciones)
    estados = determinar_estado(calificaciones, umbral)
    mostrar_resultados(materias, calificaciones, estados, promedio, umbral)


if __name__ == "__main__":
    main()
