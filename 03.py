# Ülesańne 03
# 05.12.2024

nimi = "Karin" 			#sõne, string, str
vanus = 18 				#int, ineger, täisarv
keskmine_hinne = 4.7	#komaarv, float

print(nimi+", vanus "+str(vanus)+", keskmine hinne on "+str(keskmine_hinne))

#print(nimi,vanus,keskmine_hinne)

#print(f"{nimi} on käinud {vanus} aastat koolis ja hindeks on {keskmine_hinne}")


import turtle


kylje_pikkus = 100

nurk = 60

varv = "red"

#liigtume kohta, et kujund oleks keskel

#turtle.penup()
#turtle.goto(0, 200)
#turtle.pendown()

#hakkame joonistama
turtle.speed(0)
turtle.color(varv)

turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.right(nurk)
turtle.forward(kylje_pikkus)
turtle.right(nurk)

#üks kolmnurk on olemas, teeme sisemise. Liigume nii, et kujund oleks keskel ja ilus ja kaunis

#turtle.penup()
#turtle.goto(0,-145)
#turtle.pendown()

#oleme kohal, joonistame

#turtle.left(60)
#turtle.forward(200)
#turtle.left(120)
#turtle.forward(200)
#turtle.left(120)
#turtle.forward(200)

#korras. viime kursori ka ilusasse paika ja saan rahul olla.

turtle.penup()
turtle.fd(kylje_pikkus*1.5)
turtle.pendown()


turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.right(nurk)
turtle.forward(kylje_pikkus)
turtle.right(nurk)

turtle.penup()
turtle.fd(kylje_pikkus*1.5)
turtle.pendown()


turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.right(nurk)
turtle.forward(kylje_pikkus)
turtle.right(nurk)

#turtle.penup()
#turtle.fd(kylje_pikkus*1.5,0)
#turtle.pendown()
#kilpkonn on väsinud, tahab koju magama minna

turtle.done()