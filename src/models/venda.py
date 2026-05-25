"""
Módulo que define a entidade Venda.
"""

from datetime import datetime
from .cliente import Cliente


class Venda:
    """Representa uma venda realizada no e-commerce."""
    
    _contador_id = 1  # Contador estático para IDs únicos
    
    def __init__(self, cliente: Cliente, produto: str, valor: float):
        """
        Inicializa uma venda.
        
        Args:
            cliente: Objeto Cliente que realizou a compra
            produto: Nome/descrição do produto
            valor: Valor total da venda
        """
        self._id = Venda._contador_id
        Venda._contador_id += 1
        
        self._cliente = cliente
        self._produto = produto
        self._valor = valor
        self._data_hora = datetime.now()
    
    @property
    def id(self) -> int:
        """Retorna o ID único da venda."""
        return self._id
    
    @property
    def cliente(self) -> Cliente:
        """Retorna o cliente da venda."""
        return self._cliente
    
    @property
    def produto(self) -> str:
        """Retorna o produto vendido."""
        return self._produto
    
    @property
    def valor(self) -> float:
        """Retorna o valor da venda."""
        return self._valor
    
    @property
    def data_hora(self) -> datetime:
        """Retorna a data e hora da venda."""
        return self._data_hora
    
    def __str__(self) -> str:
        """Representação em string da venda."""
        data_formatada = self._data_hora.strftime("%d/%m/%Y %H:%M:%S")
        return (f"Venda #{self._id} | {self._cliente.nome} | "
                f"{self._produto} | R$ {self._valor:.2f} | {data_formatada}")