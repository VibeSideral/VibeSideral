const botoes = document.querySelectorAll('.botao');

const personagens = document.querySelectorAll('.personagem');

botoes.forEach((botao, indice) => {
    botoes.addEventListener("click", () => {
        removerSelecaoBotao();
        selecionarBotao(botao);

        removerSelecaoPersonagem();
        selecionarPersonagem(indice);
    });
});

function removerSelecaoBotao() {
    const botaoSelecionado = document.querySelector('.botao.selecionado');
    if (botaoSelecionado) {
        botaoSelecionado.classList.remove('selecionado');
    }
}

function selecionarBotao(botao) {
    botao.classList.add('selecionado');
}

function removerSelecaoPersonagem() {
    const personagemSelecionado = document.querySelector('.personagem.selecionado');
    if (personagemSelecionado) {
        personagemSelecionado.classList.remove('selecionado');
    }
}

function selecionarPersonagem(indice) {
    personagens[indice].classList.add('selecionado');
}

