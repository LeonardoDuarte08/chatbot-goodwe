
const parametros = new URLSearchParams(window.location.search);
const mensagem = parametros.get("mensagem");
const elementoMensagem = document.getElementById("mensagem");

if (mensagem && elementoMensagem) {
    elementoMensagem.textContent = mensagem;
    elementoMensagem.style.color = mensagem.startsWith("Erro:")
        ? "#b91c1c"
        : "#166534";

    window.history.replaceState({}, document.title, "/");
}

let idBuscaAtivo = null;
let campoOrdenacao =
    document.getElementById("ordenar-por")?.value || "id";

const POTENCIA_TOTAL = 7;

function formatarNumero(valor) {
    return Number(valor || 0).toLocaleString("pt-BR", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
}

function formatarMoeda(valor) {
    return Number(valor || 0).toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL"
    });
}

async function atualizarPainel() {
    try {
        const resposta = await fetch(
            `/dados/sessoes.json?t=${Date.now()}`,
            { cache: "no-store" }
        );

        if (!resposta.ok) {
            throw new Error("Não foi possível carregar as sessões.");
        }

        const sessoes = await resposta.json();

        atualizarIndicadores(sessoes);
        atualizarRelatorio(sessoes);
        atualizarCarregadores(sessoes);
        await atualizarTabelaAtual(sessoes);
    } catch (erro) {
        console.error("Erro ao atualizar o painel:", erro);
    }
}

function atualizarIndicadores(sessoes) {
    const totalElemento = document.getElementById("total-sessoes");
    const ativasElemento = document.getElementById("sessoes-ativas");
    const energiaElemento = document.getElementById("energia-total");
    const faturamentoElemento = document.getElementById("faturamento-total");

    if (
        !totalElemento ||
        !ativasElemento ||
        !energiaElemento ||
        !faturamentoElemento
    ) {
        console.error("Indicadores não encontrados no HTML.");
        return;
    }

    const totalEnergia = sessoes.reduce(
        (total, sessao) => total + Number(sessao.energia || 0),
        0
    );

    const faturamento = sessoes.reduce(
        (total, sessao) => total + Number(sessao.custo || 0),
        0
    );

    const ativas = sessoes.filter(
        sessao => sessao.status === "Carregando"
    ).length;

    totalElemento.textContent = sessoes.length;
    ativasElemento.textContent = ativas;
    energiaElemento.textContent = `${formatarNumero(totalEnergia)} kWh`;
    faturamentoElemento.textContent = formatarMoeda(faturamento);
}


function atualizarRelatorio(sessoes) {
    const concluidasElemento = document.getElementById(
        "relatorio-concluidas"
    );
    const interrompidasElemento = document.getElementById(
        "relatorio-interrompidas"
    );
    const estornosElemento = document.getElementById(
        "relatorio-estornos"
    );
    const ticketMedioElemento = document.getElementById(
        "relatorio-ticket-medio"
    );
    const maiorVeiculoElemento = document.getElementById(
        "relatorio-maior-veiculo"
    );
    const maiorConsumoElemento = document.getElementById(
        "relatorio-maior-consumo"
    );

    const concluidas = sessoes.filter(
        sessao => sessao.status === "Concluída"
    ).length;

    const statusInterrompidos = [
        "Interrompida",
        "Interrompido",
        "Cancelada",
        "Cancelado"
    ];

    const interrompidas = sessoes.filter(
        sessao => statusInterrompidos.includes(sessao.status)
    ).length;

    const totalEstornos = sessoes.reduce(
        (total, sessao) => total + Number(sessao.estorno || 0),
        0
    );

    const faturamentoLiquido = sessoes.reduce(
        (total, sessao) => total + Number(sessao.custo || 0),
        0
    );

    const ticketMedio = sessoes.length > 0
        ? faturamentoLiquido / sessoes.length
        : 0;

    // Soma a energia consumida por cada modelo de veículo.
    const consumoPorVeiculo = {};

    sessoes.forEach(sessao => {
        const veiculo = sessao.veiculo || "Veículo não informado";
        const energia = Number(sessao.energia || 0);

        consumoPorVeiculo[veiculo] =
            (consumoPorVeiculo[veiculo] || 0) + energia;
    });

    const veiculos = Object.entries(consumoPorVeiculo);

    veiculos.sort((a, b) => b[1] - a[1]);

    const maiorVeiculo = veiculos.length > 0
        ? veiculos[0]
        : null;

    // Identifica a sessão individual com maior consumo.
    const maiorSessao = sessoes.reduce(
        (maior, sessao) => {
            if (!maior || Number(sessao.energia || 0) >
                Number(maior.energia || 0)) {
                return sessao;
            }

            return maior;
        },
        null
    );

    if (concluidasElemento) {
        concluidasElemento.textContent = concluidas;
    }

    if (interrompidasElemento) {
        interrompidasElemento.textContent = interrompidas;
    }

    if (estornosElemento) {
        estornosElemento.textContent = formatarMoeda(totalEstornos);
    }

    if (ticketMedioElemento) {
        ticketMedioElemento.textContent = formatarMoeda(ticketMedio);
    }

    if (maiorVeiculoElemento) {
        maiorVeiculoElemento.textContent = maiorVeiculo
            ? `${maiorVeiculo[0]} (${formatarNumero(maiorVeiculo[1])} kWh)`
            : "Nenhum registro";
    }

    if (maiorConsumoElemento) {
        maiorConsumoElemento.textContent = maiorSessao
            ? `${formatarNumero(maiorSessao.energia)} kWh`
            : "0,00 kWh";
    }
}


function atualizarPotencia(sessoes) {
    const totalElemento = document.getElementById("potencia-total");
    const disponivelElemento = document.getElementById("potencia-disponivel");

    const sessoesAtivas = sessoes.filter(
        sessao => sessao.status === "Carregando"
    );

    const quantidade = sessoesAtivas.length;

    const potenciaIndividual = quantidade > 0
        ? 7 / quantidade
        : 7;

    if (totalElemento) {
        totalElemento.textContent = `${formatarNumero(7)} kW`;
    }

    if (disponivelElemento) {
        disponivelElemento.textContent =
            `${formatarNumero(potenciaIndividual)} kW`;
    }
}

function atualizarCarregadores(sessoes) {
    const elemento = document.getElementById("lista-carregadores");

    if (!elemento) {
        console.error("Elemento lista-carregadores não encontrado no HTML.");
        return;
    }

    atualizarPotencia(sessoes);
    elemento.replaceChildren();

    for (let numero = 1; numero <= 4; numero++) {
        const sessao = sessoes.find(
            item =>
                Number(item.carregador) === numero &&
                item.status === "Carregando"
        );

        const card = document.createElement("div");
        card.className = "card";

        const titulo = document.createElement("h3");
        titulo.textContent = `Carregador ${numero}`;

        const status = document.createElement("p");
        status.textContent = sessao ? "Carregando" : "Disponível";

        const detalhes = document.createElement("p");
        detalhes.textContent = sessao
            ? `${sessao.cliente} — ${sessao.veiculo}`
            : "Pronto para uma nova recarga";

        const barra = document.createElement("progress");
        barra.max = 100;
        barra.value = sessao
            ? Math.min(100, Math.max(0, Number(sessao.progresso) || 0))
            : 0;
        barra.style.width = "100%";
        barra.style.display = "block";
        barra.style.marginTop = "12px";

        const percentual = document.createElement("p");
        percentual.textContent = sessao
            ? `${barra.value}% concluído`
            : "0% concluído";

        card.append(titulo, status, detalhes);

        if (sessao) {
            const energia = document.createElement("p");
            energia.textContent =
                `Energia: ${formatarNumero(sessao.energia)} kWh`;

            const potencia = document.createElement("p");
            potencia.textContent =
                `Potência atual: ${formatarNumero(sessao.potencia_atual)} kW`;

            const custo = document.createElement("p");
            custo.textContent =
                `Valor utilizado: ${formatarMoeda(sessao.custo)}`;

            const estorno = document.createElement("p");
            estorno.textContent =
                `Estorno: ${formatarMoeda(sessao.estorno)}`;

            card.append(energia, potencia, custo, estorno);
        }

        card.append(barra, percentual);
        elemento.appendChild(card);
    }
}

async function atualizarTabelaAtual(sessoes) {
    if (idBuscaAtivo !== null) {
        try {
            const resposta = await fetch(
                `/buscar-sessao?id=${encodeURIComponent(idBuscaAtivo)}&t=${Date.now()}`,
                { cache: "no-store" }
            );

            const dados = await resposta.json();

            if (!resposta.ok) {
                atualizarTabela([]);
                mostrarMensagemSessoes(
                    dados.erro || "Sessão não encontrada.",
                    true
                );
                return;
            }

            atualizarTabela([dados]);
            mostrarMensagemSessoes(
                `Exibindo a sessão ${idBuscaAtivo}.`,
                false
            );
        } catch (erro) {
            console.error("Erro ao buscar sessão:", erro);
        }

        return;
    }

    try {
        const resposta = await fetch(
            `/ordenar-sessoes?campo=${encodeURIComponent(campoOrdenacao)}&t=${Date.now()}`,
            { cache: "no-store" }
        );

        const dados = await resposta.json();

        if (!resposta.ok) {
            throw new Error(
                dados.erro || "Não foi possível ordenar as sessões."
            );
        }

        atualizarTabela(dados);
    } catch (erro) {
        console.error("Erro ao ordenar sessões:", erro);
        atualizarTabela(sessoes);
    }
}

function atualizarTabela(sessoes) {
    const corpo = document.getElementById("tabela-sessoes");

    if (!corpo) {
        console.error("Elemento tabela-sessoes não encontrado no HTML.");
        return;
    }

    corpo.replaceChildren();

    if (sessoes.length === 0) {
        const linha = document.createElement("tr");
        const celula = document.createElement("td");

        celula.colSpan = 8;
        celula.textContent = "Nenhuma sessão encontrada.";

        linha.appendChild(celula);
        corpo.appendChild(linha);
        return;
    }

    sessoes.forEach(sessao => {
        const linha = document.createElement("tr");

        const valores = [
            sessao.id_sessao,
            sessao.cliente,
            sessao.veiculo,
            sessao.carregador,
            `${formatarNumero(sessao.energia)} kWh`,
            formatarMoeda(sessao.estorno),
            sessao.status,
            `${Number(sessao.progresso || 0)}%`
        ];

        valores.forEach(valor => {
            const celula = document.createElement("td");
            celula.textContent = valor ?? "-";
            linha.appendChild(celula);
        });

        corpo.appendChild(linha);
    });
}

function mostrarMensagemSessoes(texto, erro) {
    const elemento = document.getElementById("mensagem-sessoes");

    if (!elemento) {
        return;
    }

    elemento.textContent = texto;
    elemento.style.color = erro ? "#b91c1c" : "#166534";
}

const formularioBusca = document.getElementById("form-busca");
const campoBusca = document.getElementById("buscar-id");
const botaoLimpar = document.getElementById("limpar-busca");
const seletorOrdenacao = document.getElementById("ordenar-por");

if (formularioBusca && campoBusca) {
    formularioBusca.addEventListener("submit", async evento => {
        evento.preventDefault();

        const id = Number(campoBusca.value);

        if (!Number.isInteger(id) || id < 1) {
            mostrarMensagemSessoes("Informe um ID válido.", true);
            return;
        }

        idBuscaAtivo = id;
        await atualizarTabelaAtual([]);
    });
}

if (botaoLimpar) {
    botaoLimpar.addEventListener("click", async () => {
        idBuscaAtivo = null;

        if (campoBusca) {
            campoBusca.value = "";
        }

        mostrarMensagemSessoes("", false);
        await atualizarPainel();
    });
}

if (seletorOrdenacao) {
    seletorOrdenacao.addEventListener("change", async () => {
        campoOrdenacao = seletorOrdenacao.value;
        idBuscaAtivo = null;

        if (campoBusca) {
            campoBusca.value = "";
        }

        mostrarMensagemSessoes("", false);
        await atualizarPainel();
    });
}

atualizarPainel();
setInterval(atualizarPainel, 2000);
