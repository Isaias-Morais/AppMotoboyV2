def validacao_manutencao(
        tipo,
        descricao,
        valor,
        quilometragem,
        moto_id
        ):
    if not isinstance(tipo,(str)) or len(tipo) == 0 or tipo == None:
        return False, 'Tipo invalido'
    if not isinstance(descricao,(str)):
        return False, 'Descricao invalida'
    if not isinstance(valor,(int,float)) or valor <0 or valor == None:
        return False, 'Valor invalido'
    if not isinstance(quilometragem,(int,float)) or quilometragem <0 or quilometragem == None:
        return False, 'Quilometragem invalida'
    if not isinstance(moto_id,(int)) or moto_id <0 or moto_id == None:
        return False, 'Digite um id valido'
    return True ,None