# Sistema de Notificações de E-commerce

Trabalho Discente Efetivo (TDE) da disciplina Padrões de Projeto de Software.

## Objetivo

Desenvolvimento de um protótipo de sistema de notificações que utiliza a integração dos padrões Observer e Strategy para garantir escalabilidade e facilitar a manutenção do código.

## Descrição do Sistema

O sistema simula notificações de um e-commerce. Quando uma venda é realizada, diferentes observadores são notificados automaticamente e cada um utiliza sua própria estratégia de comunicação (Email, SMS ou Log em arquivo).

## Padrões de Projeto Implementados

### Observer (Comportamental)

Define uma dependência um-para-muitos entre objetos. Quando o objeto observado (Subject) muda de estado, todos os seus observadores são notificados automaticamente.

**Implementação:**
- Subject: `SistemaVendas`
- Observers: `NotificadorCliente`, `NotificadorAdmin`, `NotificadorLog`
- Evento observado: Venda realizada

### Strategy (Comportamental)

Define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis. Permite que o algoritmo varie independentemente dos clientes que o utilizam.

**Implementação:**
- Interface: `EstrategiaNotificacao`
- Estratégias concretas: `NotificacaoEmail`, `NotificacaoSMS`, `NotificacaoLog`
- Contexto: Cada notificador pode escolher e trocar sua estratégia dinamicamente

### Integração dos Padrões

1. Sistema de vendas registra uma venda e dispara o evento
2. Todos os observadores registrados são notificados (Observer)
3. Cada observador executa sua notificação usando a estratégia configurada (Strategy)
4. As estratégias podem ser trocadas em tempo de execução sem alterar o código dos observadores

## Estrutura do Projeto

```
tde-padroes-projeto/
│
├── src/
│   ├── __init__.py
│   ├── main.py               
│   │
│   ├── models/                
│   │   ├── __init__.py
│   │   ├── cliente.py         
│   │   └── venda.py           
│   │
│   ├── observer/              
│   │   ├── __init__.py
│   │   ├── subject.py         
│   │   ├── observer.py         
│   │   └── notificadores.py   
│   │
│   └── strategy/              
│       ├── __init__.py
│       ├── estrategia_notificacao.py    
│       └── estrategias_concretas.py     
│
├── tests/                      
│   └── __init__.py
│
├── docs/                      
│   └── diagrama_uml.png       
│
├── logs/                       
│   └── notificacoes.log
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa necessária (usa apenas bibliotecas padrão do Python)

## Como Executar

1. Clone ou extraia o projeto

2. Navegue até o diretório do projeto:
```bash
cd tde-padroes-projeto
```

3. Execute o sistema:
```bash
python -m src.main
```

## Funcionalidades

- Realizar vendas de forma interativa
- Configurar estratégias de notificação em tempo de execução
- Visualizar histórico de vendas
- Demonstração automática completa do sistema
- Informações detalhadas sobre os padrões implementados

## Boas Práticas Aplicadas

- Código organizado seguindo princípios SOLID
- Nomenclatura clara e significativa
- Separação de responsabilidades
- Uso de docstrings em todas as classes e métodos
- Type hints para melhor legibilidade
- Encapsulamento adequado com propriedades

## Disciplina

- Disciplina: Padrões de Projeto de Software
- Professor: Marcos Gomes da Silva Rocha
- Período: 5º
