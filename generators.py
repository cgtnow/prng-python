# -*- coding: utf-8 -*-

import random

class PRNG(object):
    """
        Pseudorandom Number Generator.
        Classe responsável por conter atributos e métodos comuns aos PRNGs

        self.seed =  semente a ser utilizada no gerador, deve ter
                origem verdadeiramente aleatória

        self.length = tamanho do número a ser gerado

    """
    def __init__(self, seed, length):
        self.seed = seed
        self.length = length


    """
        Retorna uma lista de números primos até o valor 'max'
        utilizando o metodo de Crivo de Eratóstenes
    """
    def get_list_of_primes(self, max):
        primes = list()
        not_primes = list()
        for i in range(2, max + 1):
            if i not in not_primes:
                primes.append(i)
                for j in range(i * i, max + 1, i):
                    not_primes.append(j)
        return primes


    """
        Verifica se os valores v1 e v2 são coprimos entre si
    """
    def are_coprimes(self, v1, v2):
        while v2 != 0:
            v1, v2 = v2, (v1 % v2)
        return v1 == 1

class BBS(PRNG):
    """
        Algoritmo Blum Blum Shub.
        Herda classe pai PRNG.
    """
    def __init__(self, seed, length):
        super(BBS, self).__init__(seed, length)

    """
        Método utilizado para geração de n, que é produto
        da multiplicação dos números primos p e q.

        Faz verificações de modulo 4 == 3, valor maior que um
        threshold (utilizado para gerar números grandes), além
        de verificar se p e q são coprimos entre si.
    """
    def get_n(self):
        # valor minimo para o valor de p e q
        threshold = 7000
        # retorna uma lista de números primos até 100000
        primes = self.get_list_of_primes(10000)
        while True:
            p = random.choice(primes)
            # faz verificações do número escolhido
            if (((p % 4) == 3) and p > threshold):
                break
        while True:
            q = random.choice(primes)
            # faz verificações do número escolhido
            if (((q % 4) == 3) and q > threshold):
                # faz a verificação de co-primos
                if ((p != q) and self.are_coprimes(self.seed, p*q)):
                    break
        return p * q


    """
        Método utilizado para gerar efetivamente o número
        pseudoaleatório.

        is_default indica se devem ser utilizados os valores
        setados anteriormente p e q, onde p = 70891 e q = 85247.
        Caso o valor seja falso, utiliza a função get_n() para
        gerar os valores de p e q, aumentando a complexidade do
        algoritmo.

        Efetiva cada passo da execução do algoritmo

    """
    def generate_number(self, is_default=True):
        if is_default:
            p = 70891
            q = 85247
            n = p * q
        else:
            n = self.get_n()
        x = list()
        b = list()
        x.append((self.seed ** 2) % n) # atribuição de x[0]
        for i in range(self.length):
            # atribuição de Xi de acordo com algoritmo
            x.append((x[-1]**2) % n)
            # atribuição de Bi de acordo com algoritmo
            b.append(x[-1] % 2)
        # Agrupa valores de Bi como uma string para
        # setar self.generated_number, variável onde
        # estará armazenado o número pseudoaleatório
        # final gerado.
        self.generated_number = ''.join(map(str, b))
        return True


class LCG(PRNG):
    """
        Algoritmo Linear Congruential Generator.
        Herda classe pai PRNG.

        Faz todas as verificações de acordo com as regras
        do algoritmo para as variáveis m, a, c e x0.

        length e x0 serão atribuidas aos atributos herdados
        da classe PRNG self.length e self.seed.
    """
    def __init__(self, length, m, a, c, x0):
        if m <= 0:
            raise ValueError('m must be > 0')
        if a <= 0:
            raise ValueError('a must be > 0')
        if a >= m:
            raise ValueError('a must be < m')
        if c < 0:
            raise ValueError('c must be >= 0')
        if c >= m:
            raise ValueError('c must be < m')
        if x0 < 0:
            raise ValueError('x0 must be >= 0')
        if c >= m:
            raise ValueError('x0 must be < m')
        self.m = m
        self.a = a
        self.c = c
        super(LCG, self).__init__(x0, length)


    """
        Gera efetivamente o número pseudo-aleatório através
        do algoritmo equivalente e os atributos configurados
        no construtor da classe.
    """
    def generate_number(self):
        x = list()
        # Adiciona a semente 'seed' ao valor inicial de X
        x.append(self.seed)
        # De acordo com o tamanho desejado, gera os valores
        # que devem ser concatenados
        for i in range(self.length):
            # Adiciona em X o calculo ((a*X(n-1) + c) mod m))
            # de acordo com regras do algoritmo
            x.append((self.a * x[-1] + self.c) % self.m)
        # armazena o número pseudo-aleatório gerado na variável
        # self.generated_number
        self.generated_number = ''.join(map(str,x))



class MT(PRNG):
    """
        Algoritmo Mersenne Twister.

    """
    def __init__(self, seed):
        super(MT, self).__init__(seed)
