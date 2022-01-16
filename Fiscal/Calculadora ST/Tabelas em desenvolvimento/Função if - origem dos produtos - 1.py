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
