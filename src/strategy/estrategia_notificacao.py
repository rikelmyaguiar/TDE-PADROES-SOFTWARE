from abc import ABC, abstractmethod


class EstrategiaNotificacao(ABC):

    @abstractmethod
    def enviar(self, destinatario: str, mensagem: str):
        pass

    @abstractmethod
    def obter_tipo(self) -> str:
        pass