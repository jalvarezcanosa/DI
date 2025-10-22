from operaciones import suma, resta, multiplicacion, division

def calculadora():
    while True:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Error: introduce valores numéricos válidos.")
            continue

        print("\nOperaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")

        opcion = input("Elige una operación (1-4): ")

        if opcion == "1":
            resultado = suma(num1, num2)
        elif opcion == "2":
            resultado = resta(num1, num2)
        elif opcion == "3":
            resultado = multiplicacion(num1, num2)
        elif opcion == "4":
            resultado = division(num1, num2)
        else:
            print("Opción no válida.")
            continue

        print(f"Resultado: {resultado}")

        continuar = input("\n¿Quieres hacer otra operación? (s/n): ").lower()
        if continuar != "s":
            print("Saliendo")
            break

calculadora()