#16
xoro = int(input('Digite um número inteiro para descobrir se é par ou ímpar: '))
if xoro % 2 == 0:
	print('Par')
else:
	print('Ímpar')

#17
cópivas = int(input('Digite sua idade para saber se você é ou não maior de idade: '))

if cópivas >= 18:
	print('Maior de idade')
else:
	print('Menor de idade')
	
#18
print('Digite dois números inteiros para saber o maior entre eles.')
capricórnio = int(input())
cãncer = int(input())
ço = max(capricórnio, cãncer)

if capricórnio == cãncer:
    print('Os números são iguais.')
else:
    print(f'{ço} é o maior entre eles.')

#19
alphabetlore = int(input('Digite um número inteiro para saber se ele é negativo: '))

if alphabetlore >= 0:
	print('Não negativo')
else:
	print('Negativo')

#20
produtostoxicos = float(input('Digite sua nota para saber se você está aprovado ou reprovado: '))

if produtostoxicos >= 7:
	print('Aprovado')
else:
	print('Reprovado')

#21
rooster_fight = int(input('Digite um número inteiro para descobrir se é divisível por sete: '))
if rooster_fight % 7 == 0:
	print('Divisível por 7')
else:
	print('Não divisível por 7')

#22
ifuruguaçu = float(input('Digite seu salário para ver a taxa que será imposta nele: '))
if ifuruguaçu > 3000:
	print(f"Taxa: 15% \nSalário após imposto: R${ifuruguaçu - (ifuruguaçu * 0.15):.2f}")
else:
	print(f"Taxa: 7,5% \nSalário após imposto: R${ifuruguaçu - (ifuruguaçu * 0.075):.2f}")

#23
pinton = input("Digite a senha: ")
if pinton == "python2026":
	print("Acesso Permitido")
else:
	print("Acesso Negado")

#24
print("Digite dois números inteiros para ver a divisão entre eles.")
punch = int(input())
kun = int(input())

if kun != 0:
	print(f"A divisão entre {punch} e {kun} resulta em {punch / kun}")
else:
	print("Divisão por zero não é permitida")

#25
ran = float(input('Digite uma temperatura (em °C) para ver uma comparação entre ela e o pono de ebulição da água: '))
if ran > 100:
	print('Acima do ponto de ebulição')
else:
	print('Abaixo do ponto de ebulição')

#26
elt = int(input("Digite um número inteiro (se ele for positivo, verá o quadrado dele; caso contrário, verá o cubo): "))
if elt > 0:
	print(f'{elt}² = {elt ** 2}')
else:
		print(f'{elt}³ = {elt ** 3}')

#27
lit = int(input('Digite seu ano de nascimento para saber se está elegível para aposentadoria: '))
if 2026 - lit >= 65:
	print('Elegível para aposentadoria')
else:
	print('Não elegível ainda')

#28
print('Digite dois números inteiros para descobrir se a soma deles é grande (maior que 100) ou pequena (menor que 100).')
sadako = int(input())
kayako = int(input())

if sadako + kayako > 100:
	print('Soma grande')
else:
	print('Soma pequena')

#29
print('Digite seu peso (em quilogramas) e sua altura (em metros) para descobrir se você está acima do peso')
jóji = float(input("Peso: "))
cilindro = float(input("Altura: "))

if jóji / cilindro ** 2 < 25:
	print("Peso normal")
else:
	print("Acima do peso")

#30
print("Digite qualquer coisa aqui.")
lenda = input()
mito = len(lenda)

if mito > 5:
	print(lenda.upper())
else:
	print(lenda.lower())
