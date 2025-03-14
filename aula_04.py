numero = int(input("Digite um número para a tabuada : "))

for x in range(1,numero):
 print("-------------------------------------------")
 for i in range(1,11):
    resultado = i * x
    print(f"{x} * {i} = {resultado}")
    