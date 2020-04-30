#Autor: Vitor André
#Data: 13/04/2020
#Função: Cálculo com as quatro operações

print("Digite um dos símbolos matemáticos para realizar uma conta")
print("Soma -> +")
print("Subtração -> -")
print("Multiplicação -> *")
print("Divisão -> /")
print("Caso queria terminar digie 0")
x = str(input("Digite um símbolo para realizar uma operação: "))

while x != "0":
    if x == "+":
        print("Você escolheu soma")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        s = n1 + n2
        print("O resultado deu", s)
        x = str(input("Digite um símbolo para realizar uma operação: "))
    elif x == "-":
        print("Você escolheu subtração")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        sub = n1 - n2
        print("O resultado deu", sub)
        x = str(input("Digite um símbolo para realizar uma operação: "))
    elif x == "*":
        print("Você escolheu multiplicação")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        mult = n1*n2
        print("O resultado deu", mult)
        x = str(input("Digite um símbolo para realizar uma operação: "))
    elif x == "/":
        print("Você escolheu divisão")
        n1 = float(input("Digite o dividendo: "))
        n2 = float(input("Digite o divisor: "))
        div = n1/n2
        print("O resultado deu", format(div, ".2f"))
        x = str(input("Digite um símbolo para realizar uma operação: "))
    else:
        print("Símbolo digitado não reconhecido")
        x = str(input("Digite um símbolo para realizar uma operação: "))
print("Programa finaizado")
    
