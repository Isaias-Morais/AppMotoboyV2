from modelos.motoboy import Motoboy
from validacoes.motoboy_validacao import validacao_motoboy
from BancoDeDados.motoboy_repositorio import salvar_motoboy

def registrar_motoboy(nome,idade,email):
    valido , erro = validacao_motoboy(nome,idade,email)
    if not valido:
        return erro
    else:
        motoboy = Motoboy(nome=nome,idade=idade,email=email)
        salvar_motoboy(motoboy)
        return motoboy