"""
Criar class carro que vai possuir dois atributos
compostos por outras duas classes:

1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

1) Atributo de dado velocidade
2) Método acelerar que deverá incrementar a velocidade em
   uma unidade.
3) Método frear que deverá decrementar a velocidade em
   duas unidades 

A direção terá a responsabilidade de controlar a direção.
Ela oferece os seguintes atributos:

1) Valor da direção com valores possíveis: Norte, Sul, Leste
   e oeste
2) Método girar a direita.
3) Método girar a esquerda.

   N
 O   L
   S  

Exemplo:
>>> #Testando Motor
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelelar()
>>> motor.velocidade
1
>>> motor.acelelar()
>>> motor.velocidade
2
>>> motor.acelelar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0
>>> #Testando Direção
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_direita()
>>> direcao.valor
'Sul'
>>> direcao.girar_direita()
>>> direcao.valor
'Oeste'
>>> direcao.girar_direita()
>>> direcao.valor
'Norte'
>>> direcao.girar_esquerda()
>>> direcao.valor
'Oeste'
>>> direcao.girar_esquerda()
>>> direcao.valor
'Sul'
>>> direcao.girar_esquerda()
>>> direcao.valor
'Leste'
>>> direcao.girar_esquerda()
>>> direcao.valor
'Norte'
>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade
0
>>> carro.acelelar()
>>> = carro.calcular_velocidade()
1
>>> carro.acelelar()
>>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direcao()
>>> 'Norte'
>>> carro.girar_direita()
>>> carro.calcular_direcao
>>> 'Leste'
>>> carro.girar_esquerda()
>>> carro.calcular_direcao()
>>> 'Norte'
>>> carro.girar_esquerda()
>>> carro.calcular_direcao()
>>> 'Oeste'

"""
class Motor:
    def __init__(self):
        self.velocidade = 0
        
    def acelelar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        """
        if self.velocidade < 0:
            self.velocidade = 0
        """
        self.velocidade = max(0, self.velocidade)

NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'

class Direcao:
    rotacao_direita_dict = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_esquerda_dict = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }
    def __init__(self):
        self.valor = NORTE

    def girar_direita(self):
        self.valor = self.rotacao_direita_dict[self.valor]
        """
        if self.valor == NORTE:
            self.valor = LESTE
        elif self.valor == LESTE:
            self.valor = SUL
        elif self.valor == SUL:
            self.valor = OESTE
        elif self.valor == OESTE:
            self.valor = NORTE
        """

    def girar_esquerda(self):
        self.valor = self.rotacao_esquerda_dict[self.valor]
        """
        if self.valor == NORTE:
            self.valor = OESTE
        elif self.valor == OESTE:
            self.valor = SUL
        elif self.valor == SUL:
            self.valor = LESTE
        elif self.valor == LESTE:
            self.valor = NORTE
        """

class Carro(Direcao, Motor):
    def __init__(self, Direcao, Motor):
        self.calcular_velocidade = 0

    def calcular_velocidade(self):
        pass
        