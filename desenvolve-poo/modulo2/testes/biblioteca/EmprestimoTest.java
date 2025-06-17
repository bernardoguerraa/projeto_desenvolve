package biblioteca;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.Date;

public class EmprestimoTest {

    @Test
    public void testEmprestimoCriadoComSucesso() {
        Date dataRetirada = new Date();
        Date dataDevolucao = new Date();

        Livro livro = new Livro("Java Basics", new Autor("Alan Turing", "Inglês"), "Tecnologia");
        Usuario usuario = new Usuario("Gabriel", 21);

        Emprestimo emprestimo = new Emprestimo(livro, usuario, dataRetirada, dataDevolucao);

        assertEquals(livro, emprestimo.getLivro());
        assertEquals(usuario, emprestimo.getUsuario());
        assertEquals(dataRetirada, emprestimo.getDataRetirada());
        assertEquals(dataDevolucao, emprestimo.getdataDevolucao());
        assertFalse(livro.isDisponivel());
    }

    @Test
    public void testFinalizarEmprestimo() {
        Date dataRetirada = new Date();
        Date dataDevolucao = new Date();

        Livro livro = new Livro("Java Basics", new Autor("Alan Turing", "Inglês"), "Tecnologia");
        Usuario usuario = new Usuario("Gabriel", 21);
        Emprestimo emprestimo = new Emprestimo(livro, usuario, dataRetirada, dataDevolucao);

        emprestimo.finalizarEmprestimo();
        assertTrue(livro.isDisponivel());
    }

    @Test
    public void testSetDataDevolucao() {
        Livro livro = new Livro("Java Basics", new Autor("Alan Turing", "Inglês"), "Tecnologia");
        Usuario usuario = new Usuario("Gabriel", 21);
        Emprestimo emprestimo = new Emprestimo(livro, usuario, new Date(), new Date());

        Date novaData = new Date(System.currentTimeMillis() + 86400000); // +1 dia
        emprestimo.setDataDevolucao(novaData);
        assertEquals(novaData, emprestimo.getdataDevolucao());
    }
}
