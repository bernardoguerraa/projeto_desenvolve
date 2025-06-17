package modulo2.testes.biblioteca;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class LivroTest {

    @Test
    public void testGetTitulo() {
        Autor autor = new Autor("Jess", "Brasileira");
        Livro livro = new Livro("Java Basico", autor, "tecnologia");

        assertEquals("Java Basico", livro.getTitulo());
    }

    @Test
    public void testIsDisponivel() {
        Autor autor = new Autor("Jess", "Brasileira");
        Livro livro = new Livro("Java Avançado", autor, "tecnologia");
        livro.setDisponivel(false);

        assertFalse(livro.isDisponivel());
    }
}
