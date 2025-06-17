package modulo2.testes.biblioteca;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class PessoaTest {

    @Test
    public void testGetNome() {
        Pessoa pessoa = new Pessoa("Maria");
        assertEquals("Maria", pessoa.getNome());
    }

    @Test
    public void testSetNome() {
        Pessoa pessoa = new Pessoa("João");
        pessoa.setNome("Carlos");
        assertEquals("Carlos", pessoa.getNome());
    }
}
