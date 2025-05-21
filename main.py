"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Novák
email: martyn.novak@gmail.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

print("_ "*30)
print(" ")

user=input("Zadejte uživatelské jméno: ")
password=input("Zadejte heslo: ")
print("_ "*30)
print(" ")

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}  

if user in users and password == users[user]:
    print(f"Vítejte {user}!")
    print("Můžete analyzovat 3 texty.")
    
else:
    print("Neplatné uživatelské jméno nebo heslo. Program bude ukončen")
    exit()

print("_ "*30)
print(" ")

text_num = input("Zadejte číslo textu (1-3): ")

if text_num not in ["1", "2", "3"]:
    print("Neplatné číslo textu. Zadejte číslo mezi 1 a 3.")
    exit()

print("_ "*30) 
print(" ")

"""Definování číselných proměnných."""
pocet_slov = 0
pocet_velkych_pismen = 0
pocet_velkych_slov = 0
pocet_malych_pismen = 0
pocet_cisel = 0
suma_cisel = 0

text = TEXTS[int(text_num) - 1]

""" 1) Počet slov ve vybraném textu.
    2) Počet slov začínajících velkým písmenem.
    3) Počet slov psaných velkými písmeny
    4) Počet slov psaných malými písmeny.
    5) Počet čísel.
    6) Suma čísel.""" 

for word in text.split():
    pocet_slov += 1
    if word[0].isupper():
        pocet_velkych_pismen += 1
    if word.isupper():
        pocet_velkych_slov += 1
    if word.islower():
        pocet_malych_pismen += 1
    if word.isdigit():
        pocet_cisel += 1
    if word.isdigit():
        suma_cisel += int(word)

print(f"1) Počet slov: {pocet_slov}")
print(f"2) Počet slov začínajících velkým písmenem: {pocet_velkych_pismen}")
print(f"3) Počet slov psaných velkými písmeny: {pocet_velkych_slov}")
print(f"4) Počet slov psaných malými písmeny: {pocet_malych_pismen}")
print(f"5) Počet čísel: {pocet_cisel}")
print(f"6) Suma čísel: {suma_cisel}")

print("_ "*30)
print(" ")

"""jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov"""
delka_slov = {}
for word in text.split():
    delka = len(word)
    if delka not in delka_slov:
        delka_slov[delka] = 1
    else:
        delka_slov[delka] += 1

print("Sloupcový graf četnosti délek slov:")
print("_ "*30)
print(" ")
print("Délka|    Četnost         |Počet")
print("_ "*30)

for delka, pocet in sorted(delka_slov.items()):
    print (f"{delka:>5}| {'*' * pocet:<20}  |{pocet:>5}")
    
print("_ "*30)
print(" ")  

print("Děkujeme za použití našeho programu!")
print("Nashledanou!")

print("_ "*30)