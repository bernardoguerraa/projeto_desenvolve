package biblioteca;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.Date;

public class UsuarioTest {

    @Test
    public void testGetIdade() {
        Usuario usuario = new Usuario("Ana", 22);
        assertEquals(22, usuario.getIdade());
    }

    @Test
    public void testSetIdade() {
        Usuario usuario = new Usuario("Ana", 22);
        usuario.setIdade(25);
        assertEquals(25, usuario.getIdade());
    }

    @Test
    public void testAdicionarEmprestimo() {
        Usuario usuario = new Usuario("Ana", 22);
        Autor autor = new Autor("Carlos", "Brasileira");
        Livro livro = new Livro("Java Básico", autor, "Tecnologia");
        Emprestimo emprestimo = new Emprestimo(livro, usuario, new Date(), new Date());

        assertEquals(1, usuario.getHistoricoEmprestimos().size());
        assertEquals(emprestimo, usuario.getHistoricoEmprestimos().get(0));
    }
}
