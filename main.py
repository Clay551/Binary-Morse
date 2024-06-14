from pystyle import Colors, Colorate
from colorama import Fore , init
import pyfiglet
import colorama
import re
import os
from tqdm import tqdm 
import time 
MORSE_CODE_DICT = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',

                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
PREG_MATCH = "[a-z0-9,=*_&^%$#@!<>""'`~]"
BINARY_PREG_MATCH = "[a-z2-9,=*_&^%$#@!<>""'`~]"
MORSE_PREG_MATCH = "[,=*_&^%$#@!<>""'`~]"


def en_to_morse(text):
    cipher = ""
    for letter in text:
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            cipher += " "
    return cipher

def morse_to_en(text):
    text += " "
    decipher = ""
    citext = ""
    for letter in text:
        if letter != " ":
            i = 0
            citext += letter
        else:   
            i += 1
            if i == 2:
                decipher += " "
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ""
    return decipher
os.system(f'cls' if {os.name} == 'nt' else 'clear')
# TITLE
print(colorama.Fore.RED)
pyfiglet.print_figlet("Asylum")
info = colorama.Fore.GREEN + "If Input Is Empty, Press 'Enter' to Exit"

print(info)
print(colorama.Fore.RESET)

question = input(colorama.Fore.BLUE+"Translate Chi Ro Mikhay? <morse code>,<binary>,<english> : ")

print(colorama.Fore.RESET)
# ENGLISH TO BINARY
if re.match("english", question):
    en = input("Matn Ro Vared Kon==> ")
    if (en == ""):
        print("Nothing inputed, restarting...")
    else:
     binary = " ".join(format(ord(c), "b") for c in en)
     ones = binary.count("1")
     zeros = binary.count("0")
     answer = colorama.Fore.CYAN+ binary
    
     print(colorama.Fore.RED + answer)
     print('')
     print(f"Ones: {ones}")
     print(f"Zeros: {zeros}")
     print(f"{ones + zeros} characters")

# BINARY TO ENGLISH
if re.match("binary", question):
    binary = input("Binary==> ")
    if re.match(BINARY_PREG_MATCH, binary):
        ERR = colorama.Fore.RED + "Baraye Code Binary Nemitoni Az 2-9 Ya Character Estefade Koni!"
        print(ERR)
        print(colorama.Fore.RESET)
    elif (binary == ""):
        print("Nothing inputed, restarting...")
    else:
     en = "".join(chr(int(c, 2)) for c in binary.split(" "))
     answer = colorama.Fore.CYAN + en
     print('')
     print(answer)

if re.match("morse code", question):
    morse_question = input("Morse Be English (me), English Be Morse (em) : ")
    # MORSE TO ENGLISH
    if re.match("me", morse_question):
        morse_text = input("Morse Code==> ")
        if re.match(PREG_MATCH, morse_text):
            ERR = colorama.Fore.RED + "Dar Talashe Tarjome Code Morse Nemitonid Az numerator,character Estefade Konid!"
            print(ERR)
            print(colorama.Fore.RESET)
        elif (morse_text == ""):
         print("Nothing inputed, restarting...")
        else:
         en = morse_to_en(morse_text)
         answer = colorama.Fore.CYAN + en
         print(answer)

    # ENGLISH TO MORSE
    if re.match("em", morse_question):
        FYI = colorama.Fore.RED + "Matn Ro Ba Horofe Borozg Type Konid!"
        print(FYI)
        print(colorama.Fore.RESET)

        en = input("English==> ")
        if re.match(MORSE_PREG_MATCH, en):
            ERR = colorama.Fore.RED + "Dar Talashe Tarjome English Be Morse Code, Nemitonid Az character Estedfade Konid "
            print(ERR)
            print(colorama.Fore.RESET)
        elif (en == ""):
         print("Nothing inputed, restarting...")
        else:
         morse_text = en_to_morse(en.upper())
         dots = morse_text.count(".")
         dashes = morse_text.count("-")
         answer = colorama.Fore.CYAN + morse_text

         print(answer)
         print(f"Dots: {dots}")
         print(f"Dashes: {dashes}")
         print(f"{dots + dashes} characters ")

print(colorama.Fore.RESET)
