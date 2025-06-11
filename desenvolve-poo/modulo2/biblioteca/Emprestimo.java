package modulo2.biblioteca;
import java.util.Date;

public class Emprestimo {
    private Date dataRetirada;
    private Date dataDevolucao;
    private Livro livro;
    private Usuario usuario;

    public Emprestimo(Livro livro, Usuario usuario, Date dataRetirada, Date dataDevolucao) {
        if (livro == null) {
            throw new IllegalArgumentException("Não é possível realizar um empréstimo sem um livro.");
        }
        if (usuario == null) {
            throw new IllegalArgumentException("Não é possível realizar um empréstimo sem um usuário.");
        }

        if (!livro.isDisponivel()) { 
            throw new IllegalArgumentException("O livro '" + livro.getTitulo() + "' não está disponível para empréstimo.");
        }

        this.livro = livro;
        this.usuario = usuario;
        this.dataRetirada = dataRetirada;
        this.dataDevolucao = dataDevolucao;

    
        this.livro.setDisponivel(false);

        
        this.usuario.adicionarEmprestimo(this);
    }

    
    public Date getDataRetirada(){
        return dataRetirada;
    }

    public Date getdataDevolucao(){ 
        return dataDevolucao;
    }

    public Livro getLivro(){
        return livro;
    }

    public Usuario getUsuario(){
        return usuario;
    }


    public void setDataDevolucao(Date dataDevolucao) {
        this.dataDevolucao = dataDevolucao;
    }

    
    public void finalizarEmprestimo() {
        if (this.livro != null) {
            this.livro.setDisponivel(true); 
        }
    }
}
