import random
from sympy import primefactors, mod_inverse
from hash_generation import HashGeneration

class KeySignatureGenerator:
    def __init__(self, text, prime_number):
        self.p = prime_number
        self.text = text
        hash_generation = HashGeneration(text)
        self.hash_code = hash_generation.gen_hash()
        self.h = random.randint(2, self.p - 2)  
        self.q = self.find_prime_divisors()
        self.g = self.generator()
        self.private_key = random.randint(1, self.q - 1)  
        self.k = None  
        self.r = None  

    def find_prime_divisors(self):
        return max(primefactors(self.p - 1))  

    def generator(self):
        upper_sub = (self.p - 1) // self.q
        return pow(self.h, upper_sub, self.p)

    def public_key(self):
        y = pow(self.g, self.private_key, self.p)
        return self.p, self.q, self.g, y

    def choose_random(self):
        k = random.randint(2, self.q - 1) 
        while not mod_inverse(k, self.q):  
            k = random.randint(2, self.q - 1)
        return k

    def first_signature(self):
        self.k = self.choose_random() 
        self.r = pow(self.g, self.k, self.p) % self.q  
        if self.r == 0:
            return self.first_signature()  
        return self.r

    def second_signature(self):
        k_inv = mod_inverse(self.k, self.q)  
        s = (k_inv * (self.hash_code + self.private_key * self.r)) % self.q
        if s == 0:
            return self.second_signature()  
        return s

    def output_signature(self):
        return self.first_signature(), self.second_signature()
