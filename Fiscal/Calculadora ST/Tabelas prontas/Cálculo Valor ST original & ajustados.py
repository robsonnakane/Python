##cálculo Valor ST##

##valor_produto = float(input('Digite o valor do produto - usar apenas números e ponto: '))
##percent_ipi = float(input('Digite o percentual de IPI do produto - usar apenas números e ponto: '))
##original = float(input('Digite o MVA original do produto - usar apenas números e ponto: '))
##interna = float(input('Digite o percentual da alíquota interna do ICMS do estado de SP - usar apenas números e ponto: '))
##interestadual = float(input('Digite o percentual da alíquota interestadual do ICMS da operação - usar apenas números e ponto: '))

valor_produto = float(input('Valor do produto: '))
percent_ipi = float(input('Alíquota do IPI: '))
original = float(input('MVA original: '))
interna = float(input('Alíquota interna do ICMS: '))
interestadual = float(input('Alíquota interestadual da operação: '))
fator_ipi = percent_ipi / 100
icms_op = valor_produto * interestadual / 100
bc_produto = valor_produto + (valor_produto * fator_ipi)
fator_original = float(1 + original / 100)
fator_interna = float(1 - interna / 100)
fator_interestadual = float(interestadual / 100)
fator_aliq_4 = float(100/100 - 4/100)
fator_aliq_12 = float(100/100 - 12/100)
mva_ajustado_4 = float(fator_original * fator_aliq_4 / fator_interna)
mva_ajustado_12 = float(fator_original * fator_aliq_12 / fator_interna)
ajustado_4 = float(((fator_original * fator_aliq_4 / fator_interna) - 1) * 100 )
ajustado_12 = float(((fator_original * fator_aliq_12 / fator_interna) - 1) * 100 )

##Base de cálculo para produto Nacional - ICMS 18%##
bc_st0 = float(bc_produto * fator_original)
valor_st0 = bc_st0 * interna/100 - icms_op 
print(input('Considerando que:\nO valor da mercadoria é R$ {:.2f}\nMVA original de {:.2f}%\nAlíquota do IPI de {:.2f}%\nAlíquota do ICMS interna em SP é de {:.2f}%\nAlíquota de ICMS da operação é {:.2f}%\nPortanto temos que o Valor da Substituição Tributária é de R$ {:.2f}'.format(valor_produto, original, percent_ipi, interna, interestadual, valor_st0)))

##Base de cálculo para produto importado - ICMS 4%##
bc_st1 = float(bc_produto * mva_ajustado_4)
valor_st1 = bc_st1 * interna/100 - icms_op
print(input('Considerando que:\nO valor da mercadoria é R$ {:.2f}\nMVA Ajustado para 4% de {:.2f}%\nAlíquota do IPI de {:.2f}%\nAlíquota do ICMS interna em SP é de {:.2f}%\nAlíquota de ICMS da operação é {:.2f}%\nPortanto temos que o Valor da Substituição Tributária é de R$ {:.2f}'.format(valor_produto, ajustado_4, percent_ipi, interna, interestadual, valor_st1)))

##Base de cálculo para PPB - ICMS 12%##
bc_st2 = float(bc_produto * mva_ajustado_12)
valor_st2 = bc_st2 * interna/100 - icms_op
print(input('Considerando que:\nO valor da mercadoria é R$ {:.2f}\nMVA Ajustado para 12% de {:.2f}%\nAlíquota do IPI de {:.2f}%\nAlíquota do ICMS interna em SP é de {:.2f}%\nAlíquota de ICMS da operação é {:.2f}%\nPortanto temos que o Valor da Substituição Tributária é de R$ {:.2f}'.format(valor_produto, ajustado_12, percent_ipi, interna, interestadual, valor_st2)))

