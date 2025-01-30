from datetime import datetime

#3.1
fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))

fail.close()

aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))

index = aasta - 2011

#3.2
print(f"{aasta}. aastal oli vastuvõetuid {vastuvõetud[index]}")
ringide_arv = int(input("Sisestage ringide arv: "))
porgandite_koguarv = 0

for i in range(2, ringide_arv + 1, 2):
    porgandite_koguarv += i

print(f"Saadavate porgandite koguarv on {porgandite_koguarv}.")
#3.3
with open("konto.txt", encoding="UTF-8") as fail:
    for rida in fail:
        tehing = float(rida.strip())
        if tehing > 0:
            print(tehing)
#3.4
failinimi = input("Palun sisestage failinimi: ")

try:
    with open(failinimi, encoding="UTF-8") as fail:
        laulud = fail.readlines()
        
    for i, laul in enumerate(laulud, start=1):
        print(f"{i}. {laul.strip()}")
    
    valik = int(input("Mitmendat laulu soovite? "))
    
    if 1 <= valik <= len(laulud):
        print(f"Teie valitud laul on: {laulud[valik - 1].strip()}")
    else:
        print("Vigane valik.")
except FileNotFoundError:
    print("Faili ei leitud.")
#3.5
failinimi = input("Palun sisestage failinimi: ")

with open(failinimi, encoding="UTF-8") as fail:
    nimed = fail.readlines()

tana_paev = datetime.now().day
vastama_peab = nimed[tana_paev - 1].strip()

print(f"Täna peab vastama: {vastama_peab}")