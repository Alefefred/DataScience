#Solicitar ao usuário que insira um número
numero = int(input("Digite um número inteiro: "))

#Imprimir a tabuada do número selecionado até 10
print(f"\nTabuada do {numero}:\n")
for i in range(1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")