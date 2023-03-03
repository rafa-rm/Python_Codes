entrada = input("Digite um texto: ")
reversa = ""

for letra in entrada:
   reversa = letra + reversa

print("A String original é:",entrada)
print("A String invertida é:",reversa)