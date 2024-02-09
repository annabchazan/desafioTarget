
string_usuario = input("Digite uma string: ")

indice = len(string_usuario) - 1
string_invertida = ""

while indice >= 0:
    string_invertida += string_usuario[indice]
    indice -= 1


print(f"A string invertida é: {string_invertida}")
