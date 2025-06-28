# SIG-Finance: Sistema de Controle de Finanças Domésticas

**SIG-Finance** é um sistema desenvolvido em Python com o objetivo de ajudar usuários a controlarem suas finanças pessoais de forma prática e eficiente. Através de uma interface simples e algoritmos estruturados, o sistema permite cadastrar, visualizar e gerenciar receitas e despesas, além de gerar relatórios que auxiliam na organização financeira.

## ✨ Funcionalidades

- **Cadastro de Receitas**: Registro de entradas como salários, investimentos, entre outros.
- **Cadastro de Despesas**: Inclusão de gastos mensais categorizados (ex: alimentação, transporte).
- **Cálculo de Saldo Atual**: Atualização automática do saldo com base nas movimentações.
- **Relatórios Simples**: Visualização das despesas por categoria e período.

## 🛠 Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas**: Nenhuma biblioteca externa — apenas recursos nativos da linguagem.

## ▶️ Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/PHS-01/SIG-Finance.git
   cd SIG-Finance
   ```

2. Execute o programa:
   ```bash
   python main.py
   ```

3. Siga as instruções no terminal para interagir com o sistema.

## 📁 Estrutura de Pastas

```
SIG-Finance/
│
├── main.py    # Código principal do sistema
└── README.md  # Este arquivo
```

## Modelo de Dados

### Receita

| Campo         | Tipo         | Descrição                        |
|---------------|--------------|----------------------------------|
| id            | inteiro      | Identificador único da receita   |
| descricao     | texto        | Descrição da receita             |
| valor         | decimal      | Valor monetário da receita       |
| data          | data         | Data em que a receita ocorreu    |
| categoria_id  | inteiro      | ID da categoria associada        |

### Despesa

| Campo         | Tipo         | Descrição                         |
|---------------|--------------|-----------------------------------|
| id            | inteiro      | Identificador único da despesa    |
| descricao     | texto        | Descrição da despesa              |
| valor         | decimal      | Valor monetário da despesa        |
| data          | data         | Data em que a despesa ocorreu     |
| categoria_id  | inteiro      | ID da categoria associada         |

### Categoria

| Campo         | Tipo         | Descrição                              |
|---------------|--------------|----------------------------------------|
| id            | inteiro      | Identificador único da categoria       |
| nome          | texto        | Nome da categoria (ex: Alimentação)    |

## 📄 Licença

Este projeto **não possui licença definida**. O uso, cópia e modificação do código devem ser autorizados pelo autor.
