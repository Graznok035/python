# #Harjutus 9
# # Genereeri ja kuva arvud arvud 1-20
# # for i in range(1,21):
# #     print(i, end= " ")


# # print(" ")


# # # Genereeri ja kuva 20 suvalist arvu vahemikus 1-99
# # import random
# # for i in range(1,21):
# #     print(random.randint(1, 99), end=" ")


# numbrid = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
# # Leia paaris ja paaritud arvud ning lisa oma loendisse
# paaris = []
# paaritud = []
# for nr in numbrid:
#     if nr%2==0:
#         paaris.append(nr)
#     else:
#         paaritud.append(nr)

# print(paaris)
# print(paaritud)


# # Kuva paaris ja paritute arvude summad
# # Kuva arvud 1-42
# # Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
# # Arvud, mis jagunevad 5, lisa tekst TAK (näiteks 5 TAK)
# # Kui jagunevad mõlemaga, siis lisa tekst TIKTAK (näiteks 15 TIKTAK)

# for i in range(1,43):
#     if i%5==0 and i%3==0:
#         print(f"{i} TIKTAK")
#     elif i%3==0:
#         print(f"{i} TIK")
#     elif i%5==0:
#         print(f"{i} TAK")
#     else:
#         print(i)



# for i in range(1,6):
#     print(" " * i, end="")
#     print("*" * (6-i))

ev_data = [
['vehicle', 'range', 'price'],
['Tesla Model Y Long Range', '330', '58990'],
['Volkswagen ID.4 Pro', '260', '39995'],
['Ford Mustang Mach-E', '300', '42995'],
['Audi e-tron GT', '238', '102700'],
['Nissan Leaf', '149', '27400'],
['BMW iX xDrive50', '324', '83995'],
['Polestar 2', '265', '45500'],
['Kia EV6 Long Range', '310', '47795'],
['Mercedes-Benz EQS 450+', '350', '102310'],
['Hyundai Kona Electric', '258', '37400']
]

ranges=[]

for autod in ev_data:
    print(f"{autod[0]:20} {autod[1]:5} {autod[2]:7}")
    if autod[1].isnumeric():
        ranges.append(int(autod[1]))
    # for i in autod:
    #     print(i)

print("----------------------------------------------")

print(f"keskmine ulatus: {sum(ranges)/len(ranges)}")

print("-----------------------------------------------")

for autod in ev_data:
       if autod[1].isnumeric():
        if int(autod[1]) > 300:
            print(autod[0])







