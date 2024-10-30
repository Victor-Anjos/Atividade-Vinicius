def calcular_media(*notas):
    "Calcula a média de uma lista de notas, validando os valores."
    if not notas:
        raise ValueError("Pelo menos uma nota deve ser fornecida.")
    
    for nota in notas:
        if nota < 0 or nota > 100:
            raise ValueError("As notas devem estar entre 0 e 100.")
    
    return sum(notas) / len(notas)