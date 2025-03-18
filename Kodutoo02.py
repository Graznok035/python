import turtle
import random
turtle.speed(0)
def joonista_kujund(kujund, x, y, suurus):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    
    if kujund == 'viisnurk':
        for _ in range(5):
            turtle.forward(suurus)
            turtle.right(72)
    elif kujund == 'ring':
        turtle.penup()
        turtle.goto(x, y - suurus)
        turtle.pendown()
        turtle.circle(suurus)
    elif kujund == 'ruut':
        for _ in range(4):
            turtle.forward(suurus)
            turtle.right(90)

while True:
    kujundi_tüüp = input("Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? ")
    if not kujundi_tüüp:
        print("Programm lõpetab töö.")
        break
    if kujundi_tüüp not in ['viisnurk', 'ring', 'ruut', 'suvaline']:
        print("Vigane sisend. Proovi uuesti.")
        continue
    
    kogus_sisend = input("Mitu kujundit soovid joonistada? ")
    try:
        kogus = int(kogus_sisend)
    except ValueError:
        print("Palun sisesta korrektne täisarv.")
        continue
    
    turtle.reset()
    vahemaa = 100
    veerud = 5  
    algus_x = -200  
    algus_y = 200
    
    for indeks in range(kogus):
        x = algus_x + (indeks % veerud) * vahemaa
        y = algus_y - (indeks // veerud) * vahemaa
        suurus = 50 
        kujund = random.choice(['viisnurk', 'ring', 'ruut']) if kujundi_tüüp == 'suvaline' else kujundi_tüüp
        joonista_kujund(kujund, x, y, suurus)

turtle.done()
