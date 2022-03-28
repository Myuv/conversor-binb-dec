# Converter BINARIO E DECIMAL.
#MENU para escolher conversao
print('''Escolha a conversão:
[1] DECIMAL p/ BINARIO
[2] BINARIO p/ DECIMAL''')
opcao = int (input('Sua opcao: '))
#Conversao dec p/ bin
if opcao == 1:
n = int(input('Digite o valor que deseja converter: '))
def conv_dec_bin (n):
restos = ''
while n > 0:
restos+= str(n%2)
n//=2
return restos[::-1]
print("Conversao em binario eh: " + str(conv_dec_bin(n)))
#Conversao bin p/ dec 
elif opcao == 2:
x = str(input('Digite o valor que deseja converter: '))
res = 0
for i in range(len(x)):
res += int(x[i]) * 2 ** (len(x) - i - 1)
print('A conversao para DECIMAL eh: ', res)
