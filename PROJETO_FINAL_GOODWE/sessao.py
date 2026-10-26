class Sessao:

    def __init__(
        self,
        id_sessao,
        cliente,
        veiculo,
        carregador,
        energia,
        tarifa,
        custo,
        tempo,
        estorno=0.0
    ):

        self.id_sessao = id_sessao
        self.cliente = cliente
        self.veiculo = veiculo
        self.carregador = carregador
        self.energia = energia
        self.energia_restante = energia
        self.tarifa = tarifa
        self.custo = custo
        self.estorno = estorno
        self.tempo = tempo
        self.status = "Carregando"
        self.progresso = 0
        self.potencia_atual = 7

    def exibir(self):

        print("\n==============================")
        print(f"ID: {self.id_sessao}")
        print(f"Cliente: {self.cliente}")
        print(f"Veículo: {self.veiculo}")
        print(f"Carregador: {self.carregador}")
        print(f"Energia: {self.energia:.2f} kWh")
        print(f"Tarifa: R$ {self.tarifa:.2f}/kWh")
        print(f"Custo: R$ {self.custo:.2f}")
        print(f"Estorno: R$ {self.estorno:.2f}")
        print(f"Tempo: {self.tempo:.2f} horas")
        print("==============================")