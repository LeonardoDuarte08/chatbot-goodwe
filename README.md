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

### Sprint 4

Na Sprint 04, montamos um golden dataset com 20 perguntas e gabaritos para comparar duas versões do prompt do chatbot GoodWe. Usamos o Kaggle e a API Groq com LLM as a Judge. Foram feitas 40 avaliações, com médias de **9,65 para a v1** e **9,50 para a v2**. A v1 foi melhor no resultado geral, enquanto a v2 apresentou uma pequena vantagem nas perguntas de funcionalidade.

- [Notebook final da Sprint 04](notebooks/Sprint%2004.ipynb)
- [CSV com as 40 avaliações](docs/resultados/avaliacoes_sprint04.csv)
- [Relatório final em PDF](docs/Relatorio%20Sprint04.pdf)
- [Relatório em Markdown](docs/Relatorio_Sprint04.md)
- [Arquivo de entrega da Sprint 04](Entrega-Sprint04.txt)

Para executar o notebook, importe o arquivo no Kaggle, habilite o acesso à internet e configure o Secret `GROQ_API_KEY`.

## Estrutura do projeto

```text
chatbot-goodwe/
├── README.md
├── requirements.txt
├── .gitignore
├── entrega-sprint01.txt
├── Entrega-Sprint3.txt
├── Entrega-Sprint04.txt
├── context/
│   └── goodwe_context.txt
├── src/
│   ├── chatbot.py
│   └── main.py
├── notebooks/
│   ├── Sprint3_GoodWe_Agentes.ipynb
│   └── Sprint 04.ipynb
└── docs/
    ├── Relatorio_Sprint3_Prompt_and_Artificial_Intelligence.docx
    ├── Relatorio Sprint04.pdf
    ├── Relatorio_Sprint04.md
    ├── fluxograma.png
    ├── perguntas_teste.md
    └── resultados/
        ├── comparacao_modelos_sprint3.csv
        ├── resumo_modelos_sprint3.csv
        ├── testes_seguranca_sprint3.csv
        └── avaliacoes_sprint04.csv
```
