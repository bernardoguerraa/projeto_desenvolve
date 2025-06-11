package modulo2.biblioteca;
import java.util.ArrayList;
import java.util.List;


public class Usuario extends Pessoa{
    private int idade;
    private List<Emprestimo> historicoEmprestimos;

    public Usuario(String nome, int idade){
        super(nome);
        this.idade = idade;
        this.historicoEmprestimos = new ArrayList<>();
    }

    public int getIdade(){
        return idade;
    }

    public void setIdade(int idade){
        this.idade=idade;
    }

    public List<Emprestimo> getHistoricoEmprestimos(){
        return historicoEmprestimos;
    }

    public void adicionarEmprestimo(Emprestimo emprestimo) {
        if (emprestimo != null) { // Ainda é bom verificar se o empréstimo não é nulo
            this.historicoEmprestimos.add(emprestimo);
            System.out.println("DEBUG: Empréstimo do livro '" + emprestimo.getLivro().getTitulo() + "' adicionado ao histórico de " + this.getNome());
        } else {
            System.err.println("Erro: Tentativa de adicionar um empréstimo nulo ao histórico.");
        }
    }



    
}
