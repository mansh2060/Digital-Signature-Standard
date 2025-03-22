from key_signature_generator import KeySignatureGenerator
from hash_generation import HashGeneration
from choose_prime import choose_prime

class SignatureVerification:
    def __init__(self, text, n_bits):
        self.text = text
        self.n_bits = n_bits
        self.prime_number = choose_prime(n_bits)
        key_signature_generator = KeySignatureGenerator(text, self.prime_number)
        self.first_signature, self.second_signature = key_signature_generator.output_signature()
        self.p, self.q, self.g, self.y = key_signature_generator.public_key()
        hash_generation = HashGeneration(self.text)
        self.hash_code = hash_generation.gen_hash()

    def check_signature_validity(self):
        if 0 < self.first_signature < self.q and 0 < self.second_signature < self.q:
            return "Valid"
        return "Invalid"

    def compute_hash(self):
        return self.hash_code

    def intermediate_values(self):
        try:
            w = pow(self.second_signature, -1, self.q)  
        except ValueError:
            print("Error: second_signature is not invertible mod q!")
            return None

        u1 = (self.hash_code * w) % self.q
        u2 = (self.first_signature * w) % self.q
        v = ((pow(self.g, u1, self.p) * pow(self.y, u2, self.p)) % self.p) % self.q
        return v

    def output_validation(self):
        v = self.intermediate_values()
        if v is None:
            return "Error in computing intermediate values"
        if v == self.first_signature:
            print("Validation Successful:", v, self.first_signature)
            return "Valid"
        else:
            print("Validation Failed:", v, self.first_signature)
            return "Invalid"

