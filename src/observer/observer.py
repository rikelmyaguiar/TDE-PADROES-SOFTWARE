"""
Interface Observer.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    """Interface que define o contrato para observadores."""
    
    @abstractmethod
    def atualizar(self, dados: dict) -> None:
        """
        Método chamado quando há uma notificação do subject.
        
        Args:
            dados: Dicionário contendo informações do evento
        """
        pass