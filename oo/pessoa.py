class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 32

    @classmethod
    def nome_e_atributos(cls):
        return f'{cls} - olhos{cls.olhos}'


class Mutante(Pessoa):
    olhos = 5


class Homem(Pessoa):
    pass

    def cumprimentar(self):
        cumprimentar_antes = super().cumprimentar()
        return f'{cumprimentar_antes}. Aperto de mão'





if __name__ == '__main__':
    cleusa = Mutante(nome='Cleusa')
    Oswaldo = Homem(cleusa, nome='Oswaldo')
    print(Pessoa.cumprimentar(Oswaldo))
    print(id(Oswaldo))
    print(Oswaldo.cumprimentar())
    print(Oswaldo.nome)
    print(Oswaldo.idade)
    print(Oswaldo.__dict__)
    for filho in Oswaldo.filhos:
        print(filho.nome)
    print(Pessoa.metodo_estatico(), Oswaldo.metodo_estatico())
    print(Pessoa.nome_e_atributos(), Oswaldo.nome_e_atributos())
    print(Oswaldo.olhos)
    print(cleusa.olhos)
    print(Oswaldo.cumprimentar())
    print(cleusa.cumprimentar())


