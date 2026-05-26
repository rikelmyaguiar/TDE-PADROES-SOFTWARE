import os
from datetime import datetime

from .estrategia_notificacao import EstrategiaNotificacao


class NotificacaoEmail(EstrategiaNotificacao):

    def enviar(self, destinatario: str, mensagem: str):
        print(f"\n[EMAIL] Para: {destinatario}")
        print(f"Mensagem: {mensagem}\n")
        return True

    def obter_tipo(self) -> str:
        return "Email"


class NotificacaoSMS(EstrategiaNotificacao):

    def enviar(self, destinatario: str, mensagem: str):
        print(f"\n[SMS] Para: {destinatario}")
        print(f"Mensagem: {mensagem}\n")
        return True

    def obter_tipo(self) -> str:
        return "SMS"


class NotificacaoLog(EstrategiaNotificacao):

    def __init__(self, arquivo_log="logs/notificacoes.log"):
        self.arquivo_log = arquivo_log

        diretorio = os.path.dirname(arquivo_log)

        if diretorio and not os.path.exists(diretorio):
            os.makedirs(diretorio)

    def enviar(self, destinatario: str, mensagem: str):
        try:
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            linha = f"[{timestamp}] [{destinatario}] {mensagem}\n"

            with open(self.arquivo_log, "a", encoding="utf-8") as arquivo:
                arquivo.write(linha)

            print(f"\n[LOG] Mensagem registrada\n")
            return True

        except Exception as erro:
            print(f"\nErro ao gravar log: {erro}\n")
            return False

    def obter_tipo(self) -> str:
        return "Log"