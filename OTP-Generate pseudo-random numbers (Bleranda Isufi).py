import random

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def encrypt(plaintext):
    
    otp = "".join(random.sample(charset, len(charset)))
    result = ""

    for c in plaintext.upper():
        if c not in otp:
            continue
        else:
            result += otp[charset.find(c)]

    return result , otp



def decrypt(ciphertext, otp):
    result = ""

    for c in ciphertext.upper():
        if c not in otp:
            continue
        else:
            result += charset[otp.find(c)]

    return result

def main():

    
            print(" OTP - Program")
            plaintext=input("Please enter your plaintext: ")
            encrypted = encrypt(plaintext)
            decrypted = decrypt(encrypted[0], encrypted[1])
            print("Ciphertext : " ,encrypted[0])
            print("Generated OTP:" ,encrypted[1])
            print("Decrypted: " + decrypted)

main()