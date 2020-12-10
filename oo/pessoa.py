class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'

    @staticmethod
    def metodo_estatico():
        return 32

    @classmethod
    def nome_e_atributos(cls):
        return f'{cls} - olhos{cls.olhos}'


if __name__ == '__main__':
    cleusa = Pessoa(nome='Cleusa')
    Oswaldo = Pessoa(cleusa, nome='Oswaldo')
    print(Pessoa.cumprimentar(Oswaldo))
    print(id(Oswaldo))
    print(Oswaldo.cumprimentar())
    print(Oswaldo.nome)
    print(Oswaldo.idade)
    for filho in Oswaldo.filhos:
        print(filho.nome)
    print(Pessoa.metodo_estatico(), Oswaldo.metodo_estatico())
    print(Pessoa.nome_e1_atributos(), Oswaldo.nome_e_atributos())

