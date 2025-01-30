import random

#2.1
kordi = int(input("Mitu korda äratus heliseb? "))

for _ in range(kordi):
    print("Tõuse ja sära!")
#2.2
ringid = int(input("Sisesta ringide arv: "))

if ringid < 0:*-
    print("Viga: ringide arv peab olema positiivne.")
else:
    porgandid = 0
    i = 2
    while i <= ringid:
        porgandid += i
        i += 2
    print(f"Saadud porgandite koguarv: {porgandid}")
#2.3
taringud = int(input("Mitu täringut visata? "))

for _ in range(taringud):
    tulemus = random.randint(1, 6)
    print(tulemus)
#2.4
sn = int(input("Sisesta täisarv: "))
g = 1
c = 1
while c < sn:
    g *= 2
    c += 1
print(f"Nisuteri {sn}. Ruudu eest: {g}")
#2.5
ok = 14
pk = int(input("Mitu põialpoissi tahab õunu? "))
oa = []
for _ in range(pk):
    õunad = random.randint(1, 2)
    oa.append(õunad)
    print(õunad)
oj = ok - sum(oa)
print(f"Lumivalgekesele jäi {oj} õuna üle.")