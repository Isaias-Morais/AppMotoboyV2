from BancoDeDados.moto_repositorio import excluir_moto
from BancoDeDados.dia_de_trabalho_repositorio import excluir_dias_trabalhados
from BancoDeDados.manutecao_repositorio import excluir_manutencao
from BancoDeDados.abastecimento_repositorio import excluir_abastecimentos
from servicos.moto_ativa import redefinir_moto_ativa, busca_moto_ativa
from validacoes.moto_exitente import moto_existe


def excluir_moto_geral(moto_id):
    id = busca_moto_ativa()
    if not moto_existe(moto_id):
        return False, 'Moto nao existente'

    excluir_manutencao(moto_id)
    excluir_abastecimentos(moto_id)
    excluir_dias_trabalhados(moto_id)
    excluir_moto(moto_id)

    if id == moto_id:
        redefinir_moto_ativa()

    return True,'Moto excluida com sucesso'

