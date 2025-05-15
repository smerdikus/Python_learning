"""
    Máme za úkol vytvořit Bludiště, ve kterém se bude pohybovat hráč pomocí klávesnice
    Zdi budou tvořit '#' a volná místa budeme značit jako '.'
    Hráč bude reprezentovaný pomocí např 'r' (z důvodu že potom přejdeme na algoritmizaci a bude běhat sám, takže ho pak pojmenujeme r jako robot).
    Budeme zde mít i cíl, který bude značen 'g', jako goal.
    Hráčem budeme pohybovat skiskem klávesnice, konkrétně písmeny 'w/a/s/d'.
    Jakmlike bude hráč na poli s 'g', pak se program ukončí a vypíše na obrazovku: Hráč vyhrál!
"""



bludiste = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#' ],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#' ],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#' ],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#' ],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#' ],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#' ],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#' ],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#' ],
    ['#', '.', '.', '.', '.', '.', '.', '.', 'g', '#' ],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#' ],
]

# takto se take da vytvorit "pole poli", kde v jednom poli mame ulozeno vice poli
player_x = int(input("zadejte pocatecni pozici x hrace: "))
player_y = int(input("zadejte pocatecni pozici y hrace: "))


# doporucuji si vytvorit funkci pro vykresleni pole (napr print_maze(), v navodu jsme pojmenovali print_bludiste())
def print_maze():
    pass # pass znamena ze se zde nic nedeje v tomto bloku kodu, ale nelze proste vynechat prazdne misto za dvojteckou



# ted pohyb hrace, pouzijeme while prvek v poli neni cil, neboli, dokud hrac neni v cili
while bludiste[player_y][player_x] != 'g': # toto rika dokud v bludisti na pozici hrace neni g (cil)
    # zde mame za cil ptat se uzivatele zda chce nahoru, doleva, dolu nebo nahoru  ('w', 'a', 's', 'd')
    # pak ruznymi if smer == 'w' udelate player_y -= 1 a podobne pro kazdy smer
    # pozor, musite se podivat pokud na nove pozici je '.' nebo '#', take nam poslouzi if
    
    # pak vykreslime bludiste
    pass

# pokud se dostaneme sem, vypiste neco jako: "skvele, dostali jste se do cile, ktery je na pozici: x, y" za x, y dosadte pozici cile



# potom zkuste upravovat bludiste, pridavat steny, delat ruzne delky bludiste a trochu experimentovat co vas jen napadne
