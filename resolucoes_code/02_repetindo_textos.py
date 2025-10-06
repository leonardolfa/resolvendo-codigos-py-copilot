# Agora vamos solicitar uma string e um número inteiro como entrada. 
# Depois teremos que retornar a string repetida o número de vezes informado.

texto = input("Digite um texto: ")
quantidade = int(input("Digite um número inteiro: "))

print((texto + " ") * quantidade)

#outra forma de fazer: porem em linhas diferentes
# for i in range(quantidade):
#     print(texto)