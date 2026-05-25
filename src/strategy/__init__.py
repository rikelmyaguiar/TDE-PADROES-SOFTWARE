"""
Módulo do padrão Strategy para notificações.
"""

from .estrategia_notificacao import EstrategiaNotificacao
from .estrategias_concretas import (
    NotificacaoEmail,
    NotificacaoSMS,
    NotificacaoLog
)

__all__ = [
    'EstrategiaNotificacao',
    'NotificacaoEmail',
    'NotificacaoSMS',
    'NotificacaoLog'
]