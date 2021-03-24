#1
#print ("ALGORITMO SÓ SE APRENDE PRATICANDO")
#2
#nome = input("Qual seu Nome ?\n")
#print ("Seja bem Vindo",nome)
#3
#dia = input ("Dia de nascimento\n") 
#mes = input ('Mes de Nascimento\n')
#ano = input ('Ano de Nascimento\n')
#print ('Você nasceu no dia {} ''de {} ''de {} '.format(dia,mes,ano))
#4
#n1 = input('Escolha três numeros:\nNumero 1: ')
#n2 = input('Numero 2: ')
#n3 = input('Numero 3: ')
#print ("{}-{}-{}".format(n1,n2,n3))
#5 
#n1 = int (input("Digite um numero\n"))
#print ("Sucessor {} " "Antecessor {} ".format((n1 + 1),(n1 - 1)))
#6
#n1 = float(input("Para somar digite o primeiro numero:\n"))
#n2 = float(input("Agora o Segundo:\n"))
#print ("Soma: {:.1f} ".format((n1+n2)))
#7 
#ht = float(input('Por favor Inserir \nHoras trabalhadas: '))
#vh = float(input('Valor das horas trabalhadas: '))
#sb = ht * vh
#pd = float(input(" --Aliquotas de Inss 2021--\n até 1.100,00 =7,5%\n de 1.100,01 até 2.203,48 =9%\n de 2.203,49 até 3.305,22 =12%\n de 3.305,23 até 6.433,57 =14%\n De Acordo com seu Salario {}\n digite somente valor da sua porcentagem : ".format(sb)))
#td = sb / 100 * pd
#sl = sb - td
#print("Salario Liquido é igual a: {}".format(sl))
#8
#c = int(input("Digite a temperatura em graus Centigrados: \n"))
#f = (9*c+160)/5
#print ('A conversão de {} graus Centigrados para Fahrenheit é igual a {}'.format(c,f))
#9
#tempo = float(input('Em quantas horas você fez a viagem:\n'))
#vel = float(input('Qual a velocidade media da viagem:\n'))
#dist =tempo*vel
#lit_usados= dist/12
#print('Em {} horas de viagem a uma velocidade média de {} km/h uma distancia de {} km foi gasto {} litros de combustivel.'.format(tempo,vel,dist,lit_usados))
#10
#valor=float(input('Qual o valor da sua prestação ?\n'))
#taxa=0.1
#tempo=float(input('Quantos dias está atrasado ?\n'))
#prest=valor+(valor*(taxa/100)*tempo)
#print('O valor da sua prestaçao por causa do atraso é de {} reais'.format(prest))
#11
#valor=float(input('Valor que irá depositar. \n'))
#taxa=0.01
#tempo=int(input('Por quanto tempo quer deixar seu dinheiro depositado ? \n'))
#prest=valor+(valor*(taxa/100)*tempo)
#print('O seu dinheiro em {} dias ira te render {}.'.format(tempo,prest))