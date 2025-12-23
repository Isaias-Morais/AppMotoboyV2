from datetime import datetime

def validacao_abastecimento(
        data = None,
        posto = "",
        litros = 0,
        valor = 0,
        completo = False,
        quilometragem_abastecimento = None,
        moto_id = None

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
    if not data:
        data_final = datetime.now()
    else:
        try:
            data_final = datetime.strptime(data, "%d-%m-%Y")
        except ValueError:
            return False, "Data inválida. Use DD-MM-AAAA"

    return True, data_final


