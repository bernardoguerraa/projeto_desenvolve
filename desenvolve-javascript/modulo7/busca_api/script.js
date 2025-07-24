async function buscarUsuarios() {
  const termo = document.getElementById("inputBusca").value.trim();
  const lista = document.getElementById("listaUsuarios");
  const mensagem = document.getElementById("mensagemErro");

  lista.innerHTML = "";
  mensagem.textContent = "";

  if (termo === "") {
    mensagem.textContent = "Digite algo para buscar.";
    return;
  }

  try {
    const resposta = await fetch(`https://api.github.com/search/users?q=${termo}`);

    if (!resposta.ok) {
      throw new Error("Erro ao buscar dados.");
    }

    const dados = await resposta.json();

    if (dados.total_count === 0) {
      mensagem.textContent = "Não foram encontrados usuários para esta pesquisa.";
      return;
    }

    dados.items.forEach(usuario => {
      const item = document.createElement("li");
      item.innerHTML = `
        <img src="${usuario.avatar_url}" alt="Avatar de ${usuario.login}">
        <a href="${usuario.html_url}" target="_blank">${usuario.login}</a>
      `;
      lista.appendChild(item);
    });

  } catch (erro) {
    mensagem.textContent = "Erro ao buscar usuários.";
    console.error(erro);
  }
}
