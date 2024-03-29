# 1. feladat: Olvasd be az adat.txt fájl tartalmát egy tetszőleges adatszerkezetbe!
def adatok_beolvasasa(file_path):
    with open(file_path, 'r') as file:
        adatok = [sor.strip().split() for sor in file]
    return adatok

# 2. feladat: Írd ki a képernyőre, hogy hány tranzakció (eladás) adatait tartalmazza a fájl!
def tranzakciok_szama(adatok):
    return len(adatok)

# 3. feladat: Írd ki a képernyőre, hogy az összes munkatárs együttesen összesen hány darab terméket adott el az elmúlt hónapban!
def osszes_eladott_termek(adatok):
    osszes_termek = sum(int(sor[4]) for sor in adatok)
    return osszes_termek

# 4. feladat: Kérd be a felhasználótól egy napnak a sorszámát és írd ki az adott napon történt eladásokat!
def forgalom_adott_napon(adatok):
    nap = int(input("Add meg a nap sorszámát [1...28]: "))
    while nap < 1 or nap > 28:
        print("Hibás adatbevitel! Próbáld újra...")
        nap = int(input("Add meg a nap sorszámát [1...28]: "))

    forgalom = [sor for sor in adatok if int(sor[0]) == nap]
    
    if forgalom:
        print(f"{nap}. nap forgalma:")
        for eladas in forgalom:
            print(" ".join(eladas[1:]))
    else:
        print(f"A megadott napon nem volt forgalma a cégnek.")

# 5. feladat: Írd ki a képernyőre, hogy az elmúlt hónapban melyik munkatárs generálta a legtöbb bevételt a cégnek!
def legtobb_bevetel(adatok):
    bevetel = {}
    for sor in adatok:
        munkatars = sor[2]
        termek = sor[3]
        ar = int(sor[4]) * arak[termek]
        if munkatars in bevetel:
            bevetel[munkatars] += ar
        else:
            bevetel[munkatars] = ar

    max_bevetel = max(bevetel, key=bevetel.get)
    return max_bevetel, bevetel[max_bevetel]

# 6. feladat: Írd ki a képernyőre, hogy mely napokon nem történt tranzakció (eladás)!
def tranzakciomentes_napok(adatok):
    hetek = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
    tranzakciok = {het: [] for het in hetek}
    
    for sor in adatok:
        nap_sorszam = int(sor[0])
        nap = hetek[(nap_sorszam - 1) % 7]
        if sor not in tranzakciok[nap]:
            tranzakciok[nap].append(sor)

    tranzakciomentes_hetek = []
    for het, napok in tranzakciok.items():
        if not napok:
            tranzakciomentes_hetek.append(het)

    return tranzakciomentes_hetek

# A termékek árainak rögzítése
arak = {"T1": 600, "T2": 750, "T3": 550, "T4": 650, "T5": 450}

# Főprogram
adatok = adatok_beolvasasa("adat.txt")
print("2. feladat")
print(f"A fájlban található tranzakciók (eladások) száma: {tranzakciok_szama(adatok)}")
print("\n3. feladat")
print(f"Az összes munkatárs együttesen összesen {osszes_eladott_termek(adatok)} darab terméket adott el az elmúlt hónapban.")
print("\n4. feladat")
forgalom_adott_napon(adatok)
print("\n5. feladat")
legjobb_munkatars, legtobb_bevetel = legtobb_bevetel(adatok)
print(f"A legtöbb bevételt az {legjobb_munkatars} kódú munkatárs generálta: {legtobb_bevetel} Ft.")
print("\n6. feladat")
tranzakciomentes_napok = tranzakciomentes_napok(adatok)
if tranzakciomentes_napok:
    print("Tranzakciómentes napok:")
    for het in tranzakciomentes_napok:
        print(f"{het}. hét: ", end="")
        print(", ".join(tranzakciomentes_napok[het]))
else:
    print("Az elmúlt hónapban minden nap történt tranzakció (eladás).")
