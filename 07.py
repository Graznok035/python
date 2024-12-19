#19.12.2024
#Ülesanne 7

nimi = ["Jüri Pootsman","Mari Jürges","Maali Mummuni","Juulikuus lumi maas"]

print(nimi)

for i in range(4):
    print(f"{i+1}. {nimi[i]}")
        
valik = int(input("vali lugu(1-4): "))
print(f"Mängin: {nimi[valik-1]}")

