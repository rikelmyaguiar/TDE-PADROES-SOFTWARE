"""
Interface Strategy para estratégias de notificação.
"""

from abc import ABC, abstractmethod


class EstrategiaNotificacao(ABC):
    """Interface que define o contrato para estratégias de notificação."""
    
    @abstractmethod
    def enviar(self, destinatario: str, mensagem: str) -> bool:
        """
        Envia uma notificação.
        
        Args:
            destinatario: Destinatário da notificação (email, telefone, etc)
            mensagem: Conteúdo da mensagem
            
        Returns:
            True se enviado com sucesso, False caso contrário
        """
        pass
    
    @abstractmethod
    def obter_tipo(self) -> str:
        """
        Retorna o tipo/nome da estratégia.
        
        Returns:
            Nome da estratégia (ex: "Email", "SMS", "Log")
        """
        pass