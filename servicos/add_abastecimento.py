from BancoDeDados.finaceiro_repositorio import busca_abastecimento_consumo_medio
from modelos.abastecimento import Abastecimento
from servicos.atualiza_consumo import atualizar_consumo
from servicos.calculos import calcular_km_rodados, calcular_consumo_medio_real
from validacoes.abasteciento_validacao import validacao_abastecimento
from BancoDeDados.abastecimento_repositorio import salvar_abastecimeto
from validacoes.valida_data import valida_data
from datetime import date


def registra_abastecimento(
        dia=None,
        mes=None,
        ano=None,
        posto=None,
        litros=None,
        valor=None,
        tanque_completo=False,
        quilometragem_abastecimento=None,
        moto_id=None
    ):

    valido , erro = validacao_abastecimento(posto,litros,valor,tanque_completo,quilometragem_abastecimento,moto_id)
    if not valido:
        return erro

    valido_data , data = valida_data(dia,mes,ano)
    if not valido_data:
        data = date.today()

    abastecimento = Abastecimento(
        data=data,
        posto=posto,
        litros=litros,
        valor=valor,
        tanque_completo=tanque_completo,
        quilometragem_abastecimento=quilometragem_abastecimento,
        moto_id=moto_id
        )
    salvar_abastecimeto(abastecimento)
    if not tanque_completo:
        return

    historico = busca_abastecimento_consumo_medio(moto_id)

    if not historico or len(historico) < 2:
        return

    km_litros = calcular_km_rodados(historico)

    if not km_litros:
        return


    consumo_medio = calcular_consumo_medio_real(km_litros)

    atualizar_consumo(consumo_medio)

    return True



