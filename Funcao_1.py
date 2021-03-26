
import Funcao_2
master=int(input("Digite o Numero da Operação desejada:\n0- Sair\n1- Saber se o número é maior que 20.\n2- Ler valores e ver se são maior que 10.\n3- Saber se o numero é maior que 10 de sim acrescentará 5 se não será decrementado 7.\n4- Saber se o número está entre 20 e 90.\n5- Saber se os numeros são iguais ou diferentes.\n6- Saber se o número é par ou ímpar.\n7- Qual a Sigla do seu estado.\n8- Raiz Quadrada.\n9- Qual seu nome?\n10- Qual a Capital do Brasil?\n11- Saber desconto do seu INSS.\n12- Imprimir números em ordem Crescente.\n"))
if master == 1:
    Funcao_2.qst1()
elif master == 2:
    Funcao_2.qst2()
elif master == 3:
    Funcao_2.qst3()
elif master == 4:
    Funcao_2.qst4()
elif master == 5:
    Funcao_2.qst5()
elif master == 6:
    Funcao_2.qst6()
elif master == 7:
    Funcao_2.qst7()
elif master == 8:
    Funcao_2.qst8()
elif master == 9:
    Funcao_2.qst9()
elif master == 10:
    Funcao_2.qst10()
elif master == 11:
    Funcao_2.qst11()
elif master == 12:
    Funcao_2.qst12()
else:
    print("FIM")