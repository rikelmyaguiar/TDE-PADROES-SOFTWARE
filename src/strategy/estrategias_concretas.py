"""
Implementações concretas das estratégias de notificação.
"""

import os
from datetime import datetime
from .estrategia_notificacao import EstrategiaNotificacao


class NotificacaoEmail(EstrategiaNotificacao):
    """Estratégia de notificação por Email."""
    
    def enviar(self, destinatario: str, mensagem: str) -> bool:
        """
        Simula o envio de um email.
        
        Args:
            destinatario: Email do destinatário
            mensagem: Conteúdo do email
            
        Returns:
            True (sempre bem-sucedido na simulação)
        """
        print(f"\n [EMAIL] Enviando para: {destinatario}")
        print(f"   Assunto: Confirmação de Venda")
        print(f"   Mensagem: {mensagem}")
        print(f"   ✓ Email enviado com sucesso!\n")
        return True
    
    def obter_tipo(self) -> str:
        """Retorna o tipo da estratégia."""
        return "Email"


class NotificacaoSMS(EstrategiaNotificacao):
    """Estratégia de notificação por SMS."""
    
    def enviar(self, destinatario: str, mensagem: str) -> bool:
        """
        Simula o envio de um SMS.
        
        Args:
            destinatario: Telefone do destinatário
            mensagem: Conteúdo do SMS
            
        Returns:
            True (sempre bem-sucedido na simulação)
        """
        print(f"\n[SMS] Enviando para: {destinatario}")
        print(f"   Mensagem: {mensagem}")
        print(f"   ✓ SMS enviado com sucesso!\n")
        return True
    
    def obter_tipo(self) -> str:
        """Retorna o tipo da estratégia."""
        return "SMS"


class NotificacaoLog(EstrategiaNotificacao):
    """Estratégia de notificação por gravação em arquivo de log."""
    
    def __init__(self, arquivo_log: str = "logs/notificacoes.log"):
        """
        Inicializa a estratégia de log.
        
        Args:
            arquivo_log: Caminho do arquivo de log
        """
        self._arquivo_log = arquivo_log
        
        # Cria o diretório se não existir
        diretorio = os.path.dirname(arquivo_log)
        if diretorio and not os.path.exists(diretorio):
            os.makedirs(diretorio)
    
    def enviar(self, destinatario: str, mensagem: str) -> bool:
        """
        Grava a notificação em arquivo de log.
        
        Args:
            destinatario: Identificação do destinatário
            mensagem: Conteúdo a ser logado
            
        Returns:
            True se gravado com sucesso, False caso contrário
        """
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            linha_log = f"[{timestamp}] [{destinatario}] {mensagem}\n"
            
            with open(self._arquivo_log, 'a', encoding='utf-8') as arquivo:
                arquivo.write(linha_log)
            
            print(f"\n [LOG] Gravado em: {self._arquivo_log}")
            print(f"   Destinatário: {destinatario}")
            print(f"   Mensagem: {mensagem}")
            print(f"   ✓ Log gravado com sucesso!\n")
            return True
            
        except Exception as e:
            print(f"\n [LOG] Erro ao gravar log: {e}\n")
            return False
    
    def obter_tipo(self) -> str:
        """Retorna o tipo da estratégia."""
        return "Log"