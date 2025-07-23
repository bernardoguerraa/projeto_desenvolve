let estoque = [];

function adicionarLivro(titulo, autor, quantidade) {
  for (let livro of estoque) {
    if (livro.titulo === titulo) {
      console.log("Livro já existe no estoque.");
      return;
    }
  }

  estoque.push({ titulo, autor, quantidade });
  console.log(`Livro "${titulo}" adicionado com sucesso.`);
}

function removerLivro(titulo) {
  const index = estoque.findIndex(livro => livro.titulo === titulo);
  if (index !== -1) {
    estoque.splice(index, 1);
    console.log(`Livro "${titulo}" removido do estoque.`);
  } else {
    console.log("Livro não encontrado.");
  }
}

function atualizarQuantidade(titulo, novaQuantidade) {
  for (let livro of estoque) {
    if (livro.titulo === titulo) {
      livro.quantidade = novaQuantidade;
      console.log(`Quantidade do livro "${titulo}" atualizada para ${novaQuantidade}.`);
      return;
    }
  }
  console.log("Livro não encontrado.");
}

function listarLivros() {
  if (estoque.length === 0) {
    console.log("Estoque vazio.");
    return;
  }

  console.log("Livros no estoque:");
  for (let livro of estoque) {
    console.log(`Título: ${livro.titulo}, Autor: ${livro.autor}, Quantidade: ${livro.quantidade}`);
  }
}
