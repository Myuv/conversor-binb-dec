# Conversão de Binário para decimal
num = input('Digite o número binário: ')
resultado = []

for i in range(len(num)):
    if int(num[::-1][i]) == 1:
        resultado += 2 ** i

print(resultado)



#Conversão de Decimal para binário

num = int(input("Digite o número decimal: "))
binario = ''

while True:
    binario += str(0 if num % 2 == 0 else 1)
    num //= 2
    if num == 0:
        break

print(binario[::-1])