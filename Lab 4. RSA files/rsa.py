import sys
from Crypto.Util import number
from random import randrange


class RSA(object):
    def __init__(self, p=None, q=None, bits=8):
        if not p:
            self.p = number.getPrime(bits)
        elif number.isPrime(p):
            self.p = p
        else:
            raise ValueError

        if not q:
            self.q = number.getPrime(bits)
        elif number.isPrime(q):
            self.q = q
        else:
            raise ValueError

        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self.get_e(self.phi, bits)
        self.d = self.get_d(self.e, self.phi)

    @staticmethod
    def get_d(e, phi):
        return number.inverse(e, phi)

    @staticmethod
    def get_e(phi, bits=192):
        # (e*d) mod fi == 1
        while True:
            result = randrange(280, 290)
            modulus = number.GCD(result, phi)
            if modulus == 1:
                return result

    @staticmethod
    def get_greatest_common_divisor(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def _crypt(self, char, key):
        '''
        С = M**e mod N
        M’ = C**d mod N
        '''
        return pow(char, key, self.n)

    def encrypt(self, byte):
        return self._crypt(byte, self.d)
        
    def decrypt(self, byte):
        return self._crypt(byte, self.e)

    def keys_to_files(self, path_to_files=''):
        with open(path_to_files + "public_key.rsa", 'w') as file:
            file.write(str(self.e))
            file.write('\n')
            file.write(str(self.n))
        with open(path_to_files + "private_key.rsa", 'w') as file:
            file.write(str(self.d))
            file.write('\n')
            file.write(str(self.n)) 

    def read_public_key(self, path_to_files=''):
        with open(path_to_files + "public_key.rsa", 'r') as file:
            self.e = int(file.readline())
            self.n = int(file.readline())
    
    def read_private_key(self, path_to_files=''):
        with open(path_to_files + "private_key.rsa", 'r') as file:
            self.d = int(file.readline())
            self.n = int(file.readline())

    