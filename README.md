# EcoGrid CEV — Sistema de Recarga de Veículos Elétricos

**FIAP | GoodWe — EV Challenge 2026**

**CHATBOT + APLICAÇÃO DOS CARREGADORES**

| Nome | RM |
|---|---|
| Eduardo Oliveira | 570374 |
| Timoteo de Andrade Romano | 569711 |
| Bruno Albuquerque Aguiar | 569035 |
| João Pedro Conturbia | 569788 |
| Enzo De Nadai | 569985 |
| Leonardo Duarte | 569029 |

# Chatbot - Prompt and Artifical Intelligence

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
# Aplicação - Carregadores (EcoGrid)

## Sobre o projeto

Nosso projeto é um sistema para simular o gerenciamento de recargas de veículos elétricos. Nele, o usuário consegue selecionar um veículo e um carregador, informar o valor da recarga e consultar as sessões que já foram registradas.

A ideia foi montar algo que mostrasse, de forma prática, como organizar as recargas, calcular o consumo e o custo e acompanhar o uso dos carregadores. Não usamos carregadores físicos: toda a parte da recarga é simulada pelo sistema.

## Como organizamos o sistema

Separamos o projeto em uma interface web e a parte de processamento em Python. O HTML, CSS e JavaScript ficam responsáveis pelo que aparece na tela e pelas ações do usuário. Quando alguma operação é solicitada, o JavaScript faz a requisição ao servidor Python, que executa as regras do sistema.

Os principais arquivos são:

- `servidor.py`: inicia o servidor local e recebe as requisições da interface.
- `main.py`: controla as principais operações, como a criação e a consulta das recargas.
- `algoritmos.py`: faz os cálculos de energia, valor, tarifa e tempo estimado.
- `veiculos.py`: contém os dados dos veículos usados na simulação.
- `sessao.py`: organiza as informações de cada sessão.
- `persistencia.py`: salva e recupera as sessões no arquivo JSON.
- `templates/index.html`, `static/css/style.css` e `static/js/script.js`: formam a interface web.
- `dados/sessoes.json`: guarda o histórico de sessões.

O funcionamento, de forma resumida, é este:

```text
Usuário na página web
        |
        v
HTML, CSS e JavaScript
        |
        v
servidor.py
        |
        v
main.py ---> algoritmos.py / veiculos.py / sessao.py
        |
        v
persistencia.py ---> dados/sessoes.json
```

Também usamos uma simulação do andamento das recargas. As informações ficam registradas em JSON, então não precisamos de um banco de dados externo para demonstrar o projeto.

## Relação com o desafio GoodWe e com a matéria

O projeto se encaixa no desafio GoodWe porque trabalha com a recarga de veículos elétricos, mostrando questões como disponibilidade dos carregadores, consumo de energia e custo para o usuário.

Na matéria de Python, usamos listas e dicionários para organizar as informações, classes para representar as sessões e funções para fazer cálculos, buscas e ordenação dos registros. Assim, conseguimos aplicar no projeto o que vimos nas aulas.

## O que implementamos

Na versão entregue, temos:

- 4 carregadores cadastrados na simulação;
- 7 kW de potência de referência para os cálculos;
- 4 valores de tarifa por horário: R$ 1,50, R$ 2,00, R$ 2,80 e R$ 2,20 por kWh;
- cálculo de energia, custo, tempo estimado e possível estorno;
- histórico de sessões e informações para acompanhar o uso do sistema.

Esses valores fazem parte da configuração do protótipo. Não são medições de carregadores reais.

## Testes que fizemos

Depois de terminar o projeto, testamos se todas as recargas funcionavam do começo ao fim. Rodamos tudo em uma cópia separada, para não alterar os dados originais.

### Criando e finalizando recargas

No primeiro teste de recarga, usamos o **BYD Dolphin** e colocamos **R$ 10,00**. A sessão foi criada e o carregador ficou ocupado. Quando tentamos começar outra recarga nele, o sistema não deixou.

Depois iniciamos recargas nos **quatro carregadores ao mesmo tempo**, com veículos diferentes. O sistema dividiu os **7 kW** disponíveis em **1,75 kW por carregador**. Acompanhamos a simulação até as quatro sessões chegarem a **100%**, com a energia restante zerada. No final, todos os carregadores ficaram disponíveis de novo. Conseguimos iniciar outra recarga no carregador 1, mostrando que ele podia ser reutilizado.

### Conferindo os cálculos e os dados

Também testamos uma recarga com valor acima do necessário para completar a bateria. Nesse caso, o programa limitou a quantidade de energia à capacidade do veículo e calculou o **estorno** do dinheiro que sobrou.

Verificamos se as sessões eram salvas no arquivo JSON e se o histórico voltava quando carregávamos os dados novamente. Fizemos ainda um teste com uma recarga marcada como em andamento antes do reinício: ao recuperar o histórico, ela passou para **Interrompida**, em vez de aparecer como concluída.

### Validações

Testamos alguns dados errados de propósito: nome de cliente vazio, veículo não cadastrado, valor negativo e número de carregador inexistente. O sistema recusou essas tentativas. Também conseguimos buscar uma sessão pelo ID e ordenar os registros pelo custo.

| O que testamos | Resultado |
|---|---|
| Criar sessão e ocupar carregador | Funcionou |
| Tentar usar um carregador ocupado | Foi bloqueado |
| Usar os 4 carregadores juntos | Funcionou |
| Dividir 7 kW entre 4 recargas | 1,75 kW para cada uma |
| Finalizar as 4 recargas | Chegaram a 100% |
| Liberar carregadores ao finalizar | Todos ficaram disponíveis |
| Reutilizar um carregador | Funcionou |
| Valor maior que a capacidade da bateria | Energia limitada e estorno calculado |
| Dados inválidos de cliente, veículo, valor e carregador | Foram recusados |
| Salvar e recuperar o histórico em JSON | Funcionou |
| Recuperar recarga em andamento após reinício | Ficou como Interrompida |
| Buscar sessão e ordenar por custo | Funcionou |

No registro dos testes funcionais, tivemos **19 verificações aprovadas**. Esse número se refere aos testes de lógica do projeto, não a recargas reais. Também verificamos o acesso às páginas e às rotas HTTP em uma etapa separada.

Os testes ajudaram a confirmar que a criação, o acompanhamento e a finalização das recargas estão ligados ao controle dos carregadores e ao histórico. Ainda precisamos testar a interface com cliques reais em diferentes navegadores, situações com várias requisições chegando exatamente ao mesmo tempo e uma integração com equipamentos físicos.

## Sustentabilidade e inovação

Escolhemos trabalhar com recarga de veículos elétricos porque é um assunto ligado à mobilidade sustentável. Com as informações de consumo, custo e disponibilidade reunidas em um só sistema, fica mais fácil acompanhar as sessões e pensar em maneiras de organizar melhor o uso dos carregadores.

Um ponto interessante é a tarifa por horário. Ela permite simular como o custo muda dependendo do momento da recarga. No futuro, poderíamos usar informações reais de consumo e horários de maior demanda para melhorar essa parte.

Por enquanto, não temos dados suficientes para dizer que o projeto reduziu consumo de energia ou emissão de CO₂. Para medir isso, precisaríamos conectar o sistema a equipamentos reais e comparar os resultados. O que entregamos é um protótipo funcional para demonstrar a ideia.

## Tecnologias utilizadas

- **Python 3:** lógica do sistema e servidor HTTP.
- **HTML, CSS e JavaScript:** interface web.
- **JSON:** armazenamento local do histórico.
- **Bibliotecas do próprio Python:** recursos para servidor, arquivos, datas e execução da simulação.

Nesta versão não utilizamos sensores físicos, nem conexão direta com carregadores GoodWe. Também não usamos frameworks externos que precisem ser instalados para iniciar o sistema.

## Estrutura dos arquivos

```text
chatbot-goodwe/
Aplicação EcoGrid/
├── README.md
├── .gitignore
├── servidor.py
├── main.py
├── algoritmos.py
├── persistencia.py
├── sessao.py
├── veiculos.py
├── dados/
│   └── sessoes.json
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## Como executar

É necessário ter o Python 3 instalado. Depois, basta abrir um terminal na pasta do projeto e rodar:

```bash
python servidor.py
```

Com o servidor iniciado, abrimos no navegador:

`http://localhost:8000`

## O que podemos melhorar

Para uma próxima versão, queremos testar mais situações de uso ao mesmo tempo, melhorar as validações, adicionar testes automáticos e estudar uma integração com carregadores e dados reais. Também seria interessante substituir o arquivo JSON por um banco de dados se o sistema fosse usado com muitos registros.

## Referências

- [Documentação do Python](https://docs.python.org/3/)
- [MDN — HTML, CSS e JavaScript](https://developer.mozilla.org/)
- [Documentação do JSON (RFC 8259)](https://www.rfc-editor.org/rfc/rfc8259)
- [GoodWe](https://www.goodwe.com/)
