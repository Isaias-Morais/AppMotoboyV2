from modelos.abastecimento import Abastecimento
from validacoes.abasteciento_validacao import validacao_abastecimento
from BancoDeDados.abastecimento_repositorio import salvar_abastecimeto
from datetime import datetime

data_sql = datetime.now().strftime("%Y-%m-%d")

def registra_abastecimento(
        data=None,
        posto="",
        litros=0,
        valor=0,
        tanque_completo=False,
        quilometragem_abastecimento=None,
        moto_id=None
    ):

    valido , erro = validacao_abastecimento(data,posto,litros,valor,tanque_completo,quilometragem_abastecimento,moto_id)

    if not valido:
        return erro
    else:
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
        return abastecimento


