#Ülesanne 5
#19.12.2024
"""
Sinu ülesanne on luua lihtne Pythoni programm, mis aitab kasutajal valida sobiva riietuse vastavalt ilmale.
Kasutaja sisestab temperatuuri (Celsius). Kui temperatuur on alla 0 kraadi, peab programm väljastama soovituse kanda talveriideid. Kui temperatuur on vahemikus 0 kuni 15 kraadi, peaks programm soovitama kanda kevad-sügis rõivaid. Kui temperatuur on üle 15 kraadi, soovitab programm kanda suveriideid.
Kasuta if, elif ja else lauseid selle ülesande lahendamiseks.
"""
try:
    kraadid = -2
    
    if kraadid <0:
        print("Talveriided")
    elif kraadid >= 0 and kraadid <= 15:
        print("Kevad-sügis")
    else:
        print("Suvi")
except:
    print("Viga sisestuses!!!")
    
"""
Matemaatika test (randint)
Kirjuta programm, mis kontrollib kasutaja poolt sisestatud vastust lihtsale matemaatikaülesandele.
Näiteks, programm esitab küsimuse “Mis on 3 korda 4?”. Kasutaja peab sisestama vastuse. Kui kasutaja vastus on 12, siis programm väljastab “Õige vastus!”, kui aga vastus on midagi muud, siis väljastab “Vale vastus, proovi uuesti!”.
Kasuta if ja else lauseid selleks, et kontrollida kasutaja sisestatud vastust.
"""
"""import random

#print(randint(1,10))
try:
    x = random.randint(1,10)
    y = random.randint(1,10)
    vastus = int(input(f"Mis on {x} * {y} vastus?\nSisesta vastus: "))
    korrutis = x * y
    print(vastus)
    print(korrutis)
    if korrutis == vastus:
        print("Õige!")
    else:
        print("Vale")
        
    
    
    
except:
    print("viga sisestuses")"""
"""
0kiri
1kull
Mündiviskamise äraarvamine koos juhuslikkusega (and ja or)
Kirjuta programm, mis simuleerib mündiviskamist. Programm genereerib juhusliku tulemuse – “kiri” või “kull”, kasutades random.randint(0,1) funktsiooni. Programmi koostamisel pead importima import random mooduli ja kasutama randint() funktsiooni, et valida kahe võimaliku tulemuse vahel. Näiteks, kui randint(0, 1) annab tulemuseks 0, siis võib see tähendada “kirja”, ja 1 võib tähendada “kulli”.
Seejärel palub programm kasutajal arvata, kumb külg maandub ülespoole.
Kasuta if lauset, et kontrollida, kas kasutaja arvas õigesti. Kui arvas õigesti, siis joonista Turtle abil roheline ring; kui valesti, siis punane ring.
"""
import turtle
import random



try:
    valik = random.randint(0,1)
    arvamus = int(input("Vali kull (1) või kiri (0):"))
    if arvamus >=0 and arvamus <=1:
        if valik == arvamus:
            print("Arvasid ära!")
            turtle.speed(0)
            turtle.color("green")
            turtle.circle(50)
        
        else:
            print("Arvasid valesti!")
            turtle.speed(0)
            turtle.color("red")
            turtle.circle(50)
#    print("Kas kull või kiri?")

    else:
        print("See ei ole valikus!!!")
except:
    print("Midagi katastroofilist juhtus!")
turtle.done()