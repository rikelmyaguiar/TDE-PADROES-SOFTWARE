"""
Módulo que define a entidade Cliente.
"""

class Cliente:
    """Representa um cliente do e-commerce."""
    
    def __init__(self, nome: str, email: str, telefone: str):
        """
        Inicializa um cliente.
        
        Args:
            nome: Nome completo do cliente
            email: Endereço de email
            telefone: Número de telefone no formato (XX) XXXXX-XXXX
        """
        self._nome = nome
        self._email = email
        self._telefone = telefone
    
    @property
    def nome(self) -> str:
        """Retorna o nome do cliente."""
        return self._nome
    
    @property
    def email(self) -> str:
        """Retorna o email do cliente."""
        return self._email
    
    @property
    def telefone(self) -> str:
        """Retorna o telefone do cliente."""
        return self._telefone
    
    def __str__(self) -> str:
        """Representação em string do cliente."""
        return f"Cliente: {self._nome} | Email: {self._email} | Tel: {self._telefone}"