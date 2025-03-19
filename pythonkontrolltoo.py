import json
import requests

url = 'https://metshein.com/kordamine/json/kasutajad.json'

response = requests.get(url)
if response.status_code == 200:
    print('Kasutajad on olemas')
    info = response.json()
    kasutajad =  info["kasutajad"]
#################################################################################
  
# esimene harjutus

    admin_kasutajad = [kasutaja["nimi"].replace('.' , '') for kasutaja in kasutajad if "admin" in kasutaja["roll"]]
    print("Admin kasutajad: ")
    for admin in admin_kasutajad:
        print(admin)

#################################################################################

# teine harjutus

    # for kasutaja in info["kasutajad"]: siin laks mul pekki

    admin_arv = 0
    for kasutaja in kasutajad:
        if "admin" in kasutaja["roll"]:
            admin_arv = admin_arv + 1
    print("Administraatoreid on " + str(admin_arv))
  

#################################################################################
 
# kolmas harjutus

    peatatud_kasutajad = []
    for kasutaja in kasutajad:
        if kasutaja["staatus"] == "peatatud":
            peatatud_kasutajad.append(kasutaja["nimi"])

    print("Peatatud kasutajad:")
    if peatatud_kasutajad:
        for nimi in peatatud_kasutajad:
            print(nimi)
else:
    print("Kasutajaid ei leitud")

#################################################################################

# kontrolltöö tehtud