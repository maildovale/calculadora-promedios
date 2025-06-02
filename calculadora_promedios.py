def ingresar_calificaciones():
    """
    Solicita al usuario ingresar nombre de materia y calificación.
    Devuelve dos listas: materias[] y calificaciones[].
    """
    materias = []
    calificaciones = []

    print("📘 Ingresá materias y sus calificaciones (0 a 10). Escribí 'fin' para terminar.\n")

    while True:
        materia = input("Nombre de la materia (o 'fin' para terminar): ").strip()
        if materia.lower() == 'fin':
            break
        if not materia:
            print("⚠️ El nombre de la materia no puede estar vacío.")
            continue
        if materia in materias:
            print("⚠️ Ya ingresaste esa materia. Evitá duplicados.")
            continue

        try:
            nota = float(input(f"Ingresá la calificación para {materia}: "))
            if 0 <= nota <= 10:
                materias.append(materia)
                calificaciones.append(nota)
            else:
                print("⚠️ La calificación debe estar entre 0 y 10.")
        except ValueError:
            print("❌ Entrada inválida. Ingresá un número.")

    return materias, calificaciones


def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        return None
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral):
    """
    Devuelve una lista de 'Aprobado' o 'Reprobado' según el umbral indicado.
    """
    return ['Aprobado' if nota >= umbral else 'Reprobado' for nota in calificaciones]


def encontrar_extremos(calificaciones):
    """
    Retorna una tupla con los índices de la calificación máxima y mínima.
    """
    if not calificaciones:
        return None, None
    max_index = calificaciones.index(max(calificaciones))
    min_index = calificaciones.index(min(calificaciones))
    return max_index, min_index


def mostrar_resultados(materias, calificaciones, estados, promedio, umbral):
    print("\n📊 Resultados:")
    for i in range(len(materias)):
        print(f" - {materias[i]}: {calificaciones[i]:.2f} ➜ {estados[i]}")
    
    print(f"\n🔢 Promedio general: {promedio:.2f}")
    print(f"📈 Umbral de aprobación: {umbral:.1f}")

    max_i, min_i = encontrar_extremos(calificaciones)
    if max_i is not None:
        print(f"⭐ Materia con mayor nota: {materias[max_i]} ({calificaciones[max_i]:.2f})")
        print(f"⚠️ Materia con menor nota: {materias[min_i]} ({calificaciones[min_i]:.2f})")


def main():
    print("🎓 Calculadora de Promedios con Materias\n")
    materias, calificaciones = ingresar_calificaciones()

    if not materias:
        print("No se ingresaron materias ni calificaciones.")
        return

    umbral = 5.0
    promedio = calcular_promedio(calificaciones)
    estados = determinar_estado(calificaciones, umbral)
    mostrar_resultados(materias, calificaciones, estados, promedio, umbral)


if __name__ == "__main__":
    main()
