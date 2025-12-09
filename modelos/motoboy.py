class Motoboy:
    def __init__(self,nome,idade,):
        self.nome = nome
        self.idade = idade
        self.dias_trabalhados = []

    def __str__(self):
        return f'{self.nome},{self.idade}'

