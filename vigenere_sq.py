from sys import exit

def vigenere_header(alphabet):
    return list(' ') + list(alphabet)

def vigenere_sq(alphabet):
    alpha = list(alphabet)
    sq_list = [vigenere_header(alphabet)]
    for i in range(len(alpha)):
        sq_list.append(list(alphabet[i]) + alpha[i:] + alpha[:i])
    return sq_list

def vigenere_sq_print(sq_list):
    for i, row in enumerate(sq_list):
        print(f"| {' | '.join(row)} |")
        if i == 0:
            print(f"{'|---'*len(row)}|")

def letter_to_index(letter, alphabet):
    return alphabet.index(letter)

def index_to_letter(index:int, alphabet:str):
    if 0 <= index < len(alphabet):
        return alphabet[index]
    return ''

def vigenere_index(key_letter, plaintext_letter, alphabet):
    return (letter_to_index(key_letter, alphabet) +
            letter_to_index(plaintext_letter, alphabet)) % len(alphabet)

def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    return (letter_to_index(cipher_letter, alphabet) -
            letter_to_index(key_letter, alphabet)) % len(alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = []
    counter = 0
    for c in plaintext:
        if c == " ":
            cipher_text.append(' ')
        elif c in alphabet:
            cipher_text.append(index_to_letter(vigenere_index(key[counter % len(key)], c, alphabet), alphabet))
            counter += 1
    return ''.join(cipher_text)

def decrypt_vigenere(key, cipher_text, alphabet):
    paintext = []
    counter = 0
    for c in cipher_text:
        if c == " ":
            paintext.append(' ')
        elif c in alphabet:
            paintext.append(index_to_letter(undo_vigenere_index(key[counter % len(key)], c, alphabet), alphabet))
            counter += 1
    return ''.join(paintext)

def add_key(key_list:list, alphabet):
    while True:
        new_key = input("Enter a new key: ").upper()
        print(new_key)
        if any(i not in alphabet for i in new_key):
            print("Improper key, use only letters in the alphabet")
        else:
            key_list.append(new_key)
            break

def enc_menu(key, alphabet, encrypted_list):
    plaintext = input("Enter text for encryption: ").upper()

    if len(encrypted_list) > 0:
        #key_id cycles through the key list according to the last key used
        key_id = ((encrypted_list[(len(encrypted_list) - 1)][1]) + 1) % len(key)
        encrypted_list.append([(encrypt_vigenere(key[key_id], plaintext, alphabet)), key_id])
    else:
        encrypted_list.append([encrypt_vigenere(key[0], plaintext, alphabet), 0])

def dec_menu(key, alphabet, encrypted_list):
    for i in range(len(encrypted_list)):
        key_id = encrypted_list[i][1]
        print(decrypt_vigenere(key[key_id], ''.join(encrypted_list[i][0]), alphabet))

def dec_dump_menu(encrypted_list):
    for i in range(len(encrypted_list)):
        print(''.join(encrypted_list[i][0]))

def main():
    encrypted_list = []
    key_list = ['BLUESMURF']
    #key = 'BLUESMURF'
    #message = 'ONE SMALL STEP FOR MAN, ONE GIANT LEAP FOR MANKIND.'
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    menu = [
        ['1) Encrypt', enc_menu, [key_list, alphabet, encrypted_list]],
        ['2) Decrypt', dec_menu, [key_list, alphabet, encrypted_list]],
        ['3) Dump Decrypt', dec_dump_menu, [encrypted_list]],
        ['4) Add Key', add_key, [key_list, alphabet]],
        ['5) Exit Program', exit, [0]]
        ]

    while True:
        for menu_item in menu:
            print(menu_item[0])
        print(encrypted_list)
        try:
            choice = int(input("Enter a selection"))
            if not (0 < choice <= len(menu)):
                print("Improper choice, make a selection of 1-" + str(len(menu)))
            else:
                menu[choice-1][1](*menu[choice-1][2])
        except ValueError as ve:
            print("Improper choice, make a selection of 1-" + str(len(menu)))


'''
for _ in range(3):
    encrypted_list.append(menu[0][1](*menu[0][2]))

    menu[2][1](*menu[2][2])
    menu[1][1](*menu[1][2])
    menu[3][1](*menu[3][2])
    '''

if __name__ == '__main__':
    main()