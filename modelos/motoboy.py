from servicos.motoboy_services import validacao_motoboy

class Motoboy:
    def __init__(self,id=None,nome="",idade=0,email=''):
        self._id = id
        self._nome = nome
        self._idade = idade
        self._email = email

    def __str__(self):
        return f'{self._nome},{self._idade}'

    def Registrar_motoboy(self):
        if validacao_motoboy()
