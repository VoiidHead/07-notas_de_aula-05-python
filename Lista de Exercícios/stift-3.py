#31
kristhyan = int(input('Digite um número inteiro para saber se ele é positivo, negativo ou nulo: '))

if kristhyan > 0:
	print('Positivo')
elif kristhyan == 0:
	print('Zero')
else:
    print('Negativo')

#32
politicagem = float(input('Digite sua nota para ver seu rank: '))

if politicagem >= 9:
    print('A')
elif politicagem >= 7:
    print("B")
elif politicagem >= 5:
    print('C')
else:
    print('D')

#33
flightaway = ['Inválido', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
#Variável desnecessária, eu só fiz porque queria usar lista

flightnear = int(input('Digite um número inteiro para ver seu equivalente na semana (a contagem começa na segunda e acaba no domingo): '))
if flightnear == 1:
    print(flightaway[1])
elif flightnear == 2:
    print(flightaway[2])
elif flightnear == 3:
    print(flightaway[3])
elif flightnear == 4:
    print(flightaway[4])
elif flightnear == 5:
    print(flightaway[5])
elif flightnear == 6:
    print(flightaway[6])
elif flightnear == 7:
    print(flightaway[7])
else:
    print(flightaway[0])

#34
print('Digite seu peso (em quilogramas) e sua altura (em metros) para descobrir como você está classificado com relação ao seu peso')
jiju = float(input("Peso: "))
paralelograma = float(input("Altura: "))
subwaymoney = jiju / paralelograma ** 2

if subwaymoney < 18.5:
	print('Abaixo do peso')
elif subwaymoney < 25:
    print("Peso normal")
elif subwaymoney < 30:
	print("Acima do peso")
else:
    print('Sobrepeso')

#35
circo = float(input('Digite a velocidade de um carro (em km/h): '))
if circo <= 80:
    print('Sem multa')
elif 80 <  circo <= 100:
    print("Multa leve: R$130")
elif 100 <  circo <= 120:
    print("Multa média: R$195")
else:
    print('Multa Grave: R$293 + suspensão')

#36
quípruvs = int(input('Digite sua idade para ver a fase da vida onde você está, perante a sociedade brasileira: '))

if quípruvs < 14:
	print('Criança')
elif quípruvs < 18:
    print("Adolescente")
elif quípruvs < 60:
	print("Adulto")
else:
    print('Idoso')

#37
flugty = ['Mês inválido', 'Verão', 'Outono', 'Inverno', 'Primavera']
flogt = int(input('Digite o número de um mês para ver qual estação do ano ocorre no hemisfério sul durante esse mês: '))
if flogt == 1 or 2 or 12:
    print(flugty[1])
elif flogt == 3 or 4 or 5:
    print(flugty[2])
elif flogt == 6 or 7 or 8:
    print(flugty[3])
elif flogt == 9 or 10 or 11:
    print(flugty[4])
else:
    print(flugty[0])

#38
print('CALCULADORA DAS 4 OPERAÇÕES BÁSICAS COM DOIS NÚMEROS')
nonchalant = float(input('Primeiro número: '))
####
while True:
    nunchalant = input('Sinal: ')

    if nunchalant in ["+", "-", "*", "×", "x", ".", "·", "/", ":", "÷"]:
         break
    
    print("Operador inválido")
####
niichalant = float(input('Segundo Número: '))

if nunchalant == "+":
    print(f"Soma: {nonchalant + niichalant}")
elif nunchalant == "-":
    print(f"Diferença: {nonchalant - niichalant}")
elif nunchalant == "*" or nunchalant == "×" or nunchalant == "x" or nunchalant == "." or nunchalant == "·":
     print(f"Produto: {nonchalant * niichalant}")
elif (nunchalant == "/" or nunchalant == ":" or nunchalant =="÷") and niichalant != 0:
    print(f"Quociente: {nonchalant / niichalant}")
else:
    print('ERRO: não é possível dividir por 0!')

#39
simontar = float(input('Digite seu salário para ver o reajuste que será imposto nele e qual será o novo valor: '))
if simontar <= 1500:
    print(f"Reajuste: 15% \nSalário após reajuste: R${simontar + (simontar * 0.15):.2f}")
elif simontar <= 3000:
	print(f"Taxa: 20% \nSalário após imposto: R${simontar - (simontar * 0.10):.2f}")
elif simontar <= 6000:
    print(f"Reajuste: 7% \nSalário após reajuste: R${simontar + (simontar * 0.07):.2f}")
else:
	print(f"Taxa: 3% \nSalário após imposto: R${simontar - (simontar * 0.003):.2f}")

#40
rosht = ["a", "e", "i", "o", "u",]
risht = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
rusht = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

while True:
    lint = input('Digite um caractere para ver se ele é uma letra minúscula, um dígito ou outro: ')

    if len(lint) == 1:
        break
    
    print("Apenas um caractere é permitido")

if lint in rosht:
    print('vogal minúscula')
elif lint in risht:
    print('consoante minúscula')
elif lint in rusht:
    print('Dígito')
else:
    print('Outro caractere')

#41
print('Digite três números inteiros para vê-los em ordem crescente: ')
ryu = int(input())
ken = int(input())
dan = int(input())

if ryu > ken > dan:
    print(f'{dan} {ken} {ryu}')
elif ryu > dan > ken:
    print(f'{ken} {dan} {ryu}')
elif ken > ryu > dan:
    print(f'{dan} {ryu} {ken}')
elif ken > dan > ryu:
    print(f'{ryu} {dan} {ken}')
elif dan > ryu > ken:
    print(f'{ken} {ryu} {dan}')
elif dan > ken > ryu:
    print(f'{ryu} {ken} {dan}')
else:
     print('Os números são iguais')
    
#42
flexgt = ['Trimestre inválido', 'Janeiro, Fevereiro, Março', 'Abril, Maio, Junho', 'Julho, Agosto, Setembro', 'Outubro, Novembro, Dezembro']
flugstar = int(input('Digite o número de um trimestre (1 a 4) para ver quais meses ele contém: '))
if flugstar == 1:
    print(flexgt[1])
elif flugstar == 2:
    print(flexgt[2])
elif flugstar == 3:
    print(flexgt[3])
elif flugstar == 4:
    print(flexgt[4])
else:
    print(flexgt[0])

#43
dordecabeça = int(input('Digite sua idade para ver qual será o preço de seu ingresso no cinema: '))
if dordecabeça <= 5:
    print('Entrada gratuita')
elif dordecabeça <= 12:
    print('R$12,00')
elif dordecabeça < 17:
    print('R$18,00')
else:
    print('R$25,00')

#44
print('Digite três lados de um triângulo para ver sua classificação: ')
crossingfield = float(input('Lado A: '))
office = float(input('Lado B: '))
borgen = float(input('Lado C: '))

while True:
    if crossingfield >= office + borgen or office >= crossingfield + borgen or borgen >= crossingfield + office:
        print('Os lados não formam um triângulo. Digite os lados novamente.')
        crossingfield = float(input('Lado A: '))
        office = float(input('Lado B: '))
        borgen = float(input('Lado C: '))
    else:
        break

if crossingfield == office == borgen:
    print('Triângulo Equilátero')
elif crossingfield == office and crossingfield != borgen or crossingfield == borgen and crossingfield != office or office == borgen and office != crossingfield:
    print('Triângulo Isósceles')
else: 
    print('Triângulo Escaleno')

#45
windsofchange = ['Mês inválido', '30', '31', '28']
liebt = int(input('Digite o número de um mês para ver quantos dias ele tem num ano convencional (não bissexto): '))
if liebt == 1 or liebt == 3 or liebt == 5 or liebt == 7 or liebt == 8 or liebt == 10 or liebt == 12:
    print(windsofchange[1])
elif liebt == 4 or liebt == 6 or liebt == 9 or liebt == 11:
    print(windsofchange[2])
elif liebt == 2:
    print(windsofchange[3])
else:
    print(windsofchange[0])

#46
print('Digite dois números e um operador para realizar a operação entre eles\nOperadores: 1 = Maior entre eles \t2 = Menor entre eles \t3 = Soma \t4 = Diferença')
inex = int(input('Primeiro número: '))
monish = int(input('Segundo número: '))
####
while True:
    operator = int(input('Operador: '))

    if operator in [1, 2, 3, 4]:
         break
    
    print("Operador inválido")
####
if operator == 1:
    print(f'Maior entre eles: {max(inex, monish)}')
elif operator == 2:
    print(f'Menor entre eles: {min(inex, monish)}')
elif operator == 3:
    print(f'Soma: {inex + monish}')
else:
    print(f'Diferença: {inex - monish}')

#47
while True:
    impota = int(input('Digite uma nota de um a 100: '))
    if 1 <= impota <= 100:
        break
    print('Nota inválida')

if impota <= 49:
    print('Insuficiente')
elif impota < 70:
    print('Regular')
elif impota < 90:
    print('Bom')
else:
    print('Excelente')

#48
#olias
falsi = int(input('Digite seu consumo mensal de enrgia elétrica (em kWH) para ver quanto pagará por ele: '))

if falsi <= 100:
    print(f"Conta de Energia: R${falsi * 0.40}")
elif falsi < 201:
    print(f"Conta de Energia: R${falsi * 0.50}")
elif falsi < 301:
    print(f"Conta de Energia: R${falsi * 0.65}")
else:
    print(f"Conta de Energia: R${falsi * 0.85}")

#49
holsi = int(input("Digite um ano para ver se ele é bissexto: "))
if holsi % 400 == 0 or (holsi % 4 == 0 and not holsi % 100 == 0):
    print("Ano Bissexto")
else:
    print("Ano não bissexto")

#50
def funcenhas():
    while True:
        joint = input('Comprará algo a mais? (S/N): ')
        
        if joint in ["S", "s"]:
            olias = int(input("O que fará?\n1 = Hambúrguer\n2 = Hot-dog\n3 = Suco\n4 = Refrigerante\n5 = Sair\n"))

            if olias == 1:
                print('Você pede um hambúrguer.')
                funcenhas()
                break
            elif olias == 2:
                print('Você pede um hot-dog.')
                funcenhas()
                break
            elif olias == 3:
                print('Você pede um suco.')
                funcenhas()
                break
            elif olias == 4:
                print('Você pede um refrigerante.')
                funcenhas()
                break
            elif olias == 5:
                print("Adeus, volte sempre!")
                break
            else:
                print("Inválido")

        elif joint in ["N", "n"]:
            print("Adeus, volte sempre!")
            break
        else:
            print("Resposta inválida")

print("Você está num restaurante, o que fazer?:")
print("1 = Pedir um hambúrguer (R$18,00) \n2 = Pedir um hot-dog (R$12,00) \n3 = Pedir um suco (R$08,00) \n4 = Pedir um refrigerante (R$6,00) \n5 = Sair sem pedir nada")
####
while True:
    olias = int(input())
    if olias in [1, 2, 3, 4, 5]:
        break
    else:
        print("Inválido")
####
if olias == 1:
    print('Você pede um hambúrguer e se delicia com essa "porcaria".')
    funcenhas()
elif olias == 2:
    print('Você pede um hot-dog e se delicia com tal "porcaria".')
    funcenhas()
elif olias == 3:
    print('Você pede um suco e se delicia com sua bebida natural.')
    funcenhas()
elif olias == 4:
    print('Você pede um refrigerante e se delicia com tal "porcaria".')
    funcenhas()
elif olias == 5:
    print("Adeus, volte sempre!")
