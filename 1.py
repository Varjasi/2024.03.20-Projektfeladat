

cégadatok = []
tranzakciók = []

with open('adat.txt', 'r', encoding='utf-8') as file:
    for sor in file:
       adatok = sor.strip().split(' ')
       adat = {'tranzakció:': adatok[0], 'város': adatok[1], 'munkatárs:': adatok[2], 'termékód:': adatok[3], 'darabszám:': adatok[4]}
       cégadatok.append(adat)
       tranzakciók.append(int(adatok[0]))

print(cégadatok)
#print(tranzakciók)

#2. feladat

def tranzakciók():
    összeg = 0
    for tranzakciószám in tranzakciók:
        összeg = összeg + tranzakciószám
        return (összeg)
tranzakciók()
