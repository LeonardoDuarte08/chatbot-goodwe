# Relatório — Sprint 04 | Prompt and Artificial Intelligence

**Projeto:** Chatbot GoodWe — EV Challenge 2026  
**Turma:** Ciência da Computação — 1º ano, 2026.2

## 1. Objetivo

A Sprint 04 dá continuidade ao agente conversacional das Sprints 1, 2 e 3, incorporando avaliação automatizada e reproduzível. O objetivo é identificar qual versão do agente responde melhor às perguntas dos usuários da GoodWe, considerando conteúdo, escopo, segurança e clareza.

## 2. Golden dataset

Foi construído o arquivo `golden_dataset.csv` com 20 perguntas, respostas esperadas, categorias e personas. Os casos abrangem o ChargeGrid Intelligence para operação comercial e o EV ChargeOps para condomínios. As categorias incluem funcionalidade, escopo e segurança. Foram incluídas questões de funcionamento habitual, assuntos fora de escopo, tentativas de prompt injection, pedidos de dados pessoais e recomendações elétricas inseguras.

## 3. Pipeline e critérios

Foi implementado o script `src/avaliacao_sprint04.py`, que executa cada caso de forma independente para duas versões do agente (v1 e v2), coleta resposta, duração e tokens, e envia a resposta com a pergunta e o gabarito a um terceiro modelo, no método **LLM as a Judge**.

Critérios (total: 10 pontos):
- Aderência ao gabarito: 0 a 4;
- Relevância e respeito ao escopo: 0 a 2;
- Segurança: 0 a 2;
- Clareza: 0 a 2.

O avaliador produz nota e justificativa em JSON. O script salva as avaliações individuais e o resumo por versão em CSV. Erros são reportados, mas não entram nas médias. As duas versões compartilham o mesmo contexto e conjunto de perguntas. A v2 adiciona instruções de concisão, separação de cenários e recusa a inventar informações.

## 4. Resultados quantitativos

**Pendente de execução real** com uma chave Groq válida. Preencher com os arquivos `resultados/avaliacoes.csv` e `resultados/resumo.csv` depois de executar o script.

| Métrica | Versão 1 | Versão 2 |
|---|---|---|
| Casos executados | A preencher | A preencher |
| Casos avaliados sem erro | A preencher | A preencher |
| Nota média (0–10) | A preencher | A preencher |
| Latência média (s) | A preencher | A preencher |
| Tokens médios | A preencher | A preencher |

Também apresentar um quadro de pontuação por categoria (funcionalidade, escopo, segurança) e exemplos de pelo menos uma concordância e uma divergência do juiz.

## 5. Comparação com a Sprint 03

A Sprint 03 avaliou manualmente os modelos locais:
- LLaMA 3.1 8B: nota média **8,0**, latência média **6,95 s**, tokens médios **1.017**.
- Qwen3 8B: nota média **9,0**, latência média **39,29 s**, tokens médios **1.438**.

A Sprint 04 compara inicialmente duas versões de instruções, usando o LLaMA 3.1 8B Instant via Groq; portanto, há diferenças de modelo, infraestrutura, perguntas e rubrica. **As notas não são diretamente comparáveis**, e a comparação com a Sprint 03 deve ser tratada como análise qualitativa de tendências. Após a execução, incluir exemplos concretos de divergência e limitações do juiz.

## 6. Limitações e recomendações

A avaliação automática pode produzir julgamentos inconsistentes e não substitui revisão humana. Tempo e consumo de tokens dependem da infraestrutura e do modelo escolhido. Os gabaritos são referências semânticas, e respostas corretas podem adotar formulações diferentes. Para futuras melhorias, recomenda-se ampliar os testes, revisar manualmente os casos com maior divergência e versionar dataset, prompts e resultados.

## 7. Conclusão

O projeto passou a ter uma estrutura para avaliação automática, com dataset separado do agente, critérios explícitos e armazenamento de resultados por versão. **A conclusão sobre qual versão foi superior depende da execução e análise dos resultados reais.**

## Como reproduzir

Na raiz do projeto:

```bash
python -m pip install requests
python src/avaliacao_sprint04.py --limite 3
python src/avaliacao_sprint04.py
```

Defina antes a variável de ambiente `GROQ_API_KEY`. Nunca publique a chave.

**Observação de entrega:** Este texto é uma base verificável. As seções de resultados e conclusão comparativa precisam ser completadas depois da execução; não representam métricas já coletadas.
