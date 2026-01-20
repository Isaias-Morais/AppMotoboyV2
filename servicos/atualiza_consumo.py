from BancoDeDados.abastecimento_repositorio import atualizar_consumo
from validacoes.moto_exitente import moto_existe
from validacoes.abasteciento_validacao import validacao_consumo

def atualizar_consumo_svc(moto_id=0,consumo=0):

    if not moto_existe(moto_id):
        return False, 'moto não existe'

    if not validacao_consumo(consumo):
        return False, 'consumo invalido'

    atualizar_consumo(moto_id,consumo)


