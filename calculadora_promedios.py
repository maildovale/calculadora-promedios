def ingresar_notas():
    notas = []
    while True:
        try:
            nota = float(input("Ingresá una nota (o escribí -1 para terminar): "))
            if nota == -1:
                break
            elif 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("⚠️ La nota debe estar entre 0 y 10.")
        except ValueError:
            print("❌ Entrada inválida. Por favor ingresá un número.")
    return notas

def calcular_promedio(notas):
    if len(notas) == 0:
        return None
    return sum(notas) / len(notas)

def mostrar_resultado(promedio):
    if promedio is None:
        print("No se ingresaron notas.")
    else:
        print(f"\n📊 Promedio final: {promedio:.2f}")
        if promedio >= 6:
            print("✅ ¡Aprobado!")
        else:
            print("❌ Reprobado. ¡Ánimo, podés mejorar!")

def main():
    print("🎓 Calculadora de Promedios Escolares 🎓\n")
    notas = ingresar_notas()
    promedio = calcular_promedio(notas)
    mostrar_resultado(promedio)

if __name__ == "__main__":
    main()
