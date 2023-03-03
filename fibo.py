entrada = int(input("Entre com um valor: "))
val1 = 0
val2 = 1
valaux = 0

while val2 < entrada:
    valaux = val1
    val1 = val2
    val2 = val2 + valaux

if(val2 != entrada):
    print('Não pertence a sequência de fibonacci')
else:
    print('Pertence a sequência de fibonacci')