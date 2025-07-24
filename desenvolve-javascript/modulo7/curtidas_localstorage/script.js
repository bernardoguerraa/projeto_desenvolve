let curtidas = [];

// Carrega nomes do localStorage ao iniciar
window.onload = function () {
  const dadosSalvos = localStorage.getItem("curtidas");
  if (dadosSalvos) {
    curtidas = JSON.parse(dadosSalvos);
    atualizarMensagem();
  }
};

function curtir() {
  const input = document.getElementById("nomeInput");
  const nome = input.value.trim();

  if (nome === "") return;

  if (!curtidas.includes(nome)) {
    curtidas.push(nome);
    localStorage.setItem("curtidas", JSON.stringify(curtidas));
  }

  atualizarMensagem();
  input.value = "";
}

function limpar() {
  curtidas = [];
  localStorage.removeItem("curtidas");
  atualizarMensagem();
}

function atualizarMensagem() {
  const p = document.getElementById("mensagemCurtidas");

  if (curtidas.length === 0) {
    p.textContent = "Ninguém curtiu";
  } else if (curtidas.length === 1) {
    p.textContent = `${curtidas[0]} curtiu`;
  } else if (curtidas.length === 2) {
    p.textContent = `${curtidas[0]} e ${curtidas[1]} curtiram`;
  } else {
    const restantes = curtidas.length - 2;
    p.textContent = `${curtidas[0]}, ${curtidas[1]} e mais ${restantes} pessoa${restantes > 1 ? "s" : ""} curtiram`;
  }
}
