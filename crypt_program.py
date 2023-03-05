def ascii_encrypt(lett):
    return(ord(lett))

def encryption(lett,Part_key):
    crypt_lett= lett+Part_key
    return crypt_lett

def decryption(lett,Part_key):
    uncrypt_lett= lett-Part_key
    return uncrypt_lett

def ascii_decrypt(lett):
    return(chr(lett))

def encrypt(Mess,key):
    crypted_mess=""
    key=str(key)
    z=0
    for i in Mess:
        if z>=len(key):
            z=0
        part_key=int(key[z])
        ascii_mess=ascii_encrypt(i)
        crypt_lett=encryption(ascii_mess,part_key)
        final_lett=ascii_decrypt(crypt_lett)
        crypted_mess+=final_lett
        z+=1
    return crypted_mess

def decrypt(Mess,key):
    decrypted=""
    key=str(key)
    z=0
    for i in Mess:
        if z>=len(key):
            z=0
        part_key=int(key[z])
        ascii_mess=ascii_encrypt(i)
        uncrypt_lett=decryption(ascii_mess,part_key)
        final_lett=ascii_decrypt(uncrypt_lett)
        decrypted+=final_lett
        z+=1
    return decrypted
