"""
Subject (Observable) do padrão Observer.
"""

from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    """Interface do Observer."""
    
    @abstractmethod
    def atualizar(self, dados: dict) -> None:
        """
        Método chamado quando o subject notifica mudanças.
        
        Args:
            dados: Dicionário com dados do evento
        """
        pass


class Subject(ABC):
    """Classe abstrata Subject (Observable)."""
    
    def __init__(self):
        """Inicializa o subject com lista vazia de observadores."""
        self._observadores: List[Observer] = []
    
    def adicionar_observador(self, observador: Observer) -> None:
        """
        Adiciona um observador à lista.
        
        Args:
            observador: Observer a ser adicionado
        """
        if observador not in self._observadores:
            self._observadores.append(observador)
            print(f"✓ Observador adicionado: {observador.__class__.__name__}")
    
    def remover_observador(self, observador: Observer) -> None:
        """
        Remove um observador da lista.
        
        Args:
            observador: Observer a ser removido
        """
        if observador in self._observadores:
            self._observadores.remove(observador)
            print(f"✓ Observador removido: {observador.__class__.__name__}")
    
    def notificar_observadores(self, dados: dict) -> None:
        """
        Notifica todos os observadores registrados.
        
        Args:
            dados: Dicionário com dados do evento
        """
        print(f"\n Notificando {len(self._observadores)} observador(es)...")
        for observador in self._observadores:
            observador.atualizar(dados)