import curses

menu = [
    "|" + ("=" * 61) + "|",
    "| 💰 SIG-Finance - Sistema de Controle de Finanças Domésticas |",
    "|" + ("=" * 61) + "|",
    "|" + (" " * 61) + "|",
    "|" + (" " * 17) + "Escolha uma das opções abaixo:" + (" " * 14) + "|",
    "|" + (" " * 61) + "|",
    "|" + (" " * 20) + "[1] ➕ Adicionar receita" + (" " * 17) + "|",
    "|" + (" " * 20) + "[2] ➖ Adicionar despesa" + (" " * 17) + "|",
    "|" + (" " * 20) + "[3] 📊 Exibir relatório" + (" " * 18) + "|",
    "|" + (" " * 20) + "[4] 💼 Ver saldo atual" + (" " * 19) + "|",
    "|" + (" " * 20) + "[0] 🚪 Sair do sistema" + (" " * 19) + "|",
    "|" + (" " * 61) + "|",
    "|" + ("=" * 61) + "|"
]



def main(stdscr):

    # Isso habilitar o cursor (0 = desligar)
    curses.curs_set(1)

    while True:

        # Limpa a tela
        stdscr.clear()

        # Inicializa o sistema de cores
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)  # Par de cores: texto vermelho no fundo preto

        y = 0
        x = 50

        # Exibe algo no terminal
        # stdscr.addstr(y, x, "texto")
        for texto in menu:
            stdscr.addstr(y, 50, texto)
            y += 1

        # Atualiza a tela
        stdscr.refresh()

        resp = stdscr.getch()  # Captura a tecla pressionada

        
        if resp == ord('1'):
            stdscr.addstr(y+2, x, "[Receita] A função para adicionar receita ainda será implementada.")
        elif resp == ord('2'):
            stdscr.addstr(y+2, x, "[Despesa] A função para adicionar despesa ainda será implementada.")
        elif resp == ord('3'):
            stdscr.addstr(y+2, x, "[Relatório] A função para exibir o relatório ainda será implementada.")
        elif resp == ord('4'):
            stdscr.addstr(y+2, x, "[Saldo] A função para exibir o saldo ainda será implementada.")
        elif resp == ord('0'):
            stdscr.addstr(y+2, x, (" " * 16) + "Saindo do sistema... Até logo!" + (" " * 16))
            stdscr.refresh()
            stdscr.getch()  # Aguarda o pressionamento de uma tecla antes de fechar
            break
        else:
            stdscr.addstr(y+2, x, (" " * 13) + " ❌ Opção inválida. Tente novamente. " + (" " * 13), curses.color_pair(1))


        stdscr.addstr(y+4, x, (" " * 15) + "Pressione Enter para continuar..." + (" " * 15))
        stdscr.getch()

        # Atualiza a tela
        stdscr.refresh()
        
        
        

# Executa a função principal no modo curses
curses.wrapper(main)
