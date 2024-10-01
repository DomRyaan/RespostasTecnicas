# Primeiro, iremos gerar a Sequencia de Fibonacci até o numero inserido ou até que o valor seja ultrapassado
def sequencia_fibonacci(valor):
    # Dentro da função, declaramos os primeiros valores da sequencia
    a = 0
    b = 1
    # O Laço de repetição irá rodar enquanto o numero inserido não for atingido ou ultrapassado
    while a < valor:
        a, b = (b, a + b)
    # Aqui, retornaremos um valor booleano
    return a == valor

# Recebemos o numeros
numero = int(input("Digite um numero: "))

# Aqui é onde iremos verificar o retorno da função
# Se retornar 'True' então faz parte da sequencia de fibonacci, se não, não faz parte
if sequencia_fibonacci(numero):
    print(f'{numero} faz parte da sequencia de Fibonacci\n')
else:
    print(f'{numero} não faz parte da sequencia de Fibonacci\n')
