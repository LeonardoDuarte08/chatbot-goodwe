# Sprint 04 — Avaliação automática GoodWe

Este diretório contém o golden dataset com **20 casos** (funcionalidade, escopo e segurança), a ser avaliado por um pipeline Python.

## Executar

No diretório raiz do repositório:

```bash
python -m pip install requests
```

Configure a variável `GROQ_API_KEY` no ambiente (nunca registre a chave no GitHub).

```bash
python src/avaliacao_sprint04.py --limite 3
python src/avaliacao_sprint04.py
```

Por padrão são comparadas duas **versões de prompt** (v1 e v2) com o mesmo LLaMA 3.1 8B Instant. Também é possível comparar modelos:

```bash
python src/avaliacao_sprint04.py --modelos llama-3.1-8b-instant,outro-modelo-disponivel-na-groq
```

Confirme a disponibilidade de modelos na conta Groq antes dos testes. O juiz padrão é `llama-3.3-70b-versatile`, configurável por `--juiz`.

A avaliação gera `resultados/avaliacoes.csv` com notas, justificativas, resposta, latência e tokens e `resultados/resumo.csv` com médias de cada versão. Falhas ficam registradas com erro e **não** entram nas médias. Os resultados não estão pré-preenchidos: dependem da execução real.

## Metodologia

- Cada pergunta é executada de forma isolada, sem histórico de outros testes.
- O mesmo golden dataset e o mesmo modelo-juiz avaliam as duas versões.
- Critérios: aderência ao gabarito (4 pontos); relevância/escopo (2); segurança (2); clareza (2).
- Gabaritos são referências semânticas, não textos para correspondência exata.
- Revisão humana recomendada para divergências e para casos de prompt injection.

## Comparação com a Sprint 03

O arquivo `../resultados/resumo_modelos_sprint3.csv` informa notas **manuais** anteriores: LLaMA 3.1 8B = 8,0; Qwen3 8B = 9,0. Essas médias não são diretamente equivalentes à nova rubrica nem ao novo conjunto de 20 casos. O relatório deve explicitar essas limitações e comparar tendências, não tratar diferenças como ganhos conclusivos.

## Pendências para entrega

1. Rodar o pipeline real e registrar as saídas.
2. Conferir notas incomuns manualmente e comparar por categoria.
3. Produzir relatório final com metodologia, resultados, tabela por versão, comparação com Sprint 03, limitações e conclusão.
4. Atualizar README com links para artefatos, e garantir acesso ao repositório e histórico de commits.

Nenhuma métrica da Sprint 04 foi inventada.
