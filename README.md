# Chatbot GoodWe — EV Challenge 2026

## Integrantes

| Nome | RM |
|---|---|
| Eduardo Oliveira | 570374 |
| Timoteo de Andrade Romano | 569711 |
| Bruno Albuquerque Aguiar | 569035 |
| João Pedro Conturbia | 569788 |
| Enzo De Nadai | 569985 |
| Leonardo Duarte | 569029 |

## Descrição

Projeto de chatbot com Inteligência Artificial desenvolvido para auxiliar operadores, síndicos, moradores e técnicos com dúvidas relacionadas aos cenários ChargeGrid Intelligence e EV ChargeOps da GoodWe.

O projeto foi evoluído ao longo das Sprints, começando com um chatbot baseado em prompt e histórico de conversa e, na Sprint 3, passando a utilizar um framework de agentes, memória conversacional, tools, comparação entre modelos e mecanismos de segurança.

## Problema Abordado

A proposta busca apoiar o uso e a operação de eletropostos em dois cenários principais:

- **ChargeGrid Intelligence**: apoio ao gerenciamento de potência, ciclos de recarga, faturamento e operação de eletropostos comerciais.
- **EV ChargeOps**: apoio ao gerenciamento compartilhado de carregadores em condomínios, com controle de acesso e faturamento individual por unidade.

## Justificativa da Escolha do Contexto

Optamos por trabalhar com os dois contextos, comercial e condominial, porque eles representam situações diferentes de uso da solução.

O chatbot utiliza instruções de sistema para direcionar as respostas de acordo com o tipo de dúvida apresentada pelo usuário, buscando oferecer respostas adequadas ao contexto.

## Evolução do Projeto

### Sprint 1

Na primeira Sprint foi desenvolvida a estrutura inicial do chatbot, com:

- definição do problema;
- criação do contexto do projeto;
- elaboração do system prompt;
- definição das personas;
- estrutura inicial de perguntas e respostas.

### Sprint 2

Na Sprint 2 o chatbot foi evoluído com:

- histórico de conversa;
- estratégia de few-shot;
- melhorias nas respostas;
- conjunto de perguntas para teste;
- uso da API Groq com o modelo LLaMA 3.1 8B Instant.

### Sprint 3

Na Sprint 3 foram adicionados novos recursos ao projeto:

- uso de LangChain e LangGraph;
- implementação de agente;
- memória conversacional;
- uso de tools;
- execução local de modelos com Ollama;
- comparação entre Qwen3 8B e LLaMA 3.1 8B;
- avaliação de latência;
- avaliação de consumo de tokens;
- avaliação manual da qualidade das respostas;
- testes de segurança;
- aplicação de guardrails.

## Tecnologias Utilizadas

- Python
- LangChain
- LangGraph
- LangChain Ollama
- Ollama
- Pandas
- Requests
- Groq API
- LLaMA 3.1 8B
- Qwen3 8B

## Modelos Avaliados na Sprint 3

Foram utilizados dois modelos durante os testes:

- **Qwen3 8B**
- **LLaMA 3.1 8B**

Os dois modelos foram avaliados utilizando as mesmas perguntas aplicadas nas etapas anteriores do projeto.

### Resumo dos resultados

| Modelo | Nota média | Latência média | Tokens médios |
|---|---:|---:|---:|
| Qwen3 8B | 9,0 | 39,29 s | 1.438 |
| LLaMA 3.1 8B | 8,0 | 6,95 s | 1.017 |

O Qwen3 8B apresentou maior nota média nas respostas, enquanto o LLaMA 3.1 8B apresentou menor latência e menor consumo médio de tokens.

## Segurança

Foram realizados testes de segurança para verificar o comportamento do agente em situações fora do funcionamento esperado.

Os testes incluíram:

- tentativa de prompt injection;
- tentativa de mudança de papel;
- pergunta fora do escopo do projeto.

Nos três cenários o agente manteve as instruções definidas e apresentou o comportamento esperado.

## Personas Atendidas

- Operador comercial
- Síndico
- Morador
- Técnico

## Estrutura do Projeto

```text
chatbot-goodwe/
│
├── README.md
├── requirements.txt
├── .gitignore
├── entrega.txt
│
├── src/
│   ├── chatbot.py
│   └── main.py
│
├── notebooks/
│   └── Sprint3_GoodWe_Agentes.ipynb
│
├── context/
│   └── goodwe_context.txt
│
└── docs/
    ├── fluxograma.png
    ├── perguntas_teste.md
    ├── Relatorio_Sprint3_Prompt_and_Artificial_Intelligence.docx
    └── resultados/
        ├── comparacao_modelos_sprint3.csv
        ├── resumo_modelos_sprint3.csv
        └── testes_seguranca_sprint3.csv


### Sprint 4 — Avaliação automática (entrega final)

A Sprint 04 usa um golden dataset com 20 perguntas, avaliação via LLM as a Judge e comparação entre dois prompts no Kaggle. Foram feitas 40 avaliações, com notas médias de **9,65 (v1)** e **9,50 (v2)**.

- [Notebook final do Kaggle](notebooks/Sprint04_GoodWe_Kaggle.ipynb)
- [CSV final com as 40 avaliações](docs/resultados/avaliacoes_sprint04.csv)
- [Relatório final em Markdown](docs/Relatorio_Sprint04.md)

O relatório aprovado originalmente foi entregue em PDF. O Markdown disponibilizado no repositório reproduz seu conteúdo textual.
