from rsa import RSA


class FileCryptor:
    def __init__(self, bits=8):
        self.rsa = RSA(bits=bits)
        self.bits = bits
   
    def _bitstring_to_bytes(self, s):
        return int(s, 2).to_bytes(len(s) // 8, byteorder='big')
    
    def _encrypt_chunk(self, chunk):
        enc = self.rsa.encrypt(int.from_bytes(chunk, "big"))
        to_add = self.bits * 2 - enc.bit_length() 
        bit_enc = '0' * to_add + str(bin(enc))[2:] 
        return self._bitstring_to_bytes(bit_enc)

    def _decrypt_chunk(self, chunk):
        dec = self.rsa.decrypt(int.from_bytes(chunk, "big"))
        if dec == 0:
            return b'\x00'
        return dec.to_bytes((dec.bit_length() + 7) // 8, 'big')

    def encrypt(self, filename):
        with open(filename, 'rb') as file, open(filename + '.enc', 'wb') as enc_file:
            chunk = file.read(self.bits // 8)
            while chunk != b"":
                enc_chunk = self._encrypt_chunk(chunk)
                enc_file.write(enc_chunk)
                chunk = file.read(self.bits // 8)
                
    def decrypt(self, filename):
        with open(filename, 'rb') as file, open(filename + '.dec', 'wb') as dec_file:
            chunk = file.read(self.bits * 2 // 8)
            while chunk != b"":
                dec_file.write(self._decrypt_chunk(chunk))
                chunk = file.read(self.bits * 2 // 8)


if __name__ == '__main__': 
    cryptor = FileCryptor()
    cryptor.encrypt('Piet.png')
    cryptor.decrypt('Piet.png.enc')