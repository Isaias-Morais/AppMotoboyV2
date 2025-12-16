class Motoboy:
    def __init__(self,nome="",idade=0,email=''):
        self._nome = nome
        self._idade = idade
        self._email = email

    def __str__(self):
        return f'{self._nome},{self._idade}'

