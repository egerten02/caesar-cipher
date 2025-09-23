import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt():
    global alphabet
    key = random.randint(1, 25)
    message = input("\nEnter the message\n>")
    message = message.lower()
    ciphered = ''

    for i in message:
        if i == ' ':
            ciphered += ' '
        else:
            index = (alphabet.index(i) + key) % 26
            ciphered += alphabet[index]
    print(ciphered, key)

def decrypt():
    global alphabet
    enc_msg = input("\nEnter ciphered message\n>")

    for key in range(1, 26):
        dec_msg = ''
        for i in enc_msg:
            if i == ' ':
                dec_msg += ' '
            else:
                index = alphabet.index(i) - key
                dec_msg += alphabet[index]
        print(key, dec_msg, sep=': ')

def main():
    caesar = input("(e)ncrypt or (d)ecrypt?\n>")
    if caesar == 'e':
        try:
            encrypt()
        except ValueError:
            print("\nType only letters")
    elif caesar == 'd':
        try:
            decrypt()
        except ValueError:
            print("\nType only letters")
    else:
        print("\nType 'e' or 'd'")

main()