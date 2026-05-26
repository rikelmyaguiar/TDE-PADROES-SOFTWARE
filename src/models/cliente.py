class Cliente:
    def __init__(self, nome: str, email: str, telefone: str):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self) -> str:
        return f"Cliente: {self.nome} | Email: {self.email} | Tel: {self.telefone}"