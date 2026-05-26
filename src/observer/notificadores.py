from .observer import Observer
from ..strategy.estrategia_notificacao import EstrategiaNotificacao
from ..strategy.estrategias_concretas import (
    NotificacaoEmail,
    NotificacaoSMS,
    NotificacaoLog
)

from ..models.venda import Venda


class NotificadorCliente(Observer):
    def __init__(self, estrategia: EstrategiaNotificacao = None):
        self.estrategia = estrategia or NotificacaoEmail()

    def definir_estrategia(self, estrategia: EstrategiaNotificacao):
        self.estrategia = estrategia
        print(f"Estratégia do cliente alterada para {estrategia.obter_tipo()}")

    def atualizar(self, dados: dict):
        venda: Venda = dados.get("venda")

        if venda:
            cliente = venda.cliente

            mensagem = (
                f"Olá {cliente.nome}! "
                f"Sua compra de '{venda.produto}' "
                f"foi confirmada. "
                f"Pedido #{venda.id}"
            )

            destinatario = (
                cliente.email
                if isinstance(self.estrategia, NotificacaoEmail)
                else cliente.telefone
            )

            self.estrategia.enviar(destinatario, mensagem)


class NotificadorAdmin(Observer):
    def __init__(self, estrategia: EstrategiaNotificacao = None):
        self.estrategia = estrategia or NotificacaoSMS()

    def definir_estrategia(self, estrategia: EstrategiaNotificacao):
        self.estrategia = estrategia
        print(f"Estratégia do admin alterada para {estrategia.obter_tipo()}")

    def atualizar(self, dados: dict):
        venda: Venda = dados.get("venda")

        if venda:
            mensagem = (
                f"Nova venda! "
                f"Pedido #{venda.id} | "
                f"Cliente: {venda.cliente.nome} | "
                f"Produto: {venda.produto}"
            )

            destinatario = (
                "admin@loja.com"
                if isinstance(self.estrategia, NotificacaoEmail)
                else "(98) 98888-8888"
            )

            self.estrategia.enviar(destinatario, mensagem)


class NotificadorLog(Observer):
    def __init__(self):
        self.estrategia = NotificacaoLog()

    def atualizar(self, dados: dict):
        venda: Venda = dados.get("venda")

        if venda:
            mensagem = (
                f"Venda registrada | "
                f"Pedido #{venda.id} | "
                f"{venda.cliente.nome}"
            )

            self.estrategia.enviar("SISTEMA", mensagem)