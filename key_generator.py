import random
import math

mess_crypt=""

def is_primary(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def random_primary():
    while True:
        n = random.randint(100, 10000)
        if is_primary(n):
            return n

def cle_publique(prv1,prv2):
    publ=prv1*prv2
    return publ