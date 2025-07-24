const curtidas = [];

function curtir() {
  const input = document.getElementById("nomeInput");
  const nome = input.value.trim();

  if (nome === "") return;

  if (!curtidas.includes(nome)) {
    curtidas.push(nome);
  }

  atualizarMensagem();
  input.value = "";
}

function atualizarMensagem() {
  const p = document.getElementById("mensagemCurtidas");

  if (curtidas.length === 0) {
    p.textContent = "Ninguém curtiu";
  } else if (curtidas.length === 1) {
    p.textContent = `${curtidas[0]} curtiu`;
  } else {
    const lista = curtidas.slice(0, curtidas.length - 1).join(", ");
    const ultimo = curtidas[curtidas.length - 1];
    p.textContent = `${lista} e ${ultimo} curtiram`;
  }
}
