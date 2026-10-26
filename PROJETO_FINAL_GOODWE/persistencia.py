
import json
import os
import tempfile
import time
from pathlib import Path

PASTA_PROJETO = Path(__file__).resolve().parent
ARQUIVO_SESSOES = PASTA_PROJETO / "dados" / "sessoes.json"


def carregar_sessoes():
    if not ARQUIVO_SESSOES.exists():
        return []

    try:
        with open(ARQUIVO_SESSOES, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        if not isinstance(dados, list):
            raise ValueError("O arquivo precisa conter uma lista.")

        return dados

    except (json.JSONDecodeError, ValueError) as erro:
        raise ValueError(
            f"Não foi possível carregar as sessões: {erro}"
        ) from erro


def salvar_sessoes(sessoes):
    ARQUIVO_SESSOES.parent.mkdir(parents=True, exist_ok=True)

    arquivo_temporario = None

    try:
        # Cria um temporário exclusivo na mesma pasta do JSON.
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            suffix=".tmp",
            prefix="sessoes_",
            dir=ARQUIVO_SESSOES.parent,
            delete=False
        ) as arquivo:
            arquivo_temporario = Path(arquivo.name)

            json.dump(
                sessoes,
                arquivo,
                ensure_ascii=False,
                indent=4
            )

            arquivo.flush()
            os.fsync(arquivo.fileno())

        # Tenta novamente caso o Windows bloqueie temporariamente o arquivo.
        for tentativa in range(10):
            try:
                os.replace(arquivo_temporario, ARQUIVO_SESSOES)
                arquivo_temporario = None
                return

            except PermissionError:
                if tentativa == 9:
                    raise

                time.sleep(0.2 * (tentativa + 1))

    finally:
        # Remove o temporário se a gravação não for concluída.
        if (
            arquivo_temporario is not None
            and arquivo_temporario.exists()
        ):
            try:
                arquivo_temporario.unlink()
            except OSError:
                pass
