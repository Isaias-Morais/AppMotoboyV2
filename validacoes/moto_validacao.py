def validacao_moto(modelo,cor,quilometragem):
    if not isinstance(modelo,(str)) or len(modelo)==0:
        return False,'MODELO INVALIDO'
    if not isinstance(cor,(str)) or len(cor)==0:
        return False,'COR INVALIDA'
    if not isinstance(quilometragem,(float,int)) or quilometragem <0:
        return False,'QUILOMETRAGEM INVALIDA'
    else:
        return True,  'SUCESSO'
