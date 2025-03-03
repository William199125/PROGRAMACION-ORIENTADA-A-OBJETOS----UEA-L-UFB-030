### Programación Tradicional
# Implementación utilizando funciones y estructura tradicional

def ingresar_temperaturas():
    """
    Función para ingresar temperaturas diarias durante una semana.
    Retorna una lista con 7 temperaturas ingresadas.
    """
    temperaturas = []
    print("\n--- Ingreso de temperaturas diarias ---")
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingresa la temperatura del día {i + 1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio de las temperaturas ingresadas.
    """
    return sum(temperaturas) / len(temperaturas)


def main():
    """
    Función principal que organiza la ejecución del programa.
    """
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print("\n--- Resultados ---")
    print(f"Temperaturas ingresadas: {temperaturas}")
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")


# Ejecución del programa principal
if __name__ == "__main__":
    main()