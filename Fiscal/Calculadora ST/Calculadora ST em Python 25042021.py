#cálculo mva ajustado
    #original = 13507/10000
    #interna = 18/100
    #fatorinterna = 1 - interna
    #interestadual = 12/100
    #fator4aliq = 96/100
    #fator12aliq = 88/100
    #fator4mva = (original * fator4aliq) / fatorinterna
    #fator12mva = (original * fator12aliq) / fatorinterna
    #print(fator4mva)
    #print(fator12mva)

#função if - Origem do Produto
origem = int(input('Insira cst de origem do produto: '))
if origem < 0:
   origem = 0
   print('Não exite cst negativa')
elif origem == 0:
    print('Nacional')
elif origem == 1:
    print('Importada direta')
elif origem == 2:
    print('Importada indireta')
elif origem == 4:
    print('PPB')
else:
    print('CST não existe')
