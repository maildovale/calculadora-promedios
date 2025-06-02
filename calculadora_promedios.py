Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def ingresar_notas():
...     """
...     Solicita al usuario ingresar notas válidas (entre 0 y 10).
...     Devuelve una lista de notas ingresadas.
...     """
...     notas = []
...     while True:
...         try:
...             nota = float(input("Ingresá una nota (o escribí -1 para terminar): "))
...             if nota == -1:
...                 break
...             elif 0 <= nota <= 10:
...                 notas.append(nota)
...             else:
...                 print("⚠️ La nota debe estar entre 0 y 10.")
...         except ValueError:
...             print("❌ Entrada inválida. Por favor ingresá un número.")
...     return notas
... 
... 
... def calcular_promedio(notas):
...     """
...     Calcula y devuelve el promedio de una lista de notas.
...     """
...     if len(notas) == 0:
...         return None
...     return sum(notas) / len(notas)
... 
... 
... def mostrar_resultado(promedio):
...     """
...     Muestra el promedio y un mensaje según el desempeño.
...     """
...     if promedio is None:
...         print("No se ingresaron notas.")
...     else:
        print(f"\n📊 Promedio final: {promedio:.2f}")
        if promedio >= 6:
            print("✅ ¡Aprobado!")
        else:
            print("❌ Reprobado. ¡Ánimo, podés mejorar!")


# Programa principal
def main():
    print("🎓 Calculadora de Promedios Escolares 🎓\n")
    notas = ingresar_notas()
    promedio = calcular_promedio(notas)
    mostrar_resultado(promedio)

# Ejecutar programa
if __name__ == "__main__":
    main()
