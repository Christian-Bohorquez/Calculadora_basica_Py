
def calculadora_basica():
    print("---- CALCULADORA BÁSICA ----")
    try:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        print("Operaciones disponibles: +, -, *, /")
        operacion = input("Seleccione la operación a realizar: ")

        if operacion == '+':
            resultado = numero1 + numero2
        elif operacion == '-':
            resultado = numero1 - numero2
        elif operacion == '*':
            resultado = numero1 * numero2
        elif operacion == '/':
            if numero2 != 0:
                resultado = numero1 / numero2
            else:
                print("Error: No se puede dividir entre cero.")
                return
        else:
            print("Operación no válida.")
            return

        print(f"Resultado de {numero1} {operacion} {numero2} = {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor ingrese solo números.")

if __name__ == "__main__":
    calculadora_basica()
