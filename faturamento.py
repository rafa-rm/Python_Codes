dados = [{'Estado': 'SP', 'Faturamento': 67863.43},
         {'Estado': 'RJ', 'Faturamento': 36678.66},
         {'Estado': 'MG', 'Faturamento': 29229.88},
         {'Estado': 'ES', 'Faturamento': 27165.48},
         {'Estado': 'Outros', 'Faturamento': 19849.53}]



faturamento_total = 0
for dado in dados:
    faturamento_total = faturamento_total + dado.get('Faturamento')

print('------ Contribuição de cada estado ------')
for dado in dados:
    print(f'O estado', dado.get('Estado'),'Contribuiu com', 
          round(((dado.get('Faturamento')/faturamento_total) * 100),2),'% no valor total')