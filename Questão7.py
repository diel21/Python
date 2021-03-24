ht=int(input('Insira horas trabalhadas por dia:\n'))
while ht > 24:
    ht=int(input('Você Digitou errado o maximo de horas por dia é 24.\nDigite novamente:\n'))
dias=int(input ('Quantos dias você trabalhou no mês?\n'))
while dias > 31:
    dias=int(input('Você digitou errado o maximo de dias em um mês é 31.\nDigite novamente:\n'))
hrmes=ht*dias
vh=int(input('Qual valor de sua hora trabalhada:\n'))
sb=hrmes*vh
if sb>6433:
    tx= int =750
    sl=sb-tx
    print('Seu salario bruto é maior que R$6433 então seu inss é de R$750.\nSeu salario liquido é igual a R${}.'.format(sl))
    quit()
elif sb<1100:
    pd=7.5
elif sb>1100 and sb<2203:
    pd=9
elif sb>2203 and sb<3305:
    pd=12
elif sb>3305 and sb<6433:
    pd=14
td= sb/100 * pd
sl= sb-td
print ('Seu salario bruto é de R${} portanto o inss é de {}% então seu salario liquido é de R${}.'.format(sb,pd,sl))
