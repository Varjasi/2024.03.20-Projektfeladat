

cégadatok = []
tranzakciók = []
darabszám = []

with open('adat.txt', 'r', encoding='utf-8') as file:
    for sor in file:
       adatok = sor.strip().split(' ')
       adat = {'tranzakció:': adatok[0], 'város': adatok[1], 'munkatárs:': adatok[2], 'termékód:': adatok[3], 'darabszám:': adatok[4]}
       cégadatok.append(adat)
       tranzakciók.append(int(adatok[0]))
       darabszám.append(int(adatok[4]))

print(cégadatok)

#2. feladat
def tranzakció():
    összeg = 0
    for tranzakciószám in tranzakciók:
        összeg = összeg + tranzakciószám

    print(f'A fájlban található tranzakciók (eladások) száma: {összeg}')
tranzakció()

#3. feladat

def darabok():
    összeg = 0
    for darab in darabszám:
        összeg = összeg + darab

    print(f'Összes eladott termék száma: {összeg}')
darabok()

# 4. feladat

sorszám = int(input("Add meg a nap sorszámát"))

while sorszám != '':
    

    

