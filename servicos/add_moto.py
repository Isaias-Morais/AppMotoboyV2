from modelos.moto import Moto
from validacoes.moto_validacao import validacao_moto

def registra_moto(modelo='',cor='',quilometragem=0):
    valido , erro = validacao_moto(modelo,cor,quilometragem)
    if not valido:
        return erro
    else:
        moto = Moto(nome=nome,cor=cor,quilometragem=quilometragem)
        salvar_moto(moto)
        return moto