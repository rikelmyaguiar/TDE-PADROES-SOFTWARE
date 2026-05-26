import os

from src.models import Cliente, Venda
from src.observer import (
    NotificadorCliente,
    NotificadorAdmin,
    NotificadorLog
)

from src.observer.subject import Subject

from src.strategy import (
    NotificacaoEmail,
    NotificacaoSMS
)


class SistemaVendas(Subject):

    def __init__(self):
        super().__init__()
        self.vendas = []

    def realizar_venda(self, venda: Venda):
        self.vendas.append(venda)

        print("\nVenda realizada com sucesso!")
        print(venda)

        self.notificar_observadores({"venda": venda})

    def listar_vendas(self):
        if not self.vendas:
            print("\nNenhuma venda realizada.")
            return

        print("\nHistórico de vendas:\n")

        for venda in self.vendas:
            print(venda)


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def exibir_menu():
    print("\n=== SISTEMA DE VENDAS ===")
    print("[1] Realizar venda")
    print("[2] Configurar notificações")
    print("[3] Ver vendas")
    print("[0] Sair")


def configurar_notificacoes(
    notif_cliente: NotificadorCliente,
    notif_admin: NotificadorAdmin
):
    print("\n[1] Notificação do cliente")
    print("[2] Notificação do admin")

    opcao = input("\nEscolha: ").strip()

    if opcao == "1":
        print("\n[1] Email")
        print("[2] SMS")

        escolha = input("Escolha: ").strip()

        if escolha == "1":
            notif_cliente.definir_estrategia(NotificacaoEmail())

        elif escolha == "2":
            notif_cliente.definir_estrategia(NotificacaoSMS())

    elif opcao == "2":
        print("\n[1] Email")
        print("[2] SMS")

        escolha = input("Escolha: ").strip()

        if escolha == "1":
            notif_admin.definir_estrategia(NotificacaoEmail())

        elif escolha == "2":
            notif_admin.definir_estrategia(NotificacaoSMS())


def realizar_venda_interativa(sistema: SistemaVendas):
    print("\nNova venda\n")

    nome = input("Cliente: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    produto = input("Produto: ")

    try:
        valor = float(input("Valor: R$ "))

        cliente = Cliente(nome, email, telefone)

        venda = Venda(cliente, produto, valor)

        sistema.realizar_venda(venda)

    except ValueError:
        print("\nValor inválido.")


def main():
    sistema = SistemaVendas()

    notif_cliente = NotificadorCliente(NotificacaoEmail())
    notif_admin = NotificadorAdmin(NotificacaoSMS())
    notif_log = NotificadorLog()

    sistema.adicionar_observador(notif_cliente)
    sistema.adicionar_observador(notif_admin)
    sistema.adicionar_observador(notif_log)

    while True:
        limpar_tela()

        exibir_menu()

        opcao = input("\nOpção: ").strip()

        if opcao == "1":
            realizar_venda_interativa(sistema)
            input("\nPressione ENTER...")

        elif opcao == "2":
            configurar_notificacoes(
                notif_cliente,
                notif_admin
            )

            input("\nPressione ENTER...")

        elif opcao == "3":
            sistema.listar_vendas()
            input("\nPressione ENTER...")

        elif opcao == "0":
            print("\nEncerrando sistema...")
            break

        else:
            print("\nOpção inválida.")
            input("\nPressione ENTER...")


if __name__ == "__main__":
    main()