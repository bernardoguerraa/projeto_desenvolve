package biblioteca;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class AutorTest {

    @Test
    public void testGetNacionalidade() {
        Autor autor = new Autor("Carlos", "Brasileira");
        assertEquals("Brasileira", autor.getNacionalidade());
    }

    @Test
    public void testSetNacionalidade() {
        Autor autor = new Autor("Carlos", "Brasileira");
        autor.setNacionalidade("Portuguesa");
        assertEquals("Portuguesa", autor.getNacionalidade());
    }

    @Test
    public void testAdicionarObra() {
        Autor autor = new Autor("Carlos", "Brasileira");
        Livro livro = new Livro("Java Básico", autor, "Tecnologia");

        assertTrue(autor.getObrasPublicadas().contains(livro));
    }
}
