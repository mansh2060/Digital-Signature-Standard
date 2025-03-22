import random
from sympy import  isprime

def choose_prime(n_bits):
        while True:
            num = random.randrange(2 ** (n_bits - 1) + 1, 2 ** n_bits - 1)
            if num % 2 == 0:
                num += 1  
            if isprime(num):
                return num
            