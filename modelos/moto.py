class Moto:

    def __init__(self,modelo,cor,quilometragem = 0):
        self._modelo = modelo
        self._cor = cor
        self._quilometragem_total = int(quilometragem)

    def __str__(self):
        return f"modelo-{self._modelo},cor-{self._cor},quilometragem-{self._quilometragem_total}"