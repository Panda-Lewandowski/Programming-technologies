from base64 import b32encode, b32decode
from rsa import RSA
import sys
import random
import time
import matplotlib.pyplot as plt


if __name__ == '__main__':
        start = 0
        stop = 100 
        limit = 100
        
        bits = [128, 256, 512, 1024, 2048]
        enc_time = []
        dec_time = []

        for b in bits:
            rsa = RSA(bits=b)

            # print("\tP:", rsa.p, "\n\tQ:", rsa.q, "\n\tE:", rsa.e, "\n\tN:", rsa.n, "\n\tD:", rsa.d)

            sample = [random.randint(start, stop) for iter in range(limit)]
            # print(f"Sample: {sample}")
            start_time = time.time()
            enc_sample = rsa.encrypt_list(sample)
            enc_time.append(time.time() - start_time)
            # print(enc_sample)
            
            start_time = time.time()
            dec_enc_sample = rsa.decrypt_list(enc_sample)
            dec_time.append(time.time() - start_time)
            # print(dec_enc_sample)

            if dec_enc_sample != sample:
                raise ValueError
            
        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.plot(bits, enc_time)
        ax1.set(ylabel='time (sec)', title='Encryption')
        ax1.grid(True)

        ax2.plot(bits, dec_time)
        ax2.set(xlabel='Bits', ylabel='time (sec)', title='Decryption')
        ax2.grid(True)
        plt.show()
