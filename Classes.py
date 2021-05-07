class triangulo:
    def __init__(self,n1,n2,n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
    def calctriangulo(self):
        if self.n1 == self.n2 and self.n1 != self.n3:
            print('Este triangulo é Isóseles: Dois lados são iguais.')

        elif self.n1 == self.n3 and self.n1 != self.n2:
            print('Este triangulo é Isóseles: Dois lados são iguais.')

        elif self.n2 == self.n3 and self.n2 != self.n1:
            print('Este triangulo é Isóseles: Dois lados são iguais.')

        elif self.n1 == self.n2 and self.n1 == self.n3:
            print('Este triangulo é Equilatero: Os três lados são iguais.')

        elif self.n1 != self.n2 and self.n1 != self.n3 and self.n2 != self.n3:
            print('Este triangulo é Escaleno: Os três lados são diferentes.')

class notas:
    def __init__(self,nota1,nota2):
        self.nota1 = nota1
        self.nota2 = nota2
    def media(self):
        if self.nota1 + self.nota2 / 2 > 5 and self.nota1 > 3 and self.nota2 > 3:
            return 'Aprovado'
        else :
            return 'Reprovado'
    def reprovado(self,nota3):
        self.nota3 = nota3
        if self.nota3 > self.nota1:
            self.nota1 = self.nota3
        elif self.nota3 >self.nota2:
            self.nota2=self.nota3

class pesoplaneta:
    def __init__(self,esc,peso):
        self.esc=esc
        self.peso=peso
    def calcPeso(self):
        if self.esc == 1:
            a = self.peso * 0.37
            return a,'Mercúrio'

        if self.esc == 2:
            a= self.peso * 0.88
            return a, 'Vênus'
        if self.esc == 3:
            a = self.peso * 0.38
            return a, 'Marte'
        if self.esc == 4:
            a=self.peso * 2.64
            return a, 'Júpiter'
        if self.esc == 5:
            a=self.peso * 1.15
            return a, 'Saturno'
        if self.esc == 6:
            a=self.peso * 1.17
            return a, 'Urano'
        if self.esc == 7:
            a=self.peso * 1.18
            return a, 'Netuno'
        if self.esc == 8:
            a=self.peso * 0.11
            return a, 'Plutão'
        if self.esc == 0:
            exit()