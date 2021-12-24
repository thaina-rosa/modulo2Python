# numero = 0
# count = 0
# count1 = 0
# while numero < 999:
#     count += numero
#     numero = int(input('Digite um numero de 0 999: '))
#
#     if numero == 999:
#         break
#
#     count1 += 1
# print('A soma dos numeros {} escolhidos foi de {} '.format(count1, count))
# print('O programa se encerrou!!!')
#################################Exercicio2###############################
# count = 0
# resuldado = 0
# num = 0
# while True:
#     num = int(input('Digite um numero para a tabuada: '))
#     if num < 0:
#         break
#     # while count <= 9:
#     #     count += 1
#     for i in range(1, 11):
#         resuldado = i * num
#         print('A taboada do {} x {} = {}'.format(num, i, resuldado))
# print('O programa se encerrou!!!')

###################################Exercicio3#########################################
import random

# r = 0
# num = 0
# count = 0
# soma = 0

# while True:
#     r = random.randint(0, 10)
#     soma = r + num
#     num = int(input('Digite um numero: '))
#     escolha = str(input('Escolha entre Par [P] ou impar [I]')).upper().strip()[0]
#
#     if soma % 2 == 0 and escolha == 'P':
#         count += 1
#         print('Você ganhou {} este é um numero par!!')
#         print('Vamos jogar novamente!!!')
#
#     elif soma % 2 == 1 and escolha == 'I':
#         count += 1
#         print('Você ganhou este é um numero numero impar!!')
#         print('Vamos jogar novamente!!!')
#
# como fazer um loop se a pessoa escolher outra letra!!
#     else:
#         print('Você perdeu e o computador ganhou! e seu numero de vitorias foi de {}'.format(count))
#
#         break

#######################################Exercicio4##########################################

# count = 0
# mulher = 0
# h = 0
# while True:
#     idade = int(input('Digite sua idade: '))
#     sexo = str(input('Digite seu sexo [M/F]: ')).upper()
#     con = str(input('Deseja continuar [S/N]')).upper().strip()
#
#     if idade >= 19:
#         count += 1
#
#     if sexo == 'M' and idade > 0:
#         h += 1
#
#     elif sexo == 'F' and idade <= 19:
#         mulher += 1
#
#     if con == 'N':
#         print('O oprograma encerrou!!')
#         break
# print('O numero de pessoas com mais de 18 anos é de {}'.format(count))
# print('O numero de mulheres com menos de 20 anos é de {}'.format(mulher))
# print('O numero de homens cadastrados foi de {}'.format(h))

# quantas pessoas tem >18
# quantas pessoas sao do sexo f e tem < 20
#quantos homens cadastrados

#######################################Exercicio5################################################

#
# total = 0
# caro = 0
# count = 0
# nome = ''
# barato = 0
# while True:
#     produto = str(input('Digite o nome do produto: ')).lower()
#     preco = float(input('Digite o valor do produto: R$ '))
#     con = str(input('Deseja continuar [S/N]?: ')).upper().strip()
#     count += 1
#     total += preco
#     if preco > 1000:
#         caro += 1
#
#     elif count == 1:
#         barato = preco
#         nome = produto
#     elif preco > 0 and preco < barato:
#         barato = preco
#         nome = produto
#
#     if con == 'N':
#         print('O oprograma encerrou!!')
#         break
# print('O total gasto nas compras foi de {}'.format(total))
# print('O nome do produto mais barato que voçê comprou é {} e seu valor foi de {}'.format(nome, barato))
# print('O total de produtos que custam mais de 1000 foi de {}'.format(caro))
#
# ############################################Exercicio6###################################
#
dinheiro = int(input('Digite o valor que deseja sacar: '))
total = dinheiro
nota = 50
count = 0
while True:
    if total >= nota:
        total -= nota
        count += 1
    else:
        if count > 0:
            print(f'Total de {count} celulas de R$ {nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10

        elif nota == 10:
            nota = 1
        count = 0
        if nota == 0:
            break



