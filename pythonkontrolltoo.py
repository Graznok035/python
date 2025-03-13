import json
import requests

url = 'https://metshein.com/kordamine/json/kasutajad.json'

response = requests.get(url)

#################################################################################

if response.status_code == 200:
    print('Kasutajad on olemas')
    info = response.json()
    kasutajad =  info["kasutajad"]
    admin_kasutajad = [user["nimi"].replace('.' , '') for user in kasutajad if "admin" in user["roll"]]
    print("Admin kasutajad: ")
    for admin in admin_kasutajad:
        print(admin)
else:
    print('Kasutajad ei leitud')

#################################################################################

admin_arv = 0
for user in info["kasutajad"]:
    if "admin" in user["roll"]:
        admin_arv += 1

print(f'Administraatoreid on {admin_arv}')

#################################################################################





















