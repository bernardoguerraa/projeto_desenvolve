package modulo2.biblioteca;

import java.util.Date;
import java.util.Calendar; 

public class Main {
    public static void main(String[] args) {

        // 1. Criar um Autor
        Autor jessicaFelix = new Autor("Jessica Felix", "Brasileira");

        // Criar um Livro
        // No construtor de Livro, ele já se associa ao autor.
        Livro javaForBeginners = new Livro("Java for Beginners", jessicaFelix, "Tecnologia");
        System.out.println("DEBUG: Livro '" + javaForBeginners.getTitulo() + "' criado. Disponível: " + javaForBeginners.isDisponivel());

        //Criar Usuários
        Usuario lucasRafael = new Usuario("Lucas Rafael", 25);
        Usuario mariaSilva = new Usuario("Maria Silva", 30); 

        //Configurar as datas para o empréstimo
        Calendar cal = Calendar.getInstance(); // Obtém a data e hora atuais
        Date dataRetirada = cal.getTime();

        cal.add(Calendar.DAY_OF_MONTH, 7); // Adiciona 7 dias para a data de devolução
        Date dataDevolucao = cal.getTime();

        Emprestimo emprestimoLucas = null;

        // Primeiro Empréstimo
        System.out.println("\n--- Realizando o primeiro empréstimo (Lucas Rafael) ---");
        try {
            emprestimoLucas = new Emprestimo(javaForBeginners, lucasRafael, dataRetirada, dataDevolucao);
            System.out.println("Empréstimo de '" + javaForBeginners.getTitulo() + "' para " + lucasRafael.getNome() + " realizado com sucesso!");

            // Imprimir os detalhes do empréstimo bem-sucedido
            System.out.println("\nDetalhes do Empréstimo:");
            System.out.println("Livro: " + emprestimoLucas.getLivro().getTitulo());
            System.out.println("Autor: " + emprestimoLucas.getLivro().getAutor().getNome());
            System.out.println("Genero: " + emprestimoLucas.getLivro().getGenero());
            System.out.println("Usuario: " + emprestimoLucas.getUsuario().getNome());
            System.out.println("Idade: " + emprestimoLucas.getUsuario().getIdade());
            System.out.println("Data de Retirada: " + emprestimoLucas.getDataRetirada());
            System.out.println("Data de Devolucao: " + emprestimoLucas.getdataDevolucao());
            System.out.println("DEBUG: Livro '" + javaForBeginners.getTitulo() + "' agora disponível: " + javaForBeginners.isDisponivel());

        } catch (IllegalArgumentException e) {
            System.err.println("Erro ao realizar empréstimo para Lucas Rafael: " + e.getMessage());
        }

        // Segundo Empréstimo
        System.out.println("\n--- Tentando emprestar o mesmo livro ('" + javaForBeginners.getTitulo() + "') para " + mariaSilva.getNome() + " ---");
        try {
            Emprestimo emprestimoMaria = new Emprestimo(javaForBeginners, mariaSilva, new Date(), new Date());
            System.out.println("DEBUG: Empréstimo para Maria Silva realizado com sucesso (Isso não deveria acontecer!).");
        } catch (IllegalArgumentException e) {
            //Esta é a saída esperada para demonstrar a validação
            System.out.println(e.getMessage());
        }

        // Exemplo: Devolver o livro e verificar a disponibilidade novamente
        System.out.println("\n--- Simulando devolução do livro por Lucas Rafael ---");
        if (emprestimoLucas != null) {
            emprestimoLucas.finalizarEmprestimo();
            System.out.println("DEBUG: Livro '" + javaForBeginners.getTitulo() + "' agora disponível: " + javaForBeginners.isDisponivel());
        }

        //Agora, se tentar um terceiro empréstimo, ele va funcionar
        System.out.println("\n--- Tentando emprestar o livro ('" + javaForBeginners.getTitulo() + "') novamente, após devolução ---");
        try {
            Emprestimo emprestimoTerceiro = new Emprestimo(javaForBeginners, mariaSilva, new Date(), new Date());
            System.out.println("Empréstimo de '" + javaForBeginners.getTitulo() + "' para " + mariaSilva.getNome() + " realizado com sucesso APÓS A DEVOLUÇÃO!");
        } catch (IllegalArgumentException e) {
            System.err.println("Erro inesperado após devolução: " + e.getMessage());
        }
    }
}
    
