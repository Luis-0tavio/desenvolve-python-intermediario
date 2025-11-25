"""
Funções do mapa
"""
import csv

from aventura_pkg import jogador as jog

from rich.live import Live
from rich.table import Table

import msvcrt
from time import sleep

def render_labirinto(matriz, keys, nome, cor):
    """
    Gera um objeto Table do rich representando a matriz, para o terminal não dar "flicking"
    """
    tab = Table.grid(padding=0)
    # cada linha é uma única "célula" do table (para manter espaçamento)
    for linha in matriz:
        linha_texto = ""
        for cel in linha:
            if cel == 1:
                linha_texto += "###"      # Parede
            elif cel == 0:
                linha_texto += "   "                         # Caminho
            elif cel == 2:
                # jogador com cor selecionada 
                cor_text = cor if cor in ("yellow","blue", "green", "red") else "white"
                linha_texto += f"[bold {cor_text}] @ [/]"
            elif cel == 3:
                linha_texto += "[yellow] $ [/]"              # Chave
            elif cel == 4:
                linha_texto += "[red] | [/]"                 # Porta
            else:
                linha_texto += " + "                         # Final
        tab.add_row(linha_texto)

    # info abaixo do mapa
    tab.add_row("")  # linha em branco
    info = f"[green]Jogador:[/] {nome}    [yellow]Keys:[/] {keys}    [cyan]Q:[/] voltar ao menu"
    tab.add_row(info)
    return tab

def jogo_com_live(matriz, px, py, keys, nome, cor,cont):
    """
    Loop do jogo usando rich.Live. Retorna (px, py, keys, matriz) quando o jogador sai (pressiona 'q').
    """
    # cria Live controlando a tela inteira sem flicker
    with Live(screen=True, auto_refresh=False) as live:
        while True:
            live.update(render_labirinto(matriz, keys, nome, cor))
            live.refresh()

            # leitura não-bloqueante de tecla com msvcrt
            if msvcrt.kbhit():
                raw = msvcrt.getch()
                # algumas teclas especiais retornam zero ou \xe0 seguido de outro byte
                if not raw:
                    continue
                try:
                    tecla = raw.decode("utf-8").lower()
                except:
                    # tecla não mapeável em utf-8 -> ignorar
                    continue

                if tecla == 'q':
                    # voltar ao menu
                    break

                if tecla in ('w', 'a', 's', 'd'):
                    # usa sua função mover (mantendo lógica de chaves/portas)
                    px, py, keys, matriz,cont = jog.mover(tecla, px, py, keys, matriz,cont)

            # pequena pausa para evitar uso 100% CPU (o refresh já controla fluidez)
            sleep(0.01)

    return px, py, keys, matriz,cont


def criar_labirinto(arq_mapa):
    """
    Lê o arquivo do labirinto
    """
    matriz = []
    with open(arq_mapa, "r") as f:
        leitor = csv.reader(f)
        for linha in leitor:
            linha_convertida = [int(x) for x in linha]
            
            matriz.append(linha_convertida)
            
    return matriz


     