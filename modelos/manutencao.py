class Manutencao:
    def __init__(
            self,
            data=None,
            moto_id=None,
            tipo='',
            descricao='',
            valor=0,
            quilometragem_manutecao=None
        ):

        self._data = data
        self._moto = moto_id
        self._tipo = tipo
        self._descricao = descricao
        self._valor = valor
        self._quilometragem = quilometragem_manutecao

    def __str__(self):
        return f'data-{self._data},tipo-{self._tipo},valor-{self._valor},quiometragem-{self._quilometragem}'
