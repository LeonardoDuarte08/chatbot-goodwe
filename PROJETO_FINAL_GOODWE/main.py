import threading
import time#
from sessao import Sessao
from veiculos import veiculos
from algoritmos import calcular_recarga
from persistencia import carregar_sessoes, salvar_sessoes

historico_sessoes = []
sessoes_ativas = []
lock_persistencia = threading.Lock()

carregadores = {
    1: "disponivel",
    2: "disponivel",
    3: "disponivel",
    4: "disponivel"
}

def menu():

    print("\n========================")
    print("      ECOGRID CEV")
    print("========================")
    print("1 - Nova Sessão")
    print("2 - Listar Sessões")
    print("3 - Buscar Sessão")
    print("4 - Ordenar Sessões")
    print("5 - Estatísticas")
    print("6 - Monitorar Carregamentos")
    print("7 - Sair")

    return input("\nEscolha uma opção: ")

def atualizar_potencia():

    sessoes_ativas = [
        s for s in historico_sessoes
        if s.status == "Carregando"
    ]

    quantidade = len(sessoes_ativas)

    if quantidade == 0:
        return

    potencia = 7 / quantidade

    for sessao in sessoes_ativas:
        sessao.potencia_atual = potencia

def sessao_para_dict(sessao):
    return {
        "id_sessao": sessao.id_sessao,
        "cliente": sessao.cliente,
        "veiculo": sessao.veiculo,
        "carregador": sessao.carregador,
        "energia": sessao.energia,
        "energia_restante": sessao.energia_restante,
        "tarifa": sessao.tarifa,
        "custo": sessao.custo,
        "estorno": sessao.estorno,
        "tempo": sessao.tempo,
        "status": sessao.status,
        "progresso": sessao.progresso,
        "potencia_atual": sessao.potencia_atual
    }

def salvar_historico():
    with lock_persistencia:
        dados = [
            sessao_para_dict(sessao)
            for sessao in historico_sessoes
        ]

        salvar_sessoes(dados)

def carregar_historico():
    dados = carregar_sessoes()

    for item in dados:
        sessao = Sessao(
            item["id_sessao"],
            item["cliente"],
            item["veiculo"],
            item["carregador"],
            item["energia"],
            item["tarifa"],
            item["custo"],
            item["tempo"],
            item.get("estorno", 0.0)
        )

        sessao.energia_restante = item.get(
            "energia_restante", sessao.energia
        )
        sessao.status = item.get("status", "Concluída")
        sessao.progresso = item.get("progresso", 0)
        sessao.potencia_atual = item.get("potencia_atual", 7)

        # Uma recarga em andamento não pode continuar
        # automaticamente após reiniciar o programa.
        if sessao.status == "Carregando":
            sessao.status = "Interrompida"
            sessao.potencia_atual = 0

        historico_sessoes.append(sessao)

    salvar_historico()

    print(f"Histórico carregado: {len(historico_sessoes)} sessão(ões).")

def criar_sessao(cliente, veiculo, valor_recarga, carregador):
    if not cliente or not cliente.replace(" ", "").isalpha():
        raise ValueError("Nome do cliente inválido.")

    if veiculo not in veiculos:
        raise ValueError("Veículo inválido.")

    if valor_recarga <= 0:
        raise ValueError("O valor deve ser maior que zero.")

    if carregador not in carregadores:
        raise ValueError("Carregador inválido.")

    if carregadores[carregador] == "ocupado":
        raise ValueError("Este carregador já está em uso.")

    resultado = calcular_recarga(veiculo, valor_recarga)

    id_sessao = len(historico_sessoes) + 1

    sessao = Sessao(
        id_sessao,
        cliente,
        veiculo,
        carregador,
        resultado["energia_fornecida"],
        resultado["preco_kwh"],
        resultado["valor_utilizado"],
        resultado["tempo_horas"],
        resultado["estorno"]
    )

    historico_sessoes.append(sessao)
    sessoes_ativas.append(sessao)

    atualizar_potencia()
    carregadores[carregador] = "ocupado"

    salvar_historico()

    thread = threading.Thread(
        target=simular_recarga,
        args=(sessao,)
    )
    thread.daemon = True
    thread.start()

    return sessao

def nova_sessao():

    print("\n===== NOVA SESSÃO =====")

    while True:

        cliente = input(
            "Nome do cliente: "
        ).strip()

        if not cliente:
            print("Nome inválido.")
            continue

        if not cliente.replace(" ", "").isalpha():
            print(
                "Digite apenas letras."
            )
            continue

        break

    print("\nVeículos disponíveis:")

    lista_veiculos = list(veiculos.keys())

    for i, veiculo in enumerate(lista_veiculos, start=1):
        print(f"{i} - {veiculo}")

    while True:

        try:

            escolha = int(
                input("\nEscolha o veículo: ")
            )

            if 1 <= escolha <= len(lista_veiculos):
                break

            print("Veículo inválido.")

        except ValueError:
            print("Digite apenas números.")

    veiculo = lista_veiculos[escolha - 1]

    while True:

        try:

            valor_recarga = float(
                input("Valor da recarga (R$): ")
            )

            if valor_recarga > 0:
                break

            print("O valor deve ser maior que zero.")

        except ValueError:
            print("Digite um valor numérico válido.")

    while True:

        try:

            carregador = int(
                input("Carregador (1 a 4): ")
            )

            if carregador in [1, 2, 3, 4]:
                break

            print("Carregador inválido.")

        except ValueError:
            print("Digite apenas números.")

    try:
        sessao = criar_sessao(
            cliente,
            veiculo,
            valor_recarga,
            carregador
        )

        print("\nSessão criada com sucesso!")
        sessao.exibir()

    except ValueError as erro:
        print(f"\nErro: {erro}")

def listar_sessoes():

    print("\n===== SESSÕES CADASTRADAS =====")

    if len(historico_sessoes) == 0:

        print("Nenhuma sessão cadastrada.")
        return

    for sessao in historico_sessoes:
        sessao.exibir()

def buscar_sessao():

    print("\n===== BUSCAR SESSÃO =====")

    if len(historico_sessoes) == 0:
        print("Nenhuma sessão cadastrada.")
        return

    try:

        id_procurado = int(
            input("Digite o ID da sessão: ")
        )

    except ValueError:

        print("ID inválido.")
        return

    for sessao in historico_sessoes:

        if sessao.id_sessao == id_procurado:

            print("\nSessão encontrada!")
            sessao.exibir()
            return

    print("Nenhuma sessão encontrada.")

def buscar_sessao_por_id(id_procurado):
    for sessao in historico_sessoes:
        if sessao.id_sessao == id_procurado:
            return sessao

    return None

def ordenar_sessoes():

    print("\n===== ORDENAR SESSÕES =====")

    if len(historico_sessoes) == 0:
        print("Nenhuma sessão cadastrada.")
        return

    print("\nOrdenar por:")
    print("1 - ID")
    print("2 - Energia consumida")
    print("3 - Custo")
    print("4 - Tempo de recarga")

    opcao = input("\nEscolha: ")

    n = len(historico_sessoes)

    for i in range(n):

        for j in range(n - 1 - i):

            trocar = False

            if opcao == "1":

                # ID (crescente)

                if (
                        historico_sessoes[j].id_sessao >
                        historico_sessoes[j + 1].id_sessao
                ):
                    trocar = True

            elif opcao == "2":

                # Energia (decrescente)

                if (
                        historico_sessoes[j].energia <
                        historico_sessoes[j + 1].energia
                ):
                    trocar = True

            elif opcao == "3":

                # Custo (decrescente)

                if (
                        historico_sessoes[j].custo <
                        historico_sessoes[j + 1].custo
                ):
                    trocar = True

            elif opcao == "4":

                # Tempo (decrescente)

                if (
                        historico_sessoes[j].tempo <
                        historico_sessoes[j + 1].tempo
                ):
                    trocar = True

            else:
                print("Opção inválida.")
                return

            if trocar:

                historico_sessoes[j], historico_sessoes[j + 1] = (
                    historico_sessoes[j + 1],
                    historico_sessoes[j]
                )

    print("\nSessões ordenadas com sucesso!")

    listar_sessoes()

def ordenar_sessoes_por(campo):
    campos_validos = {
        "id": "id_sessao",
        "energia": "energia",
        "custo": "custo",
        "tempo": "tempo"
    }

    if campo not in campos_validos:
        raise ValueError("Campo de ordenação inválido.")

    sessoes_ordenadas = historico_sessoes.copy()
    atributo = campos_validos[campo]
    n = len(sessoes_ordenadas)

    for i in range(n):
        for j in range(n - 1 - i):
            valor_atual = getattr(sessoes_ordenadas[j], atributo)
            valor_seguinte = getattr(sessoes_ordenadas[j + 1], atributo)

            if campo == "id":
                trocar = valor_atual > valor_seguinte
            else:
                trocar = valor_atual < valor_seguinte

            if trocar:
                sessoes_ordenadas[j], sessoes_ordenadas[j + 1] = (
                    sessoes_ordenadas[j + 1],
                    sessoes_ordenadas[j]
                )

    return sessoes_ordenadas

def estatisticas():

    print("\n===== ESTATÍSTICAS =====")

    if len(historico_sessoes) == 0:
        print("Nenhuma sessão cadastrada.")
        return

    total_sessoes = len(historico_sessoes)

    energia_total = sum(
        sessao.energia
        for sessao in historico_sessoes
    )

    faturamento_total = sum(
        sessao.custo
        for sessao in historico_sessoes
    )

    ticket_medio = (
        faturamento_total / total_sessoes
    )

    maior_consumo = max(
        historico_sessoes,
        key=lambda s: s.energia
    )

    menor_consumo = min(
        historico_sessoes,
        key=lambda s: s.energia
    )

    print(f"\nTotal de Sessões: {total_sessoes}")

    print(
        f"Energia Total Fornecida: "
        f"{energia_total:.2f} kWh"
    )

    print(
        f"Faturamento Total: "
        f"R$ {faturamento_total:.2f}"
    )

    print(
        f"Ticket Médio: "
        f"R$ {ticket_medio:.2f}"
    )

    print(
        f"\nMaior Consumo:"
        f"\n{maior_consumo.cliente}"
        f" - {maior_consumo.energia:.2f} kWh"
    )

    print(
        f"\nMenor Consumo:"
        f"\n{menor_consumo.cliente}"
        f" - {menor_consumo.energia:.2f} kWh"
    )

def monitorar_carregamentos():

    print("\n===== MONITORAMENTO =====")

    existe_sessao = False

    for sessao in historico_sessoes:

        if sessao.status == "Carregando":

            existe_sessao = True

            print(
                f"\nCarregador: "
                f"{sessao.carregador}"
            )

            print(
                f"Cliente: "
                f"{sessao.cliente}"
            )

            print(
                f"Veículo: "
                f"{sessao.veiculo}"
            )

            print(
                f"Status: "
                f"{sessao.status}"
            )

            print(
                f"Potência Atual: "
                f"{sessao.potencia_atual:.2f} kW"
            )

            print(
                f"Energia Restante: "
                f"{sessao.energia_restante:.2f} kWh"
            )

            print(
                f"Progresso: "
                f"{sessao.progresso}%"
            )

    if not existe_sessao:

        print(
            "\nNenhuma recarga "
            "em andamento."
        )

def simular_recarga(sessao):
    while sessao.energia_restante > 0:
        potencia = sessao.potencia_atual

        if potencia <= 0:
            time.sleep(1)
            continue

        energia_carregada = potencia / 18

        sessao.energia_restante -= energia_carregada

        if sessao.energia_restante < 0:
            sessao.energia_restante = 0

        sessao.progresso = int(
            (
                (sessao.energia - sessao.energia_restante)
                / sessao.energia
            ) * 100
        )

        try:
            salvar_historico()
        except OSError as erro:
            print(
                f"\nAviso: não foi possível salvar o histórico: {erro}"
            )

        time.sleep(1)

    sessao.progresso = 100
    sessao.energia_restante = 0
    sessao.status = "Concluída"
    sessao.potencia_atual = 0

    atualizar_potencia()
    carregadores[sessao.carregador] = "disponivel"

    try:
        salvar_historico()
    except OSError as erro:
        print(
            f"\nAviso: recarga concluída, mas houve falha ao salvar: {erro}"
        )

    print(
        f"\n[Carregador {sessao.carregador}] Recarga concluída!"
    )

def executar_menu():
    while True:
        opcao = menu()

        if opcao == "1":
            nova_sessao()
        elif opcao == "2":
            listar_sessoes()
        elif opcao == "3":
            buscar_sessao()
        elif opcao == "4":
            ordenar_sessoes()
        elif opcao == "5":
            estatisticas()
        elif opcao == "6":
            monitorar_carregamentos()
        elif opcao == "7":
            print("\nEncerrando sistema...")
            break
        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    carregar_historico()
    executar_menu()
    
