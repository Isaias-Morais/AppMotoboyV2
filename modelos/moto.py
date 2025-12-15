from datetime import datetime
from servicos.abasteciento_service import validacao_abastecimento

class Moto:

    def __init__(self,modelo,cor,quilometragem = 0):
        self._modelo = modelo
        self._cor = cor
        self._quilometragem_total = int(quilometragem)

    def __str__(self):
        return f"{self._modelo},{self._cor}"

    def Registra_Abastecimento(self,valor,litros,completo = False,quilometragem_de_abastecimento = None,  data = None):
        if validacao_abastecimento(valor,litros,completo,quilometragem_de_abastecimento,data):
            if quilometragem_de_abastecimento > self._quilometragem_total:
                self._quilometragem_total = quilometragem_de_abastecimento
        else:
            return 'Nenhun dado alterado'

    def Registra_Manutencao(self,peca='',valor_servico=0,quilometragem_de_troca=None, data = None):

        if not isinstance(valor_servico, (int , float)):
            return 'Digite um valor valido'
        if quilometragem_de_troca is None:
            quilometragem_de_troca = 0
        if not isinstance(quilometragem_de_troca,(int,float)):
            return  'Digite uma quilometragem de troca '
        dia = data or datetime.today()
        if not isinstance(dia,(datetime)):
            return 'Digite uma data valida'
        else:
            if quilometragem_de_troca > self._quilometragem_total:
                self._quilometragem_total = quilometragem_de_troca
            registro = {
                'Dia':dia.strftime('%d/%m/%Y'),
                'Peça_trocada':peca,
                'Valor':valor_servico,
                'Quilometragem_de_troca':quilometragem_de_troca
            }






