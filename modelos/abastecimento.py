class Abastecimento:

    def __init__(
            self,
            data = None,
            posto="",
            litros=0,
            valor=0,
            tanque_completo = False,
            quilometragem_abastecimento = None,
            moto_id = None
        ):
        self._data = data
        self._valor = valor
        self._litros = litros
        self._tcompleto = tanque_completo
        self._qilometragem = quilometragem_abastecimento
        self._posto = posto
        self._moto = moto_id
        self.id = None

    def __str__(self):
        return f'data-{self._data},valor-{self._valor},litros-{self._liros}taque_cheio{self._tcompleto},quilometro_do_abastecimento{self._tcompleto}'

    @property
    def preco_litro(self):
        if self._litros <= 0:
            raise ValueError("litro deve ser maior que zero")
        else:
            return self._valor/self._litros
