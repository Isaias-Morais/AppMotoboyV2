from datetime import datetime
from multiprocessing.spawn import prepare


class Moto:

    def __init__(self,modelo,cor,quilometragem = 0):
        self._modelo = modelo
        self._cor = cor
        self._quilometrgem = quilometragem
        self._abastecimento = []
        self._manutencoes = []

    def __str__(self):
        return f"{self._modelo},{self._cor}"

    def RegistraAbastecimento(self,valor,litros,completo = False,  data = None):
        if not isinstance(valor,(int ,float)) or valor <0:
            return f'Digite um valor valido'
        if not isinstance(litros,(int ,float)) or valor <0:
            return f'Digite um litragem valida'
        if not isinstance(completo,(bool)):
            return f'Digite um valor bool valido'
        dia = data or datetime.today()
        if not isinstance(dia,(datetime)):
            return f'Digite uma data valida'
        else:
            tanque_completo_str = 'Sim' if tanque_completo else 'Não'
            preco_litro = valor / litros
            registor ={
                'Dia':dia,
                'Valor':valor,
                'Litros':litros,
                'Preço_Do_litro':preco_litro,
                'Completou':tanque_completo_str
            }
            self._abastecimento.append(registor)

    def RegistraManutencao(self,peca='',valor_peca=0,quilometrgem_de_troca=None, data = None):

        if not isinstance(valor_peca, (int , float)):
            return 'Digite um valor valido'

        if not isinstance(quilometrgem_de_troca,(int,float)):
            return  'Digite uma quilometragem de troca '
        dia = data or datetime.today()
        if not isinstance(dia,(datetime)):
            return 'Digite uma data valida'
        else:

            pecaStr = peca
            valor = valor_peca
            QuilometrgemDeTroca = quilometrgem_de_troca

            registro = {
                'Dia':dia,
                'Peça_trocada':pecaStr,
                'Valor':valor,
                'Quilometragem_de_troca':QuilometrgemDeTroca
            }
            self._manutencoes.append(registro)





