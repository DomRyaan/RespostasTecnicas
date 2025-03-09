
def sequencia_fibonacci(valor):
    if valor < 0:
        return False
    
    a = 0 
    b = 1

    while a <= valor:
        if a == valor:
            return True
        a = b
        b = a + b
    return False

numero = int(input("Digite um numero: "))

if sequencia_fibonacci(numero):
    print(f'{numero} faz parte da sequencia de Fibonacci\n')
else:
    print(f'{numero} não faz parte da sequencia de Fibonacci\n')
