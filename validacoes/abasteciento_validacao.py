from validacoes.valida_data import valida_data

def validacao_abastecimento(
        posto,
        litros,
        valor,
        completo,
        quilometragem_abastecimento,
        moto_id
    ):

    if not isinstance(posto,(str)) or len(posto) == 0:
        return False, f'Posto invalido'
    if not isinstance(valor, (int, float)) or valor < 0:
        return False, f'Digite um valor valido'
    if not isinstance(litros, (int, float)) or litros <= 0:
        return False, f'Digite um litragem valida'
    if not isinstance(completo, (bool)):
        return False, f'Digite um valor bool valido'
    if not isinstance(quilometragem_abastecimento,(int, float)) or quilometragem_abastecimento < 0:
        return False, f'Digite quilometragem valida'
    if not isinstance(moto_id,(int)) or moto_id <= 0:
        return False, f'Digite um id valido'

    return True , None

