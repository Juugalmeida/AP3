# coding=utf-8
import random
import time
import fase2 as f2


def step1_func():
    print('FASE 1')
    inicio = time.time()
    for i in range(5):

        operacao = random.choice('+-')
        n1 = random.randint(0, 99)
        n2 = random.randint(0, 99)

        print('{} {} {}'.format(n1, operacao, n2))
        if operacao == '+':
            solucao = n1 + n2

        else:
            solucao = n1 - n2

        resposta_aluno = int(input('Resposta: '))
        contador = 1
        while resposta_aluno != solucao and contador != 3:
              print('Tente novamente!')
              resposta_aluno = int(input('Resposta: '))
              contador = contador +1;
        if contador == 3:
            i = 0
            print('Você não acertou, voltou para o início do jogo !')

    fim = time.time()
    duracao = fim - inicio

    if duracao <= 120:
        print("Tempo gasto: {:.2f} segundos.".format(duracao))
        print("Parabéns! Você passou para a fase 2.")
        f2.step2_func()
    else:
        print('Tempo gasto: {:.2f} segundos.'.format(duracao))
        print("Tempo esgotado. Retorne para a fase 1.")
        step1_func()
