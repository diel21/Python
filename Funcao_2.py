def qst1():
    n1 = int(input('Coloque um Numero: '))
    if n1>20:
        print(n1)
    else:
        print("é menor que 20")
def qst2():
    n1 = int(input("Insira um Numero: "))
    n2 = int(input("Insira um Numero: "))
    n3 = n1 + n2
    if n3>10:
        print('a soma de {} + {} é igual a {} e é maior que 10'.format(n1,n2,n3))
    else:
        print("a soma de {} + {} é igual a {} e é menor que 10".format(n1,n2,n3))
def qst3():
    n1 = int(input("Insira um Numero: "))
    n2 = int(input("Insira um Numero: "))
    n3 = n1 + n2
    if n3==10:
        print ("Ja que o valor é 10 tenho que adicionar 5 e decrementar 7 o resultado é = 10+5=15 e 10-7=3 ")
    elif n3>= 10:
        n4 = n3 + 5
        print("O valor da soma dos dois numeros é igual a {} adicionando 5 ele fica {}".format(n3,n4))
    elif n3<=10:
        n4=n3 - 7
        print("O valor da soma dos dois numeros é igual a {} e é menor que 10 portanto decrementando 7 ele fica {}".format(n3,n4))
def qst4():
    n1 = int(input("Digite um numero: "))
    if n1>=20 and n1<=90:
        print("este numero está compreendido entre 20 e 90")
    else:
        print ("este numero não está entre 20 e 90")
def qst5():
    n1 = int(input("Insira um Numero: "))
    n2 = int(input("Insira um Numero: "))
    if n1==n2:
        print("São iguais")
    else:
        print("Não são iguais")
def qst6():
    n1 = int(input("Insira um Numero: "))
    if n1%2==0:
        print("Este numero é par")
    else:
        print("Este numero é impar")
def qst7():
    sigla = str(input("Qual a sigla do seu Estado ?\n"))
    if sigla=='RJ' or sigla=='rj':
        print("Seja bem Vindo Carioca")
    elif sigla=='SP' or sigla=='sp':
        print("Seja bem Vindo Paulista")
    elif sigla=='MG' or sigla=='mg':
        print ("Seja bem Vindo Mineiro")
    else:
        print("Seja bem Vindo")
def qst8():
    n1 = int(input("Insira um Numero: "))
    raiz = n1 ** 0.5
    if n1>=0:
        print("A raiz quadrada de {} é igual a {:.2f}".format(n1,raiz))
    else:
        print("O numero é negativo portanto não tem raiz quadrada")
def qst9():
    nome=str.upper(input("Qual seu nome ? \n"))
    if nome =="JOSÉ" or nome=="JOSE":
        print("Seja bem vindo José")
    else:
        print ("Seja bem vindo")
def qst10():
    nome = str.upper(input("Qual a Capital do Brasil ?\n"))
    if nome == "BRASÍLIA" or nome=="BRASILIA":
        print("Parabéns")
    else:
        print ("ERROU")
def qst11():
    sl = int(input("Qual seu Salario?\n"))
    if sl <=600:
        print("Isento")
    elif sl>600 and sl<=1200:
        print("Você paga 20% de INSS")
    elif sl>1200 and sl<=2000:
        print("Você paga 25% de INSS")
    elif sl>2000:
        print("Você paga 30% de INSS")
def qst12():
    print("Insira 3 Numeros sem repetir o mesmo numero.")
    a=int(input("Insira um numero: "))
    b=int(input("Insira um numero: "))
    c=int(input("Insira um numero: "))
    if a>b and a>c and b>c:
        print("A sequencia certa dos numeros é está {}-{}-{}".format(c,b,a))
    elif a>b and a>c and c>b:
        print("A sequencia certa dos numeros é está {}-{}-{}".format(b,c,a))
    elif b>a and b>c and a>c:
        print("A sequencia certa dos numeros é está {}-{}-{}".format(c,a,b))
    elif b>a and b>c and c>a:
        print("A sequencia certa dos numeros é está {}-{}-{}".format(a,c,b))
    elif c>a and c>b and a>b:
        print("A sequencia certa dos numeros é está {}-{}-{}".format(b,a,c))
    elif c>a and c>b and b>a:
        print("A sequencia certa dos numeros é está {}-{}-{}".format(a,b,c))
