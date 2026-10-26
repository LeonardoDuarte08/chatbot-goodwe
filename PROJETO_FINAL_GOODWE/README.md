# EcoGrid CEV — Sistema de Recarga de Veículos Elétricos

**FIAP | GoodWe — EV Challenge 2026**

## Integrantes
- Eduardo Oliveira — RM 570374
- Timoteo — RM 569711
- Bruno — RM 569035
- João Pedro — RM 569788
- Enzo — RM 569985
- Leonardo Duarte — RM 569029

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
projeto-final-goodwe/
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
