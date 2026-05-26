# Sistema de Notificações de E-commerce

Trabalho da disciplina Padrões de Projeto de Software.

## Sobre o projeto

O sistema simula notificações de um e-commerce utilizando os padrões de projeto Observer e Strategy.

Quando uma venda é realizada, os observadores cadastrados são notificados automaticamente. Cada observador utiliza uma estratégia de notificação diferente, como Email, SMS ou Log.

## Padrões utilizados

### Observer
Utilizado para notificar automaticamente os observadores quando uma venda é realizada.

- Subject: `SistemaVendas`
- Observers:
  - `NotificadorCliente`
  - `NotificadorAdmin`
  - `NotificadorLog`

### Strategy
Utilizado para definir diferentes formas de notificação.

- `NotificacaoEmail`
- `NotificacaoSMS`
- `NotificacaoLog`

As estratégias podem ser alteradas em tempo de execução.

## Estrutura do projeto

```text
tde-padroes-projeto/
│
├── src/
│   ├── main.py
│   │
│   ├── models/
│   ├── observer/
│   └── strategy/
│
├── docs/
├── logs/
├── README.md
└── .gitignore
```

## Como executar

No terminal:

```bash
python -m src.main
```

## Funcionalidades

- Realizar vendas
- Configurar notificações
- Visualizar histórico de vendas
- Registrar logs automaticamente

## Disciplina

- Padrões de Projeto de Software
- Professor: Marcos Gomes da Silva Rocha
- 5º período
