from modelos.manutencao import Manutencao
from validacoes.manutencao_validacao import validacao_manutencao
from BancoDeDados.manutecao_repositorio import salvar_manutecao
from validacoes.valida_data import valida_data
from datetime import date

def registra_manutencao(
        dia=None,
        mes=None,
        ano=None,
        tipo=None,
        descricao=None,
        valor=None,
        quilometragem_manutencao=None,
        moto_id=None
    ):

    valido , erro = validacao_manutencao(tipo,descricao,valor,quilometragem_manutencao,moto_id)
    if not valido:
        return erro

    valido_data , data = valida_data(dia,mes,ano)
    if not valido_data:
        data = date.today

    manutencao = Manutencao(
        data=data,
        tipo=tipo,
        descricao=descricao,
        valor=valor,
        quilometragem_manutecao=quilometragem_manutencao,
        moto_id=moto_id
        )
    salvar_manutecao(manutencao)
    return manutencao