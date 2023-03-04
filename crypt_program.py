def ascii_encrypt(M):
    return(ord(M))

def encryption(M,Pc):
    Lc= M+Pc
    return Lc

def ascii_decrypt(M):
    return(chr(M))

def encrypt(Mess,cle):
    mess_crypt=""
    cle=str(cle)
    y=0
    L=len(cle)
    for i in Mess:
        if y>L:
            y=0
        mess_chiffr=ascii_encrypt(i)
        part_cle=int(y)
        lett_crypt=encryption(mess_chiffr,part_cle)
        lett_fin=ascii_decrypt(lett_crypt)
        mess_crypt+=lett_fin
        y+=1
    return mess_crypt