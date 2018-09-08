import random

class PRNG(object):
    """
        Pseudorandom Number Generator.

    """
    def __init__(self, seed, length, generated_number=None):
        self.seed = seed
        self.length = length

    def get_list_of_primes(self, max):
        primes = list()
        not_primes = list()
        for i in range(2, max + 1):
            if i not in not_primes:
                primes.append(i)
                for j in range(i * i, max + 1, i):
                    not_primes.append(j)
        return primes


    def are_coprimes(self, v1, v2):
        while v2 != 0:
            v1, v2 = v2, (v1 % v2)
        return v1 == 1

class BBS(PRNG):
    """
        Algoritmo Blum Blum Shub.

    """
    def __init__(self, seed, length):
        super(BBS, self).__init__(seed, length)

    # n é p * q
    def get_n(self):
        threshold = 100
        primes = self.get_list_of_primes(1000)
        while True:
            p = random.choice(primes)
            if (((p % 4) == 3) and p > threshold):
                break
        while True:
            q = random.choice(primes)
            if (((q % 4) == 3) and q > threshold):
                if ((p != q) and self.are_coprimes(self.seed, p*q)):
                    break
        return p * q


    def generate_number(self):
        n = self.get_n()
        x = list()
        b = list()
        x.append((self.seed ** 2) % n)
        for i in range(self.length):
            x.append((x[-1]**2) % n)
            b.append(x[-1] % 2)
        self.generated_number = ''.join(map(str, b))
        return True


class LCG(PRNG):
    """
        Algoritmo Linear Congruential Generator.

    """
    def __init__(self, seed):
        super(LCG, self).__init__(seed)

class MT(PRNG):
    """
        Algoritmo Mersenne Twister.

    """
    def __init__(self, seed):
        super(MT, self).__init__(seed)
