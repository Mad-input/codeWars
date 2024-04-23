def calculadora():
    print("Calculadora Básica")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))


    opcion = input("Seleccione la operación 1: suma 2: resta 3: multiplicacion 4: divicion : ")

    if opcion == '1':
        resultado = num1 + num2
        print(f"\nResultado: {resultado}")
    elif opcion == '2':
        resultado = num1 - num2
        print(f"\nResultado: {resultado}")
    elif opcion == '3':
        resultado = num1 * num2
        print(f"\nResultado: {resultado}")
    elif opcion == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"\nResultado: {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    else:
        print("Opción no válida. Por favor, seleccione una operación válida.")

# Llamada a la función calculadora
calculadora()