class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'


if __name__ == '__main__':
    cleusa = Pessoa(nome='Cleusa')
    felipe = Pessoa(nome='Felipe')
    giovanna = Pessoa(nome='Giovanna')
    Oswaldo = Pessoa(cleusa, felipe, giovanna, nome='Oswaldo')
    print(Pessoa.cumprimentar(Oswaldo))
    print(id(Oswaldo))
    print(Oswaldo.cumprimentar())
    print(Oswaldo.nome)
    print(Oswaldo.idade)
    for filho in Oswaldo.filhos:
        print(filho.nome)
    Oswaldo.sobrenome = 'Soares'
    del Oswaldo.filhos
    print(Oswaldo.__dict__)
    print(cleusa.__dict__)
