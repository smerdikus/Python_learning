"""
    Toto je navod ke uloze03.
    Zde si procvicime jeste praci s poli a pak praci s for loopem.
"""

# Zopakovani prace s polem

# Toto vytvori nove prazdne pole
pole = []

# Toto vytvori pole ktere vsak uz neco obsahuje
pole1 = ['#', '.', '#', '#', '.', '#']

print(pole1)  # print(pole) nam vypise nase pole promennych

# ale muzeme si vsimnout, ze vypis neni uplne nejhezci, pokud bysme chteli aby byl vypis pouze znaku, musime takto
for ch in pole1:
    # toto nam do ch ulozi postupne kazdou promennou tohoto pole
    # Uz vime, ze end='' znamena ze se na konci vypisu ch neudela nova radka ale vypise se '' (to co je uvnitr uvozovek, coz je nic)
    print(ch, end='') # pojmenovavam si to jako ch, protoze je to takzvany charakter (ascii znak, pro zajimavost si doporucuji najit co je ascii tabulka)
    
print("\n\n") # pouze pro oddeleni naseho vypisu, urcite uz vite co dela toto


# nebo by slo takzvane indexovat do pole
for i in range(len(pole1)):
    print(pole1[i], end='') # neboli pro kazde cislo, ktere je od 0 do delky pole (len(pole1)) vypiseme z pole prvek na pozici i (pole1[i])

print("\n\n") # pouze pro oddeleni naseho vypisu, urcite uz vite co dela toto


# abysme mohli ukladat bludiste, potrebovali bysme ale pro kazdy radek jine pole napriklad takto
pole0 = ['#', '#', '#', '#', '#', '#']
pole2 = ['#', '.', '#', '.', '.', '#']
pole3 = ['#', '.', '.', '.', '#', '#']
pole4 = ['#', '#', '#', '#', '#', '#']


# ted bysme chteli vsechny pole vypsat
for i in range(len(pole0)):
    print(pole0[i], end='')
print()

for j in range(len(pole1)):
    print(pole1[j], end='')
print()
    
for k in range(len(pole2)):
    print(pole2[k], end='')
print()

for l in range(len(pole3)):
    print(pole3[l], end='')
print()

for m in range(len(pole4)):
    print(pole4[m], end='')
print() # tyto print() nam vzdy udelaji novou radku za kazdym radkem, jinak by se vypsaly radky hned za sbou


# co takhle ale dat vsechny pole do jednoho "pole polí"
bludiste = [pole0, pole1, pole2, pole3, pole4]

# tomuto bysme uz mohli rozumet, for loop "projede" bludiste pres kazdy radek, ktery je pole, takze vypise vsechny pole, ale ne uplne hezky
for radek in bludiste:
    print(radek)

print("\n\n") # toto uz vime
    
# to by se dalo vyresit uz nasim znamym zpusobem
for radek in bludiste:
    # toto uz jsme videli nekde, to mame nahore take, ale ulehcili jsme si psani 5 for loopu do jednoho for loopu
    # ten projede vsechny radky, pojmenuje si kazdy jako radek, pak v kazdem radku (ktery je pole) projede vsechny pismena v tom poli
    for i in range(len(radek)):
        print(radek[i], end='')
    print() # po kazdem radku musime zacit na novou radku (print() prida '\n' na konec radky, proto to potrebujeme, jinak by se psaly radky za sebe

# dalo by se ale jeste indexovat dovnitr pres 2 hranate zavorky [][]
# napriklad kdyz chceme prvek na prvnim radku, na druhem miste, tak musime do bludiste indexovat takto:
print(bludiste[0][1]) # pamatujte ze cislujeme od 0, takze 0 je prvni prvek, 1 je druhy
print(bludiste[3][1]) # toto je treba prvek na 4. radku na 2. miste

print("\n\n")

# takze zase zkusime timto zpusobem
for y in range(len(bludiste)): # projedeme kazde cislo y, jako ocislovani vsech radku
    for x in range(len(bludiste[y])): # ted projedeme pres x delku tohot radku (bludiste[y] je radek cislo y v bludisti)
        print(bludiste[y][x], end='') # toto je prvek na pozici [y][x] v bludisti, to ale jede pres cele pole po x a po y
        # zkuste si nakreslit treba na papir pole a pak co je x a co je y
    print() # toto uz vime proc potrebujeme, za kazdy radek musime dat novy radek
    
print("\n\n")
    
# co ted ale s hracem, pokud bysme meli napriklad pozici hrace ulozene jako
player_x = 1
player_y = 1

# tak do pole chceme na pozici x = 1 a y = 1 vykreslit hrace ('r')
# proto potrebujeme to nase pozicovani do pole pres [y][x] abysme poznali x a y hrace
for y in range(len(bludiste)):
    for x in range(len(bludiste[y])):
        if x == player_x and y == player_y: # pokud je na nasi pozici x y hrac, tak musime vykreslit 'r'
            print('r', end='')
        else:
            print(bludiste[y][x], end='') # jinak vykreslujeme blok v bludisti
    print()
    
    
print("\n\n")

# ted prichazi zasadni vec v programovani: funkce
# predstavte si to jako, kdyz chcete vykreslit pyramidu takto
for i in range(10):
    print('*' * i)

# ted si predstavte ze chcete vykreslit znovu, potom byste museli vzdy napsat tento for loop, na to ale mame funkce
# ty se tvori takto:
def funkce(): # nazev funkce a v zavorce jsou tzv parametry (vysvetlime pozdeji)
    # telo funkce
    for i in range(10):
        print('*' * i)
        
        
# toto program provede jenom pokud funkci "zavolame" a to se dela takto
funkce()

# kdyz chceme dalsi pyramidu, staci napsat toto:
funkce()

# ted se zamyslete, co je napriklad print()
# ano, print() je funkce, kde napriklad print('r', end='') je funkce kde davame parametr 'r' ze se vypise r a end='' ze na konec radku se nevypise '\n' ale ''

# tak co si ted vytvorit treba funkci pro vykresleni bludiste
def print_bludiste():
    print("\n\n") # pred kazdym bludistem si udelame 2 prazdne radky
    for y in range(len(bludiste)):
        for x in range(len(bludiste[y])):
            if x == player_x and y == player_y:  # pokud je na nasi pozici x y hrac, tak musime vykreslit 'r'
                print('r', end='')
            else:
                print(bludiste[y][x], end='')  # jinak vykreslujeme blok v bludisti
        
        print()

        
# zamyslete se jak by se ted vykreslilo bludiste?

# takto
print_bludiste()

# ted kdyz napriklad zmenime pozici hrace
player_x = 1
player_y = 3

# tak vykresleni bludiste rovnou hrace vykresli na teto pozici
print_bludiste()

# to je asi vse, zkuste vse pochopit proc co a jak funguje, pripadne se mi ozvete, vse vysvetlime, mail: smerdikus@gmail.com nebo whatsapp

