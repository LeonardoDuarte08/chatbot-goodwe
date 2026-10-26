
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, urlsplit, quote
import os
import json

import main


HOST = "localhost"
PORTA = 8000

PASTA_PROJETO = Path(__file__).resolve().parent
os.chdir(PASTA_PROJETO)

# Recupera as sessões salvas antes de atender o navegador.
main.carregar_historico()


class EcoGridHandler(SimpleHTTPRequestHandler):

    
    def responder_json(self, dados, status=200):
        resposta = json.dumps(
            dados,
            ensure_ascii=False
        ).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(resposta)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(resposta)

    def do_GET(self):
        url = urlsplit(self.path)
        caminho = url.path
        parametros = parse_qs(url.query)

        if caminho == "/":
            self.path = "/templates/index.html"
            return super().do_GET()

        if caminho == "/buscar-sessao":
            try:
                id_procurado = int(
                    parametros.get("id", ["0"])[0]
                )

                sessao = main.buscar_sessao_por_id(id_procurado)

                if sessao is None:
                    self.responder_json({
                        "erro": "Sessão não encontrada."
                    }, 404)
                    return

                self.responder_json(
                    main.sessao_para_dict(sessao)
                )

            except ValueError:
                self.responder_json({
                    "erro": "Informe um ID válido."
                }, 400)

            return

        if caminho == "/ordenar-sessoes":
            campo = parametros.get("campo", ["id"])[0]

            try:
                sessoes = main.ordenar_sessoes_por(campo)

                dados = [
                    main.sessao_para_dict(sessao)
                    for sessao in sessoes
                ]

                self.responder_json(dados)

            except ValueError as erro:
                self.responder_json({
                    "erro": str(erro)
                }, 400)

            return

        return super().do_GET()

    
    def do_POST(self):
        caminho = urlsplit(self.path).path

        if caminho != "/criar-sessao":
            self.send_error(404, "Página não encontrada.")
            return

        tamanho = int(self.headers.get("Content-Length", 0))
        corpo = self.rfile.read(tamanho).decode("utf-8")
        dados = parse_qs(corpo)

        try:
            cliente = dados.get("cliente", [""])[0].strip()
            veiculo = dados.get("veiculo", [""])[0]
            valor_recarga = float(
                dados.get("valor_recarga", ["0"])[0]
            )
            carregador = int(
                dados.get("carregador", ["0"])[0]
            )

            sessao = main.criar_sessao(
                cliente,
                veiculo,
                valor_recarga,
                carregador
            )

            mensagem = (
                f"Sessão {sessao.id_sessao} criada com sucesso!"
            )

        except (ValueError, KeyError) as erro:
            mensagem = f"Erro: {erro}"

        self.send_response(303)
        self.send_header("Location", "/?mensagem=" + quote(mensagem))
        self.end_headers()


def iniciar_servidor():
    servidor = HTTPServer((HOST, PORTA), EcoGridHandler)

    print(f"EcoGrid CEV: http://{HOST}:{PORTA}")
    print("Pressione Ctrl+C para encerrar.")

    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
    finally:
        servidor.server_close()


if __name__ == "__main__":
    iniciar_servidor()
