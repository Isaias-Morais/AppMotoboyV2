from modelos.moto import Moto
from validacoes.moto_validacao import validacao_moto
from BancoDeDados.moto_repositorio import salvar_moto

def registra_moto(
        marca='',
        modelo='',
        ano=0,
        quilometragem=0,
        consumo=0
    ):


    valido , erro = validacao_moto(marca,modelo,ano,quilometragem,consumo)

    if not valido:
        return erro
    else:
        moto = Moto(
            marca=marca,
            modelo=modelo,
            ano=ano,
            quilometragem=quilometragem,
            consumo=consumo,
            motoboy_id=1)
        salvar_moto(moto)
        return moto


def exluri_moto(moto_id):