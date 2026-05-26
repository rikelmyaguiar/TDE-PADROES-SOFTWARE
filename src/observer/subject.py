from abc import ABC
from .observer import Observer


class Subject(ABC):

    def __init__(self):
        self.observadores = []

    def adicionar_observador(self, observador: Observer):
        if observador not in self.observadores:
            self.observadores.append(observador)
            print(f"Observador adicionado: {observador.__class__.__name__}")

    def remover_observador(self, observador: Observer):
        if observador in self.observadores:
            self.observadores.remove(observador)
            print(f"Observador removido: {observador.__class__.__name__}")

    def notificar_observadores(self, dados: dict):
        print(f"\nNotificando {len(self.observadores)} observador(es)...")

        for observador in self.observadores:
            observador.atualizar(dados)