from Classes import *
import os
escolha = int(input('''Escolha a Questão desejada:
1- Classificação de Triangulo.
2- Calcular Média de Aluno.
3- Calcular seu Peso em Planetas.
0- Sair. 
'''))
while escolha >3 and escolha != 0 :
    escolha = int(input('''Escolha a Questão desejada:
1- Classificação de Triangulo.
2- Calcular Média de Aluno.
3- Calcular seu Peso em Planetas.
0- Sair. 
    '''))

##############################################################################################
if escolha == 1:
    os.system('cls'if os.name =='nt' else'clear')
    lado1 = int(input("Digite o Primeiro Lado: "))
    lado2 = int(input("Digite o Segundo Lado: "))
    lado3 = int(input("Digite o Terceiro Lado: "))

    triangulo = triangulo(lado1,lado2,lado3)
    triangulo.calctriangulo()

#############################################################################################
elif escolha == 2 :
    os.system('cls' if os.name == 'nt' else 'clear')
    nota1 = int(input("Digite a nota da Prova b1: "))
    nota2 = int(input("Digite a nota da Prova b2: "))
    nota = notas(nota1,nota2)
    nota.media()
    if nota.media() == 'Aprovado':
        print("Aprovado")
        exit()
    if nota.media()== 'Reprovado':
        nota3 = int(input('Digite a Nota da prova de Recuperação: '))
        nota.reprovado(nota3)
        nota.media()
        if nota.media() == 'Reprovado':
            print("Reprovado")
        else:
            print("Aprovado")
    else:
        print('Aprovado')

#############################################################################################

elif escolha == 3:
    os.system('cls' if os.name == 'nt' else 'clear')
    planeta = int(input("""Escolha o Planeta
1- Mercúrio.
2- Vênus.
3- Marte.
4- Júpiter.
5- Saturno.
6- Urano.
7- Netuno.
8- Plutão.
0- Exit.
"""))
    while planeta > 8 and planeta != 0:
        planeta = int(input("""Escolha o Planeta
1- Mercúrio.
2- Vênus.
3- Marte.
4- Júpiter.
5- Saturno.
6- Urano.
7- Netuno.
8- Plutão.
0- Exit.
"""))
    if planeta == 0:
        exit()

    peso = int(input('Qual seu Peso: '))
    pesoPlaneta = pesoplaneta(planeta,peso)
    resultado = pesoPlaneta.calcPeso()
    print(f"O seu Peso no Planeta {resultado[1]} é {resultado[0]:.2f}")

#############################################################################################

elif escolha == 0:
    exit()