from datetime import datetime

class Evento:
    total_eventos = 0  # atributo de classe para contar eventos

    def __init__(self, titulo: str, data_hora: datetime, descricao: str):
        self.titulo = titulo
        self.data_hora = data_hora
        self.descricao = descricao
        self.is_concluido = False  # inicializa como não concluído
        
        Evento.total_eventos += 1  # incrementa o total de eventos

    def isConcluido(self):
        if self.data_hora < datetime.now():
            self.is_concluido = True
        return self.is_concluido

    @classmethod
    def num_eventos(cls):
        return cls.total_eventos

    @staticmethod
    def valida_evento(nome, data_hora, descricao):
        return isinstance(nome, str) and isinstance(data_hora, datetime) and isinstance(descricao, str)
    
    def __str__(self):
        return f"Evento: {self.titulo}, Data: {self.data_hora}, Descrição: {self.descricao}, Concluído: {self.is_concluido}"
    
    def __eq__(self, other):
        return self.data_hora == other.data_hora
    
    def __ne__(self, other):
        return self.data_hora != other.data_hora
    
    def __lt__(self, other):
        return self.data_hora < other.data_hora
    
    def __le__(self, other):
        return self.data_hora <= other.data_hora
    
    def __gt__(self, other):
        return self.data_hora > other.data_hora
    
    def __ge__(self, other):
        return self.data_hora >= other.data_hora

# criando duas instâncias de Evento para testar
evento1 = Evento("Reunião de Equipe", datetime(2025, 2, 15, 10, 30), "Revisão do projeto em andamento.")
evento2 = Evento("Aniversário do João", datetime(2025, 3, 5, 19, 0), "Festa surpresa para o João.")

# Imprimindo eventos
print(evento1)
print(evento2)

# Testando comparações
print(f"evento1 == evento2: {evento1 == evento2}")
print(f"evento1 != evento2: {evento1 != evento2}")
print(f"evento1 < evento2: {evento1 < evento2}")
print(f"evento1 <= evento2: {evento1 <= evento2}")
print(f"evento1 > evento2: {evento1 > evento2}")
print(f"evento1 >= evento2: {evento1 >= evento2}")
