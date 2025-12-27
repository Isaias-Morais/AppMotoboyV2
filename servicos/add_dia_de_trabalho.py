from modelos.dia_de_trabalho import Dia_de_trabalho
from validacoes.dia_de_trabalho_validacao import validacao_dia_de_trabalho
from BancoDeDados.dia_de_trabalho_repositorio import salvar_dia_de_trabalho
from validacoes.valida_data import valida_data
from datetime import date


def registra_dia_de_trabalho(
        dia=None,
        mes=None,
        ano=None,
        km_inicial=0,
        km_final=0,
        ganhon_bruto=0,
        moto_id=None
    ):

    valido , erro = validacao_dia_de_trabalho(km_inicial,km_final,ganhon_bruto,moto_id)
    if not valido:
        return erro

    valido_data, data = valida_data(dia, mes, ano)
    if not valido_data:
        data = date.today()

    dia_de_trabalho = Dia_de_trabalho(
        data=data,
        km_inicial=km_inicial,
        km_final=km_final,
        ganho_bruto= ganhon_bruto,
        moto_id=moto_id
    )
    salvar_dia_de_trabalho(dia_de_trabalho)
    return dia_de_trabalho