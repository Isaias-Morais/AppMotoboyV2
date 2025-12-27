def validacao_dia_de_trabalho(km_inicial,km_final,ganho_bruto,moto_id):
    if not isinstance(km_inicial,(int)) or km_inicial < 0:
        return False, 'Digite uma quilometragem valida'
    if not isinstance(km_final,(int)) or km_final < km_inicial :
        return False,'Digite uma quilometragem valida'
    if not isinstance(ganho_bruto,(int,float)) or  ganho_bruto < 0:
        return False,'Digite um valor valido'
    if not isinstance(moto_id,(int)) or moto_id <0:
        return False,'Digite um id valido'
    return True, None
