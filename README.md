# Notas de aula de 2026.1.07 - Python 05

## Informações gerais

- **Público alvo**: alunos da disciplina de **Introdução a lógica e programação** do curso de [Infoweb](https://diatinf.ifrn.edu.br/cursos/tecnico-em-informatica-para-internet/) na [DIATINF](https://diatinf.ifrn.edu.br/) no [CNAT-IFRN](https://portal.ifrn.edu.br/campus/natalcentral/)
- **Professor**: [L A Minora](https://github.com/leonardo-minora/)
- **Objetivo**:
  1. Conhecer os operadores condicionais
  2. Praticar codificação de estruturas condicionais

---
## Notas de aula [slides pdf](/05-Estruturas_de_selecao.pdf)
1. Instrução `if`, `else` e `elif`
```python
pais = input()
if pais == "Brasil":
   print("Brasília")
elif pais == "França":
   print("Paris")
elif pais == "Estados Unidos da América" or pais == "EUA":
   print("Washington")
elif pais == "Argentina":
   print("Buenos Aires")
else:
   print("Não sei :(")

```
2. Instrução se-ternário
```python
idade = 18
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)

```

---
## Exercícios [Lista de exercícios](/lista.md)
1. Escreva um programa que tem como entrada um número inteiro e imprime uma mensagem indicando se a entrada é igual ou diferente de 10.

| Exemplo de entrada | Saída esperada | 
| ------------------ | -------------- |
| 2                  | A entrada é diferente de 10 |
| 10                 | A entrada é igual a 10 |
| 0                  | A entrada é diferente de 10 |

2. Escreva um programa que tem como entrada um número inteiro e imprime uma mensagem indicando se a entrada é divisível por 2.

| Exemplo de entrada | Saída esperada | 
| ------------------ | -------------- |
| 2                  | A entrada é divisível por 2 |
| 10                 | A entrada é divisível por 2 |
| 5                  | A entrada não é divisível por 2 |

3. Escreva um programa que tem como entrada dois números inteiros e imprime uma mensagem indicando se soma das entradas resulta em um número par ou ímpar.

| Exemplo de entrada | Saída esperada | 
| ------------------ | -------------- |
| 2<br />4           | A soma das entradas é par |
| 10<br />3          | A soma das entradas é ímpar |
| 5<br />1           | A soma das entradas é par |

4. Escreva um programa que tem como entrada um número inteiro e imprime uma mensagem que indica se a entrada pertence ao intervalo [0, 6].

| Exemplo de entrada | Saída esperada | 
| ------------------ | -------------- |
| 1                  | 1 pertence ao intervalo [0, 6] |
| -5                 | -5 não pertence ao intervalo [0, 6] |
| 8                  | 8 não pertence ao intervalo [0, 6] |
| 6                  | 6 pertence ao intervalo [0, 6] |
| 0                  | 0 pertence ao intervalo [0, 6] |

5. Escreva um programa que tem como entrada dois números inteiros e imprime o maior deles.

| Exemplo de entrada | Saída esperada | 
| ------------------ | -------------- |
| 3<br />0           | 0 3            |
| 12<br />98         | 12 98          |

6. Escreva um programa que tem como entrada dois números inteiros e imprime o maior deles. Use a instrução `if`, obrigatoriamente, e `else`, opcionalmente.

| Exemplo de entrada | Saída esperada | 
| ------------------ | -------------- |
| 3<br />0           | 3              |
| 12<br />98         | 98             |

7. Escreva um programa que tem como entrada três valores inteiros e os imprime em ordem crescente. Utilize a obrigatoriamente instrução `if` com `elif` e `else`.

| Exemplo de entrada | Saída esperada | 
| ------------------ | -------------- |
| 8<br />6<br />2    | 2 6 8          |
| 3<br />2<br />1    | 1 2 3          |
| 2<br />4<br />6    | 2 4 6          |

8. Escreva um programa que tem com entrada a idade de um nadador e imprime a sua categoria, a qual é determinada pela tabela abaixo. Utilize a obrigatoriamente instrução `if` com `elif` e `else`.

| Idade            | Categoria  |
| ---------------- | ---------- |
| 5 até 7 anos     | Peixinho   |
| 8 até 10 anos    | Infantil A |
| 11 até 13 anos   | Infantil B |
| 14 até 17 anos   | Juvenil    |
| Acima de 18 anos | Adulto     |

| Exemplo de entrada | Saída esperada | 
| ------------------ | -------------- |
| 1                  | Sem categoria  |
| 6                  | Peixinho       |
| 10                 | Infantil A     |
| 11                 | Infantil B     |
| 14                 | Juvenil        |
| 20                 | Adulto         |

9. Escreva um programa que tem com entrada um valor inteiro e imprime o respectivo mês por extenso. O programa deve imprimir uma mensagem informativa caso seja informado um valor inválido. Utilize a obrigatoriamente instrução `if` com `elif` e `else`.

| Exemplo de entrada | Saída esperada | 
| ------------------ | -------------- |
| 11                 | Novembro       | 
| 3                  | Março          | 
| 18                 | Valor inválido |
