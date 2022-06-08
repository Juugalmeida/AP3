# coding=utf-8

"""

# Projeto AP2

# Fase 2


1) Operações: soma, subtração, multiplicação e divisão;
2) Utilização apenas de números inteiros pertencentes ao conjunto dos Reais;
3) Resultados negativos serão válidos;
4) Utilização de dois números por problema, sendo:
 - soma e subtração -> o primeiro e o segundo número terão até dois dígitos;
 - multiplicação e divisão -> o primeiro número terá dois dígitos e o 2º número terá um dígito;
 - divisão -> serão gerados apenas problemas cujo resultado tenha resto zero;
5) Número de questões: 5
6) Tempo da fase: 2 minutos

"""

import random
import time
import time_fase1 as f1
import fase3 as f3


def step2_func():
    print('FASE 2')
    initime = time.time()
    for i in range(5):
        operacao = random.choice('+-x/')
        n1 = random.randint(0, 99)
        n2 = random.randint(0, 99)
        n3 = random.randint(10, 99)
        n4 = random.randint(1, 9)

        if operacao == '+':
            print('{} {} {}'.format(n1, operacao, n2))
            solucao = n1 + n2

        elif operacao == '-':
            print('{} {} {}'.format(n1, operacao, n2))
            solucao = n1 - n2

        elif operacao == 'x':
            print('{} {} {}'.format(n3, operacao, n4))
            solucao = n3 * n4

        else:
            while n3 % n4 != 0:
                n3 = random.randint(10, 99)
                n4 = random.randint(1, 9)
            print('{} {} {}'.format(n3, operacao, n4))
            solucao = n3 / n4

        resposta_aluno = int(input('Resposta: '))
        contador = 1
        while resposta_aluno != solucao and contador != 3:
            print('Tente novamente!')
            resposta_aluno = int(input('Resposta: '))
            contador = contador + 1;

        if contador == 3:
                i = 0
                print('Você não acertou, voltou para o início do jogo !')

    fim = time.time()
    dur = fim - initime
    if dur <= 120:
        print("Tempo gasto: {:.2f} segundos.".format(dur))
        print("Parabéns! Você passou para a fase 3.")
        f3.step3_func()
    else:
        print('Tempo gasto: {:.2f} segundos.'.format(dur))
        print("Tempo esgotado. Retorne para a fase 1")
        f1.step1_func()

    print('Parabéns!!!')
