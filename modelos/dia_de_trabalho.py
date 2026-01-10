class Dia_de_trabalho:

    def __init__(self,data='',km_inicial=0,km_final=0,ganho_bruto=0,moto_id=0,motoboy_id=0):
        self._data = data
        self._km_inicial = km_inicial
        self._km_final = km_final
        self._ganho_bruto = ganho_bruto
        self._moto_id = moto_id


    def __str__(self):
        return f'|Data-{self._data}|Km de inicio-{self._km_inicial}|Km final-{self._km_final}|Ganho bruto-{self._ganho_bruto}|Moto-{self._moto_id}|'