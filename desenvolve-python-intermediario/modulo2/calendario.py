from datetime import datetime, timedelta
from abc import ABC, abstractmethod

class EventoABC(ABC):
    def __init__(self, titulo: str, descricao: str):
        self._titulo = titulo
        self._descricao = descricao
    
    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def isConcluido(self):
        pass

class DataHora:
    FORMAT = '%d/%m/%Y, %H:%M'
    
    def __init__(self):
        self._data_hora = None
    
    @property
    def data_hora(self):
        return self._data_hora.strftime(self.FORMAT) if self._data_hora else None
    
    @data_hora.setter
    def data_hora(self, value: str):
        try:
            self._data_hora = datetime.strptime(value, self.FORMAT)
        except ValueError:
            raise ValueError("Formato de data inválido. Use '%d/%m/%Y, %H:%M'")
    
    def isPassado(self):
        return self._data_hora < datetime.now()
    
    def somaDias(self, num_dias: int):
        data_hora_somada = self._data_hora + timedelta(days=num_dias)
        return data_hora_somada.strftime(self.FORMAT)

class EventoUnico(EventoABC):
    def __init__(self, titulo: str, descricao: str, data_hora: str):
        super().__init__(titulo, descricao)
        self._data_hora = DataHora()
        self._data_hora.data_hora = data_hora
    
    def isConcluido(self):
        return self._data_hora.isPassado()
    
    def __str__(self):
        return f"Evento: {self._titulo}, Data: {self._data_hora.data_hora}, Descrição: {self._descricao}, Concluído: {self.isConcluido()}"
    
    def editar_data_hora(self, nova_data_hora: str):
        self._data_hora.data_hora = nova_data_hora

class EventoRecorrente(EventoABC):
    def __init__(self, titulo: str, descricao: str, data_hora_inicial: str, data_hora_final: str, intervalo_repeticao: int):
        super().__init__(titulo, descricao)
        self._datas_horas = []
        
        data_hora_atual = DataHora()
        data_hora_atual.data_hora = data_hora_inicial
        data_hora_final_dt = datetime.strptime(data_hora_final, DataHora.FORMAT)
        
        while datetime.strptime(data_hora_atual.data_hora, DataHora.FORMAT) <= data_hora_final_dt:
            self._datas_horas.append(data_hora_atual)
            nova_data_hora = data_hora_atual.somaDias(intervalo_repeticao)
            data_hora_atual = DataHora()
            data_hora_atual.data_hora = nova_data_hora
    
    def isConcluido(self, indice: int):
        return self._datas_horas[indice].isPassado()
    
    def __str__(self):
        return "\n".join(
            f"Evento: {self._titulo}, Data: {data.data_hora}, Descrição: {self._descricao}, Concluído: {self.isConcluido(i)}"
            for i, data in enumerate(self._datas_horas)
        )
    
    def editar_data_hora(self, data_hora_antiga: str, data_hora_nova: str):
        for data_hora in self._datas_horas:
            if data_hora.data_hora == data_hora_antiga:
                data_hora.data_hora = data_hora_nova
                return
        raise ValueError("Data antiga não encontrada na lista de eventos recorrentes.")

