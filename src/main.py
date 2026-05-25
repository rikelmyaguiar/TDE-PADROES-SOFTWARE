"""
Sistema de Notificações de E-commerce.
Demonstra a integração dos padrões Observer e Strategy.
"""

import os
from src.models import Cliente, Venda
from src.observer import NotificadorCliente, NotificadorAdmin, NotificadorLog
from src.observer.subject import Subject
from src.strategy import NotificacaoEmail, NotificacaoSMS, NotificacaoLog


class SistemaVendas(Subject):
    """Sistema principal de vendas que implementa o padrão Observer."""
    
    def __init__(self):
        """Inicializa o sistema de vendas."""
        super().__init__()
        self._vendas = []
    
    def realizar_venda(self, venda: Venda) -> None:
        """
        Realiza uma venda e notifica todos os observadores.
        
        Args:
            venda: Objeto Venda a ser registrada
        """
        self._vendas.append(venda)
        print(f"\n{'='*60}")
        print(f" VENDA REALIZADA COM SUCESSO!")
        print(f"{'='*60}")
        print(venda)
        print(f"{'='*60}\n")
        
        # Notifica todos os observadores (PADRÃO OBSERVER)
        self.notificar_observadores({'venda': venda})
    
    def listar_vendas(self) -> None:
        """Lista todas as vendas realizadas."""
        if not self._vendas:
            print("\nNenhuma venda realizada ainda.")
        else:
            print(f"\n{'='*60}")
            print(f"HISTÓRICO DE VENDAS ({len(self._vendas)} venda(s))")
            print(f"{'='*60}")
            for venda in self._vendas:
                print(venda)
            print(f"{'='*60}\n")


def limpar_tela():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_menu():
    """Exibe o menu principal."""
    print("\n" + "="*60)
    print(" "*15 + "SISTEMA DE NOTIFICAÇÕES - E-COMMERCE")
    print("="*60)
    print("\n[1] Realizar uma venda")
    print("[2] Configurar notificações")
    print("[3] Ver histórico de vendas")
    print("[4] Demonstração completa")
    print("[5] Sobre os padrões utilizados")
    print("[0] Sair")
    print("\n" + "="*60)


def demonstracao_completa(sistema: SistemaVendas):
    """Executa uma demonstração completa do sistema."""
    limpar_tela()
    print("\n" + "="*60)
    print(" "*15 + "DEMONSTRAÇÃO COMPLETA DO SISTEMA")
    print("="*60)
    
    # Criando clientes
    print("\n[1] Criando clientes...")
    cliente1 = Cliente("João Silva", "joao@email.com", "(98) 99999-1111")
    cliente2 = Cliente("Maria Santos", "maria@email.com", "(98) 99999-2222")
    print(f"✓ {cliente1}")
    print(f"✓ {cliente2}")
    
    # Configurando observadores
    print("\n[2] Configurando observadores (PADRÃO OBSERVER)...")
    notif_cliente = NotificadorCliente()
    notif_admin = NotificadorAdmin()
    notif_log = NotificadorLog()
    
    sistema.adicionar_observador(notif_cliente)
    sistema.adicionar_observador(notif_admin)
    sistema.adicionar_observador(notif_log)
    
    # Configurando estratégias
    print("\n[3] Configurando estratégias (PADRÃO STRATEGY)...")
    notif_cliente.definir_estrategia(NotificacaoEmail())
    notif_admin.definir_estrategia(NotificacaoSMS())
    # NotificadorLog já usa NotificacaoLog por padrão
    
    # Realizando vendas
    print("\n[4] Realizando vendas...")
    input("\nPressione ENTER para realizar a primeira venda...")
    
    venda1 = Venda(cliente1, "Notebook Dell Inspiron 15", 3500.00)
    sistema.realizar_venda(venda1)
    
    input("\nPressione ENTER para realizar a segunda venda...")
    
    venda2 = Venda(cliente2, "Mouse Logitech MX Master 3", 450.00)
    sistema.realizar_venda(venda2)
    
    # Mudando estratégia dinamicamente
    print("\n[5] Demonstrando mudança dinâmica de estratégia...")
    print("Alterando notificação do cliente de Email para SMS...")
    notif_cliente.definir_estrategia(NotificacaoSMS())
    
    input("\nPressione ENTER para realizar venda com nova estratégia...")
    
    venda3 = Venda(cliente1, "Teclado Mecânico Keychron K2", 650.00)
    sistema.realizar_venda(venda3)
    
    print("\n✓ Demonstração completa finalizada!")
    input("\nPressione ENTER para voltar ao menu...")


def sobre_padroes():
    """Exibe informações sobre os padrões utilizados."""
    limpar_tela()
    print("\n" + "="*60)
    print(" "*20 + "PADRÕES UTILIZADOS")
    print("="*60)
    
    print("\n PADRÃO OBSERVER")
    print("-" * 60)
    print("Propósito: Definir uma dependência um-para-muitos entre objetos")
    print("           para que quando um objeto muda de estado, todos os")
    print("           seus dependentes são notificados automaticamente.\n")
    print("Implementação neste sistema:")
    print("  • Subject: SistemaVendas")
    print("  • Observers: NotificadorCliente, NotificadorAdmin, NotificadorLog")
    print("  • Evento: Venda realizada")
    print("  • Notificação: Automática para todos observadores registrados")
    
    print("\n PADRÃO STRATEGY")
    print("-" * 60)
    print("Propósito: Definir uma família de algoritmos, encapsular cada")
    print("           um deles e torná-los intercambiáveis. Strategy permite")
    print("           que o algoritmo varie independentemente dos clientes.\n")
    print("Implementação neste sistema:")
    print("  • Interface: EstrategiaNotificacao")
    print("  • Estratégias: NotificacaoEmail, NotificacaoSMS, NotificacaoLog")
    print("  • Contexto: Cada Notificador escolhe sua estratégia")
    print("  • Vantagem: Trocar estratégia em tempo de execução")
    
    print("\n INTEGRAÇÃO DOS PADRÕES")
    print("-" * 60)
    print("  1. Sistema de Vendas dispara evento (Subject)")
    print("  2. Observadores são notificados (Observer)")
    print("  3. Cada observador usa sua estratégia (Strategy)")
    print("  4. Estratégias podem ser trocadas dinamicamente")
    
    print("\n" + "="*60)
    input("\nPressione ENTER para voltar ao menu...")


def configurar_notificacoes(sistema: SistemaVendas, 
                           notif_cliente: NotificadorCliente,
                           notif_admin: NotificadorAdmin):
    """Permite configurar as estratégias de notificação."""
    limpar_tela()
    print("\n" + "="*60)
    print(" "*18 + "CONFIGURAR NOTIFICAÇÕES")
    print("="*60)
    
    print("\n[1] Configurar notificação do CLIENTE")
    print("[2] Configurar notificação do ADMIN")
    print("[0] Voltar")
    
    opcao = input("\nEscolha uma opção: ").strip()
    
    if opcao == '1':
        print("\nEscolha a estratégia para o cliente:")
        print("[1] Email")
        print("[2] SMS")
        escolha = input("\nOpção: ").strip()
        
        if escolha == '1':
            notif_cliente.definir_estrategia(NotificacaoEmail())
        elif escolha == '2':
            notif_cliente.definir_estrategia(NotificacaoSMS())
        
        input("\nPressione ENTER para continuar...")
    
    elif opcao == '2':
        print("\nEscolha a estratégia para o admin:")
        print("[1] Email")
        print("[2] SMS")
        escolha = input("\nOpção: ").strip()
        
        if escolha == '1':
            notif_admin.definir_estrategia(NotificacaoEmail())
        elif escolha == '2':
            notif_admin.definir_estrategia(NotificacaoSMS())
        
        input("\nPressione ENTER para continuar...")


def realizar_venda_interativa(sistema: SistemaVendas):
    """Permite realizar uma venda de forma interativa."""
    limpar_tela()
    print("\n" + "="*60)
    print(" "*22 + "NOVA VENDA")
    print("="*60)
    
    nome = input("\nNome do cliente: ").strip()
    email = input("Email do cliente: ").strip()
    telefone = input("Telefone do cliente (XX) XXXXX-XXXX: ").strip()
    produto = input("Nome do produto: ").strip()
    
    try:
        valor = float(input("Valor da venda (R$): ").strip())
        
        cliente = Cliente(nome, email, telefone)
        venda = Venda(cliente, produto, valor)
        
        sistema.realizar_venda(venda)
        
        input("\nPressione ENTER para continuar...")
    except ValueError:
        print("\n Valor inválido! Venda cancelada.")
        input("\nPressione ENTER para continuar...")


def main():
    """Função principal do sistema."""
    # Inicializa o sistema
    sistema = SistemaVendas()
    
    # Configura observadores padrão
    notif_cliente = NotificadorCliente(NotificacaoEmail())
    notif_admin = NotificadorAdmin(NotificacaoSMS())
    notif_log = NotificadorLog()
    
    sistema.adicionar_observador(notif_cliente)
    sistema.adicionar_observador(notif_admin)
    sistema.adicionar_observador(notif_log)
    
    # Loop principal
    while True:
        limpar_tela()
        exibir_menu()
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '1':
            realizar_venda_interativa(sistema)
        
        elif opcao == '2':
            configurar_notificacoes(sistema, notif_cliente, notif_admin)
        
        elif opcao == '3':
            limpar_tela()
            sistema.listar_vendas()
            input("\nPressione ENTER para continuar...")
        
        elif opcao == '4':
            demonstracao_completa(sistema)
        
        elif opcao == '5':
            sobre_padroes()
        
        elif opcao == '0':
            print("\n" + "="*60)
            print(" "*15 + "Obrigado por usar o sistema!")
            print("="*60 + "\n")
            break
        
        else:
            print("\n Opção inválida!")
            input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()