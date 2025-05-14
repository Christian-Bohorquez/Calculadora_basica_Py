
def calculadora_basica():
    """
    Función principal que implementa una calculadora con operaciones básicas y avanzadas.
    Permite al usuario realizar múltiples operaciones y muestra los resultados.
    """
    print("\n===== CALCULADORA MEJORADA =====\n")
    
    # Variable para controlar el ciclo principal
    ejecutar = True
    
    while ejecutar:
        try:
            # Menú principal de operaciones
            print("Operaciones disponibles:")
            print("1. Suma (+)")
            print("2. Resta (-)")
            print("3. Multiplicación (*)")
            print("4. División (/)")
            print("5. Potencia (^)")
            print("6. Raíz cuadrada (√)")
            print("7. Módulo (%)")
            print("8. Salir")
            
            # Solicitar al usuario que elija una operación
            opcion = input("\nSeleccione una operación (1-8): ")
            
            # Opción para salir del programa
            if opcion == '8':
                print("\nGracias por usar la calculadora. ¡Hasta pronto!\n")
                ejecutar = False
                continue
                
            # La raíz cuadrada solo necesita un número
            if opcion == '6':
                try:
                    # Solicitar y validar el número
                    numero = float(input("Ingrese el número para calcular su raíz cuadrada: "))
                    
                    # Verificar que el número sea positivo para la raíz cuadrada
                    if numero < 0:
                        print("\nError: No se puede calcular la raíz cuadrada de un número negativo en los reales.\n")
                        continue
                        
                    # Calcular y mostrar el resultado
                    import math
                    resultado = math.sqrt(numero)
                    print(f"\nLa raíz cuadrada de {numero} es: {resultado:.4f}\n")
                    
                except ValueError:
                    print("\nError: Por favor ingrese un número válido.\n")
                continue
            
            # Para las demás operaciones, necesitamos dos números
            if opcion in ['1', '2', '3', '4', '5', '7']:
                try:
                    # Solicitar y validar los números
                    numero1 = float(input("Ingrese el primer número: "))
                    numero2 = float(input("Ingrese el segundo número: "))
                    
                    # Realizar la operación seleccionada
                    if opcion == '1':  # Suma
                        resultado = numero1 + numero2
                        simbolo = '+'
                    elif opcion == '2':  # Resta
                        resultado = numero1 - numero2
                        simbolo = '-'
                    elif opcion == '3':  # Multiplicación
                        resultado = numero1 * numero2
                        simbolo = '*'
                    elif opcion == '4':  # División
                        # Verificar división por cero
                        if numero2 == 0:
                            print("\nError: No se puede dividir entre cero.\n")
                            continue
                        resultado = numero1 / numero2
                        simbolo = '/'
                    elif opcion == '5':  # Potencia
                        resultado = numero1 ** numero2
                        simbolo = '^'
                    elif opcion == '7':  # Módulo (resto de la división)
                        # Verificar división por cero
                        if numero2 == 0:
                            print("\nError: No se puede calcular el módulo con divisor cero.\n")
                            continue
                        resultado = numero1 % numero2
                        simbolo = '%'
                    
                    # Mostrar el resultado con formato
                    print(f"\nResultado: {numero1} {simbolo} {numero2} = {resultado}\n")
                    
                except ValueError:
                    print("\nError: Por favor ingrese números válidos.\n")
                continue
            
            # Si la opción no es válida
            print("\nOpción no válida. Por favor seleccione una opción del 1 al 8.\n")
            
        except Exception as e:
            # Capturar cualquier otro error no previsto
            print(f"\nOcurrió un error inesperado: {str(e)}\n")

# Función para limpiar la pantalla (multiplataforma)
def limpiar_pantalla():
    """
    Limpia la pantalla de la consola en diferentes sistemas operativos.
    """
    import os
    # Comando para Windows
    if os.name == 'nt':
        os.system('cls')
    # Comando para Unix/Linux/MacOS
    else:
        os.system('clear')

# Punto de entrada principal del programa
if __name__ == "__main__":
    try:
        # Limpiar la pantalla al iniciar
        limpiar_pantalla()
        # Iniciar la calculadora
        calculadora_basica()
    except KeyboardInterrupt:
        # Manejar la interrupción del usuario (Ctrl+C)
        print("\n\nPrograma interrumpido por el usuario. ¡Hasta pronto!\n")
