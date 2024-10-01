texto = "Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre."
texto_padronizado = texto.lower()

if 'a' in texto:
    print(f"A Letra 'a' aparece no texto :)")
else:
    print("Infelizmente não tem a letra 'a' no texto :(")

print(f"A letra 'a' aparece: {texto_padronizado.count('a')} vezes")