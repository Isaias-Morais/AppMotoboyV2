from validacoes.valida_data import valida_data

def validacao_abastecimento(
        posto,
        litros,
        valor,
        completo,
        quilometragem_abastecimento,
        moto_id
    ):

    if not isinstance(posto,(str)) or len(posto) == 0 or posto == None:
        return False, f'Posto invalido'
    if not isinstance(valor, (int, float)) or valor < 0 or valor == None:
        return False, f'Digite um valor valido'
    if not isinstance(litros, (int, float)) or litros <= 0 or litros == None:
        return False, f'Digite um litragem valida'
    if not isinstance(completo, (bool)):
        return False, f'Digite um valor bool valido'
    if not isinstance(quilometragem_abastecimento,(int, float)) or quilometragem_abastecimento < 0 or quilometragem_abastecimento == None:
        return False, f'Digite quilometragem valida'
    if not isinstance(moto_id,(int)) or moto_id <= 0 or moto_id == None:
        return False, f'Digite um id valido'

    return True , None


def validacao_consumo(consumo):

    if not isinstance(consumo, (int,float)) or consumo <= 0 or consumo == None:
        return False

    return True