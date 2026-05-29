import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
    sinalizando que o cálculo não pôde ser realizado.
    """
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    
    elif operador == "-":
        result = num1 - num2
    
    elif operador == "*":   
        result = num1 * num2
        
    elif operador == "/":
        result = num1 / num2
    
    elif operador == "**":
        result = num1 ** num2
        
    elif operador == "%":
        result = num1 % num2

    return result

def calculadora_v2(num1: float, num2: float, operador: str) -> float:
    
    operacoes = {
        "+": num1 + num2
        "-": num1 - num2
        "*": num1 * num2
        "/": num1 / num2
        "**": num1 ** num2
        "%": num1 % num2
    }
    
    return operacoes.get(operador, float("nan"))


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')
    
        num1 = float(input( "Primeiro númmero: "))
        operador = input("Operador (+, -, /, **, %): ")
        num2= float(input("Segundo número:" ))
        
        print("\n Escolha a versão desejada da calculadora: ")
        print(" 1 - calculadora ()")
        print(" 2 - calculadorav2 () ")
        
        escolha = input( "Opção: ")
        
        if escolha == "1"
            resultado

        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')
