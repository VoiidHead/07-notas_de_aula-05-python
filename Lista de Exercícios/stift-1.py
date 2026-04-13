#1
lorax = int(input('Digite um número inteiro para saber se ele é positivo: '))

if lorax > 0:
	print('O número é positivo')
else:
	print('O número não é positivo')

#2
capivas = int(input('Digite sua idade para saber se você é ou não maior de idade: '))

if capivas >= 18:
	print('Você é maior de idade.')
else:
	print('Você não é maior de idade.')

#3
print('Digite dois números inteiros para descobrir se o primeiro número é maior do que o segundo.')
capivárias = int(input())
estrito = int(input())
lacks = max(capivárias, estrito )

if lacks == capivárias:
	print(f'O primeiro número é maior.')
else:
	print(f'O primeiro número não é maior.')

#4
sséverdade = int(input('Digite um número inteiro para descobrir se ele é par: '))
if sséverdade % 2 == 0:
	print('O número é par.')
else:
	print('O número não é par.')

#5
osabortivos = float(input('Digite sua nota para saber se você está aprovado ou não: '))

if osabortivos >= 7:
	print('Aprovado')
else:
	print('Reprovado')

#6
stomp = float(input('Digite sua temperatura corporal (em °C): '))
if stomp > 37.5:
	print('Você está com febre.')
else:
	print('Você não está com febre.')

#7
trint = input("Digite seu nome de usuário: ")
lax = len(trint)

if  lax > 10:
    print("O nome de usuário é muito longo.")
else:
    print("O nome de usuário é válido.")

#8
rooster_fight = int(input('Digite um número inteiro para descobrir se é divisível por três: '))
if rooster_fight % 3 == 0:
	print('Divisível por três')
else:
	print('Não divisível por três')

#9
print('Digite dois números inteiros para descobrir se eles são iguais.')
a = int(input())
b = int(input())
if a == b:
	print('Os números são iguais.')
else:
	print('Os números não são iguais.')

#10
p = int(input('Digite um número inteiro para descobrir seu módulo: '))
if p >= 0:
    print(f'Valor absoluto: {p}')
else:
	print(f'Valor absoluto: {-p}')
	
#11
rost = int(input('Digite um número inteiro para descobrir se é divisível por seis: '))
if rost % 6 == 0:
	print('Divisível por 2 e por 3')
else:
	print('Não divisível por 2 e por 3')

#12
supremacia = input("Digite uma palavra: ")
if 'A' == supremacia[0] == 'A':
    print("A palavra começa com A")
else:
	print("A palavra não começa com A")

#13
voxel = float(input('Digite a velocidade de um carro (em km/h): '))
if voxel > 80:
    print('Acima do limite de velocidade.')
else:
    print('Dentro do limite de velocidade.')

#14
print('Digite três notas de um aluno para saber a média entre as três.')
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
media = (nota1 + nota2 + nota3) / 3

if 5 <= media < 7:
    print('Em recuperação.')
else:
    print('Não está em recuperação.')

#15
inishti = int(input('Digite um número inteiro para descobrir se ele é múltiplo de cinco: '))
if inishti % 5 == 0:
    print('Múltiplo de cinco')
