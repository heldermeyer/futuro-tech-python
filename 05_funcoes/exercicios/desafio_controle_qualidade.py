# Controle de Qualidade em Produção

# Uma fábrica de garrafas realiza inspeção automatiada das medidas das peças produzidas.
# As medidas aceitáveis variam de 19,5 cm a 20,5 cm.
# Crie uma função que receba uma lista de medidas e retorne quantas estão fora do padrão.
medidas = [19.5, 20.0, 20.5, 18.5, 19.7, 10.5]
quantidade_fora_padrao = len(list(filter(lambda medida: medida < 19.5 or medida > 20.5, medidas)))
print(quantidade_fora_padrao)

exit()

def inspecionar(medidas: list) -> int:
    """
        Essa função tem como objetivo, contar a quantidade\n
        de garrafas fora do padrão aceitável (19.5 à 20.5).\n
        Argumentos: Lista contendo os tamanhos das garrafas.\n
        Saída: Quantidade de garrafas fora do padrão.
    """
    quantidade_fora_padrao = 0

    for medida in medidas:
        if medida < 19.5 or medida > 20.5:
            quantidade_fora_padrao += 1  
    return quantidade_fora_padrao

medidas = [19.5, 20.0, 20.5, 18.5, 19.7, 10.5]
print(inspecionar(medidas))