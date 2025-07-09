import os
import pickle
from Controller.menu_generator import write_menu, create_menu

from Model.income import income_menu
from Model.expense import expense_menu
from Model.report import report_menu
from Model.category import category_menu

categories = {
    1 : {"name": "Alimentação"},
    2 : {"name": "Transporte"},
    3 : {"name": "Salário"},
    4 : {"name": "Investimento"}
}
try:
  arq_categories = open("Database/categories.dat", "rb")
  categories += pickle.load(arq_categories)
except:
  arq_categories = open("Database/categories.dat", "wb")
arq_categories.close()

transactions = {
    1: {"type": "income",  "description": "Salário Mensal",        "value": 3000.00, "date": "2025-07-01", "category_id": 3},
    2: {"type": "income",  "description": "Dividendos de Ações",   "value": 250.75,  "date": "2025-07-10", "category_id": 4},
    3: {"type": "expense", "description": "Supermercado",          "value": 320.50,  "date": "2025-07-05", "category_id": 1},
    4: {"type": "expense", "description": "Passe de Ônibus",       "value": 80.00,   "date": "2025-06-02", "category_id": 2},
    5: {"type": "expense", "description": "Jantar Fora",           "value": 120.00,  "date": "2025-06-15", "category_id": 1},
    6: {"type": "income",  "description": "Freelance Design",      "value": 900.00,  "date": "2025-06-20", "category_id": 3},
    7: {"type": "expense", "description": "Combustível",           "value": 150.00,  "date": "2025-06-18", "category_id": 2},
    8: {"type": "income",  "description": "Rendimento Poupança",   "value": 45.30,   "date": "2025-05-25", "category_id": 4},
    9: {"type": "expense", "description": "Almoço com Amigos",     "value": 85.00,   "date": "2025-05-28", "category_id": 1},
   10: {"type": "expense", "description": "Uber",                  "value": 60.00,   "date": "2025-05-30", "category_id": 2}
}
try:
  arq_transactions = open("Database/transactions.dat", "rb")
  transactions += pickle.load(arq_transactions)
except:
  arq_transactions = open("Database/transactions.dat", "wb")
arq_transactions.close()

menu = {
    'header' : "💰 SIG-Finance - Sistema de Controle de Finanças Domésticas",
    'options_menu' : [
        "[1] 📥 Menu de Receitas       ",
        "[2] 📤 Menu de Despesas       ",
        "[3] 📁 Gerenciar Categorias   ",
        "[4] 📈 Relatórios             ",
        "[5] 💼 Ver saldo atual        ",
        "[0] 🚪 Sair do sistema        "
    ]
}


def main():
    while True:
        # Limpa o terminal
        os.system('clear')

        # Menu inicial em texto
        write_menu(create_menu(menu["header"], menu["options_menu"], size = 70, section_separator = "=", border = "|", recoil = 1))

        # Variável para guardar a resposta do usuário
        resp = input("\nDigite o número da opção desejada: ")
        
        # Limpa o terminal
        os.system('clear')

        match resp:
            case "1":
                print("\n➡️ Submenu de Receitas ainda será implementado.")
                income_menu(transactions)
            case "2":
                print("\n➡️ Submenu de Despesas ainda será implementado.")
                expense_menu(transactions)
            case "3":
                category_menu(categories)
            case "4":
                print("\n📊 Relatórios ainda serão implementados.")
                report_menu(transactions, categories)
            case "5":
                print("\n[Saldo] A função para exibir o saldo ainda será implementada.")
            case "0":
                print("\n👋 Saindo do sistema... Até logo!")
                break
            case _:
                print("\n❌ Opção inválida. Tente novamente.")
                
        input("\nPressione Enter para continuar...")

main()

### Gravando os dados no arquivo

arq_categories = open("Database/categories.dat", "wb")
pickle.dump(categories, arq_categories)
arq_categories.close()

arq_transactions = open("Database/transactions.dat", "wb")
pickle.dump(transactions, arq_transactions)
arq_transactions.close()