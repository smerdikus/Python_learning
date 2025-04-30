"""
Navod na treti domaci ukol (02)
- v tomto ukolu budeme procvicovat praci s cykly
- cyklus je opakujici se kus kodu, dokud neni splnena konecna podminka


- mame 2 typy cyklu: for a while
"""

# vypsani cisel od 0 do 9
print("0 1 2 3 4 5 6 7 8 9")

# slo by to napriklad takto, co kdyz ale potrebujeme vypsat napriklad 50 cisel
# na to potrebujeme cyklus: pro kazde cislo od 0 do 10 udelame cyklus, kde cislo je ulozeno v i
for i in range(10): # toto se lehce upravi pro vypis cisel od 0 do 50
    print(i, end=" ") # end=" " znamena ze se na konci vypisu neukonci novou radkou, ale pouze mezerou
    
# casto se pouziva promenna i

print() # toto nam vypise novou radky, aby se dalsi vypis psal na novou radku

# co kdyz treba chceme cislo od 1 nasobit dvemi dokud neni vetsi nez 100, to by se pocitalo treba blbe
# na to mame druhy cyklus while
i = 1
while i <= 100:
    print(i, end=", ")
    i *= 2 # *= znamena vynasobit cislo i 2 a ulozit
    
    # vsimnete si jak je nas kod "odsazeny" to znamena blok kodu a od dvojtecky tak do bloku patri vse odsazene

print()

# nyni si ukazeme co je pole
pole = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(pole) # toto vypise cele pole

print(pole[0]) # prvni prvek v poli
print(pole[1]) # druhy prvek v poli
print(pole[9]) # posledni prvek v poli

# muzeme take upravovat co mame v poli
pole[0] = "ahoj"
print(pole)

# a ted pokud chceme vypsat vsechny prvky, projdeme takzvanym for loopem nase pole
for i in pole:
    print("(", i, end=")")
    
print()
    
# muzeme nasi promennou kterou prochazime to pole pojmenovat jakkoli
for prvek in pole:
    print("(", prvek, end=")", sep="") # sep="" znamena ze mezi kazdymi prvky co se vypisujou bude "" jinak by to byla mezera
    # sep je zkratka pro anglicky separator, oddelovac
    
print()

for ahoj in pole:
    print("(", ahoj, ahoj, ")", sep=",,,") # kouknete kde vsude jsou nase 3 carky, vsude mezi prvky oddelenymi carkou


for x in "ahoj":
    print(x) # napriklad muzeme prochazet i kazde pismeno ve slove

for ovoce in ["banan", "jablo", "malina", "mango"]:
    print(ovoce, end=" ")
    
x = []

for i in range(1, 10): # toto neni od 0 ale od 1
    x.append(i * i) # jde to napriklad i takto, takze se prida na konec vzdy ten prvek (append, znamena neco jako pripojit)
    
    
    
print(len(x)) # toto vypise jakou delku ma nase pole x
print(x)

# pokud v nasem poli bude vetsi hodnota nez 30, nastavime ji na 0
for i in range(len(x)):
    if x[i] > 30:
        x[i] = 0
    
print(x)

y = ["ahoj", "toto", "je", "druhe", "pole"]
x = x + y # toto k nasemu poli x pripoji pole y
print(x)




if 5 in x:
    print("nase pole obsahuje 5")
else:
    print("nase pole neobsahuje 5")
    
ovoce = ["banan", "jablo", "malina", "mango"]

x = 0 # takto muzeme snadno zmenit co obsahuje nase promenna x, z pole na cislo 0
for prvek in ["banan", "brambora", "malina", "dvere"]:
    if prvek in ovoce:
        x += 1 # pokud je nase x ovoce, pak do x pridame 1 (pricte 1 a ulozi do x)
        
        
for x in range(10): # zde muzeme lepe videt pouziti bloku kodu
    if x % 2 == 0:
        print(x, " je sude")
    elif x % 3 == 0:
        print(x, " je delitelne 3")
        


# takzvane 2d pole, do pole muzeme ukladat dalsi pole:
bludiste = [
    ["x", "x", "x", "x", "x"],
    ["x", "", "", "", "x"],
    ["x", "", "x", "", "x"],
    ["x", "", "x", "x", "x"],
    ["x", "", "", "", "x"],
    ["x", "", "x", "", "x"],
    ["x", "x", "x", "x", "x"]
]

# na projiti kazdeho pole budeme potrebovat 2 for loopy:
for radek in bludiste: # na kazdem radku mame jeste vice prvku, proto v kazdem radky potrebujeme i pro kazdy radek dalsi for loop
    for x in radek:
        if x == "x":
            print(x, end="") # vykreslime x pokud obsahuje "x"
        else:
            print(".", end="") # jinak vykreslime tecku
            
    print() # na konci kazdeho radku vypiseme novou radku
