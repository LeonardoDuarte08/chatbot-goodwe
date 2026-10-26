from datetime import datetime
from veiculos import veiculos

def obter_tarifa_atual():

    hora = datetime.now().hour

    if 0 <= hora < 6:
        return 1.50

    if 6 <= hora < 18:
        return 2.00

    if 18 <= hora < 22:
        return 2.80

    return 2.20



def calcular_recarga(veiculo, valor_recarga):

    preco_kwh = obter_tarifa_atual()

    potencia_carregador = 7

    energia_solicitada = valor_recarga / preco_kwh

    bateria_maxima = veiculos[veiculo]["bateria"]

    energia_fornecida = energia_solicitada

    valor_utilizado = valor_recarga

    estorno = 0

    if energia_solicitada > bateria_maxima:

        energia_fornecida = bateria_maxima

        valor_utilizado = bateria_maxima * preco_kwh

        estorno = valor_recarga - valor_utilizado

    tempo_horas = energia_fornecida / potencia_carregador

    return {
        "preco_kwh": preco_kwh,
        "energia_solicitada": energia_solicitada,
        "energia_fornecida": energia_fornecida,
        "valor_utilizado": valor_utilizado,
        "estorno": estorno,
        "tempo_horas": tempo_horas
    }
