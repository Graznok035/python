# 14.02 h19 Martin Tursk

import json

klass12opilased = []
kokku12klass = 0
huvialad = []


with open('haridustulemused.json', 'r', encoding='utf-8') as file:
    students = json.load(file)
    # print(students)
    for student in students:
        #print(student["nimi"])
        if student["klass"]=="12":
            klass12opilased.append(student["nimi"])
            kokku12klass+=1
            for tegevus in student["tegevused"]:
                if tegevus not in huvialad:
                    huvialad.append(tegevus)
            print("--------------Hinneteleht---------------")
            print(student["nimi"])
            print(student["hinded"])
            d = student["hinded"]
            for k, v in d.items():
                print(k, v)
            print("----------------------------------------")


# print(klass12opilased)
# print(kokku12klass, "Õpilast")
for i in huvialad:
    print(i)