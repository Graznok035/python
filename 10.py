#13.02 Ül16
#Martin Tursk

# Kirjutage Pythoni skript, mis tervitab kasutajat, kuvab praeguse töökataloogi, loob uusi katalooge vastavalt kasutaja soovile ning küsib, millist kataloogi soovitakse kustutada.

# Skript tervitab kasutajat tema operatsioonisüsteemi sisselogimisnime alusel
# Skript kuvab kasutajale praeguse töökataloogi tee
# Kataloogide loomine:
# Skript küsib kasutajalt, mitu kataloogi ta soovib luua
# Kataloogid luuakse praegusesse töökataloogi kuupäevaga märgistatud kataloogi sees, nummerdatuna (nt “1”, “2”)
# Kataloogi kustutamine:
# Pärast kataloogide loomist küsib skript kasutajalt, millist äsja loodud või olemasolevat kataloogi soovitakse kustutada, esitades kataloogi nime 1, 2 jne
# Kui sisestatud kataloogi nimi eksisteerib, kustutatakse see
# Kuva kuupäeva kasutas olevad kataloogid

import os
from datetime import date

print(f"Tere {os.getlogin()}")
print(f"Sinu rada {os.getcwd()}")

kataloogidearv = 10
kustuta = 5
kp = str(date.today())

try:
    os.mkdir(kp)
    print(f"{kp} kataloog on loodud!")
    for i in range(1,kataloogidearv+1):
        kaust = kp+"/"+str(i)
        os.makedirs(kaust)
except:
    print("Kataloog on juba olemas!")




if os.path.exists(kp+"/"+str(kustuta)):
    os.rmdir(kp+"/"+str(kustuta))
    print(f"{kustuta} kataloog kustutatud!")
else:
    print(f"{kustuta} kataloogi ei leitud!")