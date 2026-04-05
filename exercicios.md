# Exercícios — Estruturas de Seleção em Python

> **Público alvo**: alunos da disciplina de Introdução a Lógica e Programação  
> **Objetivo**: praticar o uso de `if`, `if/else` e `if/elif/else`

---

## Parte 1 — Somente `if`

**1.** Leia um número inteiro. Se ele for positivo, exiba a mensagem `"O número é positivo"`.

**2.** Leia a idade de uma pessoa. Se ela for maior ou igual a 18, exiba `"Você é maior de idade"`.

**3.** Leia dois números inteiros. Se o primeiro for maior que o segundo, exiba `"O primeiro número é maior"`.

**4.** Leia um número inteiro. Se ele for par, exiba `"O número é par"`.

**5.** Leia a nota de um aluno (0 a 10). Se a nota for maior ou igual a 7, exiba `"Aprovado"`.

**6.** Leia um número real que representa a temperatura em graus Celsius. Se a temperatura for maior que 37.5, exiba `"Febre detectada"`.

**7.** Leia o nome de um usuário. Se o nome tiver mais de 10 caracteres, exiba `"Nome muito longo"`.

**8.** Leia um número inteiro. Se ele for divisível por 3, exiba `"Divisível por 3"`.

**9.** Leia dois números inteiros `a` e `b`. Se `a` for igual a `b`, exiba `"Os números são iguais"`.

**10.** Leia um número inteiro. Se ele for negativo, multiplique-o por `-1` e exiba o resultado com a mensagem `"Valor absoluto:"`.

**11.** Leia um número inteiro. Se ele for divisível tanto por 2 quanto por 3, exiba `"Divisível por 2 e por 3"`.

**12.** Leia uma palavra. Se ela começar com a letra `"a"` (maiúscula ou minúscula), exiba `"A palavra começa com A"`.

**13.** Leia a velocidade de um carro (km/h). Se a velocidade for maior que 80, exiba `"Acima do limite de velocidade"`.

**14.** Leia três notas de um aluno. Calcule a média. Se a média for maior ou igual a 5 e menor que 7, exiba `"Em recuperação"`.

**15.** Leia um número inteiro. Se ele for múltiplo de 5, exiba `"Múltiplo de 5"`.

---

## Parte 2 — `if` e `else`

**16.** Leia um número inteiro. Se ele for par, exiba `"Par"`; caso contrário, exiba `"Ímpar"`.

**17.** Leia a idade de uma pessoa. Se ela for maior ou igual a 18, exiba `"Maior de idade"`; caso contrário, exiba `"Menor de idade"`.

**18.** Leia dois números inteiros. Exiba o maior deles. Se forem iguais, exiba `"Os números são iguais"`.

**19.** Leia um número real. Se ele for positivo ou zero, exiba `"Não negativo"`; caso contrário, exiba `"Negativo"`.

**20.** Leia a nota de um aluno (0 a 10). Se a nota for maior ou igual a 7, exiba `"Aprovado"`; caso contrário, exiba `"Reprovado"`.

**21.** Leia um número inteiro. Se ele for divisível por 7, exiba `"Divisível por 7"`; caso contrário, exiba `"Não divisível por 7"`.

**22.** Leia o salário de uma pessoa. Se o salário for maior que 3000, calcule e exiba o imposto de 15%; caso contrário, calcule e exiba o imposto de 7.5%.

**23.** Leia uma senha digitada pelo usuário. Compare com a senha `"python2026"`. Se for correta, exiba `"Acesso permitido"`; caso contrário, exiba `"Acesso negado"`.

**24.** Leia dois números reais. Calcule e exiba a divisão do primeiro pelo segundo. Se o segundo for zero, exiba `"Divisão por zero não é permitida"`.

**25.** Leia uma temperatura em Celsius. Se for maior que 100, exiba `"Acima do ponto de ebulição"`; caso contrário, exiba `"Abaixo do ponto de ebulição"`.

**26.** Leia um número inteiro. Se o número for maior que 0, exiba seu quadrado; caso contrário, exiba seu cubo.

**27.** Leia o ano de nascimento de uma pessoa. Se a pessoa tiver 65 anos ou mais em 2026, exiba `"Elegível para aposentadoria"`; caso contrário, exiba `"Não elegível ainda"`.

**28.** Leia dois números inteiros. Se a soma deles for maior que 100, exiba `"Soma grande"`; caso contrário, exiba `"Soma pequena"`.

**29.** Leia o peso e a altura de uma pessoa e calcule o IMC (peso / altura²). Se o IMC for menor que 25, exiba `"Peso normal"`; caso contrário, exiba `"Acima do peso"`.

**30.** Leia uma string. Se ela tiver mais de 5 caracteres, exiba a string em maiúsculas; caso contrário, exiba-a em minúsculas.

---

## Parte 3 — `if`, `elif` e `else`

**31.** Leia um número inteiro. Se for positivo, exiba `"Positivo"`; se for negativo, exiba `"Negativo"`; se for zero, exiba `"Zero"`.

**32.** Leia a nota de um aluno (0 a 10) e exiba o conceito:
- Nota ≥ 9: `"A"`
- Nota ≥ 7: `"B"`
- Nota ≥ 5: `"C"`
- Nota < 5: `"D"`

**33.** Leia um número inteiro de 1 a 7 representando um dia da semana e exiba o nome do dia correspondente (1 = Segunda, 2 = Terça, …, 7 = Domingo). Se o valor estiver fora do intervalo, exiba `"Dia inválido"`.

**34.** Leia o IMC de uma pessoa e classifique:
- IMC < 18.5: `"Abaixo do peso"`
- IMC < 25: `"Peso normal"`
- IMC < 30: `"Sobrepeso"`
- IMC ≥ 30: `"Obesidade"`

**35.** Leia a velocidade de um carro e exiba a multa correspondente:
- Velocidade ≤ 80 km/h: `"Sem multa"`
- Velocidade ≤ 100 km/h: `"Multa leve: R$ 130"`
- Velocidade ≤ 120 km/h: `"Multa média: R$ 195"`
- Velocidade > 120 km/h: `"Multa grave: R$ 293 + suspensão"`

**36.** Leia a idade de uma pessoa e exiba a categoria:
- Idade < 12: `"Criança"`
- Idade < 18: `"Adolescente"`
- Idade < 60: `"Adulto"`
- Idade ≥ 60: `"Idoso"`

**37.** Leia o mês (1 a 12) e exiba a estação do ano correspondente no hemisfério sul:
- Meses 12, 1, 2: `"Verão"`
- Meses 3, 4, 5: `"Outono"`
- Meses 6, 7, 8: `"Inverno"`
- Meses 9, 10, 11: `"Primavera"`
- Valor fora do intervalo: `"Mês inválido"`

**38.** Leia dois números e um operador (`+`, `-`, `*`, `/`). Realize a operação correspondente e exiba o resultado. Se o operador for `/` e o divisor for 0, exiba mensagem de erro. Se o operador for inválido, exiba `"Operador inválido"`.

**39.** Leia o salário de um funcionário e calcule o reajuste:
- Salário ≤ 1500: reajuste de 15%
- Salário ≤ 3000: reajuste de 10%
- Salário ≤ 6000: reajuste de 7%
- Salário > 6000: reajuste de 3%

Exiba o novo salário.

**40.** Leia um caractere e informe se é:
- Uma vogal minúscula (`a`, `e`, `i`, `o`, `u`)
- Uma consoante minúscula (qualquer outra letra de `a` a `z`)
- Um dígito (`0` a `9`)
- Outro caractere

**41.** Leia três números inteiros e exiba-os em ordem crescente usando apenas estruturas de seleção.

**42.** Leia o número de um trimestre (1 a 4) e exiba os meses correspondentes:
- Trimestre 1: `"Janeiro, Fevereiro, Março"`
- Trimestre 2: `"Abril, Maio, Junho"`
- Trimestre 3: `"Julho, Agosto, Setembro"`
- Trimestre 4: `"Outubro, Novembro, Dezembro"`
- Outro valor: `"Trimestre inválido"`

**43.** Um cinema cobra ingressos de acordo com a idade:
- Crianças até 5 anos: gratuito
- De 6 a 12 anos: R$ 12,00
- De 13 a 17 anos: R$ 18,00
- 18 anos ou mais: R$ 25,00

Leia a idade e exiba o valor do ingresso.

**44.** Leia três lados de um triângulo. Verifique primeiro se formam um triângulo válido (cada lado deve ser menor que a soma dos outros dois). Se válido, classifique como:
- `"Equilátero"` (três lados iguais)
- `"Isósceles"` (dois lados iguais)
- `"Escaleno"` (todos os lados diferentes)

**45.** Leia o número de um mês (1 a 12) e exiba quantos dias ele possui, considerando que o ano é não bissexto. Se o valor for inválido, exiba `"Mês inválido"`.

**46.** Leia dois números inteiros e uma operação:
- `1` para encontrar o maior
- `2` para encontrar o menor
- `3` para calcular a soma
- `4` para calcular a diferença

Exiba o resultado ou `"Opção inválida"` se a opção não existir.

**47.** Leia uma nota de 0 a 100 (inteiro) e classifique:
- 90 a 100: `"Excelente"`
- 70 a 89: `"Bom"`
- 50 a 69: `"Regular"`
- 0 a 49: `"Insuficiente"`
- Fora do intervalo: `"Nota inválida"`

**48.** Leia o consumo mensal de energia elétrica (em kWh) de uma residência e calcule o valor da conta conforme a tabela:
- Até 100 kWh: R$ 0,40 por kWh
- De 101 a 200 kWh: R$ 0,50 por kWh
- De 201 a 300 kWh: R$ 0,65 por kWh
- Acima de 300 kWh: R$ 0,85 por kWh

Exiba o valor total a pagar.

**49.** Leia o ano e informe se é bissexto ou não. Um ano é bissexto se:
- For divisível por 400, **ou**
- For divisível por 4 **e não** divisível por 100.

Exiba `"Ano bissexto"` ou `"Ano não bissexto"`.

**50.** Crie um mini menu de uma lanchonete. Leia a opção escolhida:
- `1` — Hambúrguer: R$ 18,00
- `2` — Hot-dog: R$ 12,00
- `3` — Suco: R$ 8,00
- `4` — Refrigerante: R$ 6,00
- `5` — Sair sem pedir

Leia a quantidade desejada para a opção escolhida e exiba o total a pagar. Se a opção for inválida, exiba `"Opção inválida"`.
