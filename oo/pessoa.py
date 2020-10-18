class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'


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
