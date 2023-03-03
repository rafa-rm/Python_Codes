import json

file_json = open("./dados.json")
json_input = json.load(file_json)

maior_valor = json_input[0].get('valor')
menor_valor = json_input[0].get('valor')
soma_todos_dias = 0
numero_dias_diferete_0 = 0

for elem in json_input:
    valor_aux = elem.get('valor')

    #Adicionando a soma se o valor for diferente de 0
    if(valor_aux != 0):
        soma_todos_dias = soma_todos_dias + valor_aux
        numero_dias_diferete_0 = numero_dias_diferete_0 + 1

        #Testando se o valor é o maior
        if(valor_aux > maior_valor):
            maior_valor = valor_aux
    
        #Testando se o valor é o menor
        if(valor_aux < menor_valor):
            menor_valor = valor_aux

#Calculando a média
media_mensal = soma_todos_dias/numero_dias_diferete_0
dias_superior_media = 0

#Verificando dias com faturamento maior que a média
for elem in json_input:
    valor_aux = elem.get('valor')
    if(valor_aux > media_mensal):
        dias_superior_media = dias_superior_media + 1

print("O maior valor foi: R$", maior_valor)
print("O menor valor foi: R$", menor_valor)
print("Tiveram", dias_superior_media, "dias com faturamento superior a média mensal")