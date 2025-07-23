function trocarCorTitulo() {
  const titulo = document.getElementById("titulo");
  titulo.style.color = gerarCorAleatoria();
}

function trocarCorLista() {
  const itens = document.querySelectorAll("ul li");
  const novaCor = gerarCorAleatoria();
  itens.forEach(item => {
    item.style.color = novaCor;
  });
}

function trocarCorParagrafos() {
  const paragrafos = document.querySelectorAll("p");
  const novaCor = gerarCorAleatoria();
  paragrafos.forEach(p => {
    p.style.color = novaCor;
    p.classList.add("paragrafo-estilizado");
  });
}

function trocarCorFundo() {
  document.body.style.backgroundColor = gerarCorAleatoria();
}

function gerarCorAleatoria() {
  // Retorna uma cor hexadecimal aleatória
  const letras = "0123456789ABCDEF";
  let cor = "#";
  for (let i = 0; i < 6; i++) {
    cor += letras[Math.floor(Math.random() * 16)];
  }
  return cor;
}
