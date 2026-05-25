"""
Implementações concretas de Observadores que utilizam Strategy.
"""

from .observer import Observer
from ..strategy.estrategia_notificacao import EstrategiaNotificacao
from ..strategy.estrategias_concretas import NotificacaoEmail, NotificacaoSMS, NotificacaoLog
from ..models.venda import Venda


class NotificadorCliente(Observer):
    """Observador responsável por notificar o cliente."""
    
    def __init__(self, estrategia: EstrategiaNotificacao = None):
        """
        Inicializa o notificador do cliente.
        
        Args:
            estrategia: Estratégia de notificação (padrão: Email)
        """
        self._estrategia = estrategia if estrategia else NotificacaoEmail()
    
    def definir_estrategia(self, estrategia: EstrategiaNotificacao) -> None:
        """
        Define/altera a estratégia de notificação.
        
        Args:
            estrategia: Nova estratégia a ser utilizada
        """
        self._estrategia = estrategia
        print(f"✓ Estratégia do NotificadorCliente alterada para: {estrategia.obter_tipo()}")
    
    def atualizar(self, dados: dict) -> None:
        """
        Notifica o cliente sobre a venda.
        
        Args:
            dados: Dicionário contendo a venda realizada
        """
        venda: Venda = dados.get('venda')
        
        if venda:
            cliente = venda.cliente
            mensagem = (f"Olá {cliente.nome}! Sua compra de '{venda.produto}' "
                       f"no valor de R$ {venda.valor:.2f} foi confirmada. "
                       f"Pedido #{venda.id}")
            
            destinatario = cliente.email if isinstance(self._estrategia, NotificacaoEmail) else cliente.telefone
            self._estrategia.enviar(destinatario, mensagem)


class NotificadorAdmin(Observer):
    """Observador responsável por notificar o administrador."""
    
    def __init__(self, estrategia: EstrategiaNotificacao = None):
        """
        Inicializa o notificador do administrador.
        
        Args:
            estrategia: Estratégia de notificação (padrão: SMS)
        """
        self._estrategia = estrategia if estrategia else NotificacaoSMS()
    
    def definir_estrategia(self, estrategia: EstrategiaNotificacao) -> None:
        """
        Define/altera a estratégia de notificação.
        
        Args:
            estrategia: Nova estratégia a ser utilizada
        """
        self._estrategia = estrategia
        print(f"✓ Estratégia do NotificadorAdmin alterada para: {estrategia.obter_tipo()}")
    
    def atualizar(self, dados: dict) -> None:
        """
        Notifica o administrador sobre a venda.
        
        Args:
            dados: Dicionário contendo a venda realizada
        """
        venda: Venda = dados.get('venda')
        
        if venda:
            mensagem = (f"Nova venda! Pedido #{venda.id} - "
                       f"Cliente: {venda.cliente.nome} - "
                       f"Produto: {venda.produto} - "
                       f"Valor: R$ {venda.valor:.2f}")
            
            destinatario = "admin@loja.com" if isinstance(self._estrategia, NotificacaoEmail) else "(98) 98888-8888"
            self._estrategia.enviar(destinatario, mensagem)


class NotificadorLog(Observer):
    """Observador responsável por registrar vendas em log."""
    
    def __init__(self):
        """Inicializa o notificador de log (sempre usa estratégia Log)."""
        self._estrategia = NotificacaoLog()
    
    def atualizar(self, dados: dict) -> None:
        """
        Registra a venda em arquivo de log.
        
        Args:
            dados: Dicionário contendo a venda realizada
        """
        venda: Venda = dados.get('venda')
        
        if venda:
            mensagem = (f"VENDA REGISTRADA - Pedido #{venda.id} | "
                       f"Cliente: {venda.cliente.nome} | "
                       f"Produto: {venda.produto} | "
                       f"Valor: R$ {venda.valor:.2f}")
            
            destinatario = "SISTEMA"
            self._estrategia.enviar(destinatario, mensagem)