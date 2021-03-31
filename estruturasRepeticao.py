#1-Entrar com 12 números e mostrar a médias desses números.
# a=[]
# for i in range(12):
#   a.insert(i,int(input("Digite um numero: ")))
# soma=sum(i for i in a)
# x=soma/12
# print("A média dos numeros é igual a {:.2f}".format(x))
#
#2-Ler 200 números inteiros e mostrar quantos são pares e quantos são impares.
# a=0
# b=0
# for i in range(0,200):
#     if i%2 == 0:
#         a+=1
#     elif i%2 != 0:
#         b+=1
# print(f"São exatamente {a} numeros pares em um range de 200")
# print(f"São exatamente {b} numeros impares em um range de 200")

#3-Entrar com o nome, idade e sexo de 20 pessoas. Mostrar uma listagem contendo um título,
#nomes de todas as pessoas que sejam do sexo masculino e tenham mais de 21 anos.
# pessoa=[]
# p3= {}
# for i in range (20):
#     nome=input("Digite o nome da Pessoa: ")
#     idade=int(input("Digite a idade da Pessoa: "))
#     sexo=input("Digite o sexo da Pessoa: ")
#     p2 = {'Nome': nome, 'Idade': idade, 'Sexo': sexo}
#     if sexo == 'M' and idade>21:
#         p3[i]=p2
# print(p3)

#4-Faça um algoritmo que mostre o menu abaixo:
#   VATAPÁ
#   PIZZA
#   MACARRONADA
#   FEIJOADA
#   SAIR
#   OPÇÃO:
# O algoritmo só termina quando o usuário escolher a opção 5,
# quando o usuário selecionar uma opção inexistente deve mostrar a mensagem
# “Opção inexistente”, ao selecionar uma opção corretar mostrar o nome do prato e o valor,
# exemplo: Pizza: R$40,00.

# a = int(input("Menu de Hoje Escolha a Opção desejada:\n1-Vatapá\n2-Pizza\n3-Macarronada\n4-Feijoada\n0-Sair\n"))
# if a==0:
#     print('Obrigado Volte Sempre')
#     quit()
# elif a <0 or a >5:
#     print('Opção Inesistente')
#     a = int(input("Digite novamente\nMenu de Hoje Escolha a Opção desejada:\n1-Vatapá\n2-Pizza\n3-Macarronada\n4-Feijoada\n0-Sair\n"))
# while a >=0 or a <5:
#     if a==0:
#         print('Obrigado Volte Sempre')
#         quit()
#     elif a==1:
#         print ("Vatapá = R$30,00")
#         a = int(input("Mais alguma coisa?\nMenu de Hoje Escolha a Opção desejada:\n1-Vatapá\n2-Pizza\n3-Macarronada\n4-Feijoada\n0-Sair\n"))
#     elif a==2:
#         print('Pizza = R$25,00')
#         a = int(input("Mais alguma coisa?\nMenu de Hoje Escolha a Opção desejada:\n1-Vatapá\n2-Pizza\n3-Macarronada\n4-Feijoada\n0-Sair\n"))
#     elif a==3:
#         print ('Macarronada = R$14,00')
#         a = int(input("Mais alguma coisa?\nMenu de Hoje Escolha a Opção desejada:\n1-Vatapá\n2-Pizza\n3-Macarronada\n4-Feijoada\n0-Sair\n"))
#     elif a==4:
#         print ('Feijoada = R$30,00')
#         a = int(input("Mais alguma coisa?\nMenu de Hoje Escolha a Opção desejada:\n1-Vatapá\n2-Pizza\n3-Macarronada\n4-Feijoada\n0-Sair\n"))
#     else:
#         print('Opção Inesistente')
#         a = int(input("Digite novamente\nMenu de Hoje Escolha a Opção desejada:\n1-Vatapá\n2-Pizza\n3-Macarronada\n4-Feijoada\n0-Sair\n"))

#5-Entrar com 12 nomes e imprimir o primeiro caracter de cada nome.
# nome=''
# for i in range(12):
#     n = input("Digite um nome: ")
#     nome+=n[0]+'-'
# print(nome)

#6-Entrar com 8 nomes e imprimir quantas letras tem cada nome.
#
# nome=''
# for i in range(8):
#     n = input("Digite um nome: ")
#     l= str(len(n))
#     nome+=n+' '+l+' Letras - '
# print (nome)

#7-Entrar com um nome e mostra-lo de maneira invertida, ou seja, as últimas letras serão as primeiras.

# x=''
# invrt=1
# nome=input('Digite um Nome: ')
# for i in range(len(nome)):
#     n=nome[-invrt]
#     invrt+=1
#     x +=n
# print(x)

#8-Entrar com dois números e imprimir todos os números no intervalo fechado, do menor para o maior.
# n1=int(input("Digite o numero de inicio: "))
# n2=int(input("Digite o numero de inicio: "))
# if n1 < n2:
#     for i in range(n1+1,n2):
#         print(i)
# else:
#     for i in range(n2+1,n1):
#         print(i)