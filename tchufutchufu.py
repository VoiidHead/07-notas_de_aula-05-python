#1
osbotivarios = int(input('Digite um número inteiro para saber se ele é igual ou diferente de 10: '))

if osbotivarios == 10:
	print(f'{osbotivarios} é igual a 10.')
else:
	print(f'{osbotivarios} é diferente de 10.')


#2
resenha = int(input('Digite um número inteiro para descobrir se é divisível por dois: '))
if resenha % 2 == 0:
	print(f'{resenha} é divisível por dois.')
else:
	print(f'{resenha} não é divisível por dois.')


#3
print('Digite dois números inteiros para descobrir se a soma deles é par ou ímpar.')
risonha = int(input())
rosinha = int(input())
rôsis = risonha + rosinha

if rôsis % 2 == 0:
	print(f'{rôsis} é par.')
else:
	print(f'{rôsis} é ímpar.')


#4
empiricamente_pensado = int(input('Digite um número inteiro para saber se ele se encontra no intervalo [0, 6]: '))


if 0 <= empiricamente_pensado <= 6:
		print(f"{empiricamente_pensado} está no intervalo [0, 6].")
else:
		print(f"{empiricamente_pensado} não está no intervalo [0, 6].")


#5
print('Digite dois números inteiros para ver-los organizados em ordem crescente.')
awish_anuh = int(input())
iuwanmi = int(input())
berrebith = [awish_anuh, iuwanmi]
berrebith.sort()

print(berrebith)


#6
print('Digite dois números inteiros para ver o maior entre eles.')
teclagem = int(input())
teclada = int(input())
mox = max(teclagem, teclada)

print(f'{mox} é o maior dentre eles.')


#7
print('Digite três números inteiros para ver-los organizados em ordem crescente.')
pichu = int(input())
cat = int(input())
charmander = int(input())
stardew = [pichu, cat, charmander]
stardew.sort()

print(stardew)

#8
slf = int(input("Digite a idade de um nadador para saber em que categoria etária ele se encaixa: "))
if 5 <= slf <= 7:
	print('Peixinho')
elif 8 <= slf <= 10:
	print('Infantil A')
elif 11 <= slf <= 13:
	print('Infantil B')
elif 14 <= slf <= 17:
	print('Juvenil')
elif slf >= 18:
	print('Adulto')
else:
	print("Nadador Desclassificado")


#9
monti = int(input('Digite um número para ver seu mês equivalente: '))
if monti == 1:
	print('Janeiro')
elif monti == 2:
	print('Fevereiro')
elif monti == 3:
	print('Março')
elif monti == 4:
	print('Abril')
elif monti == 5:
	print('Maio')
elif monti == 6:
	print('Junho')
elif monti == 7:
	print('Julho')
elif monti == 8:
	print('Agosto')
elif monti == 9:
	print('Setembro')
elif monti == 10:
	print('Outubro')
elif monti == 11:
	print('Novembro')
elif monti == 12:
	print('Dezembro')
else:
	print('Número inválido')
