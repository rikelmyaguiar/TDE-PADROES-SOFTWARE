from datetime import datetime
from .cliente import Cliente


class Venda:
    contador_id = 1

    def __init__(self, cliente: Cliente, produto: str, valor: float):
        self.id = Venda.contador_id
        Venda.contador_id += 1

        self.cliente = cliente
        self.produto = produto
        self.valor = valor
        self.data_hora = datetime.now()

    def __str__(self) -> str:
        data_formatada = self.data_hora.strftime("%d/%m/%Y %H:%M:%S")

        return (
            f"Venda #{self.id} | "
            f"{self.cliente.nome} | "
            f"{self.produto} | "
            f"R$ {self.valor:.2f} | "
            f"{data_formatada}"
        )