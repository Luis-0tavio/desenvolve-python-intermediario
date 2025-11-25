"""
Utilitarios gerais e de menu
"""
import os
from rich import print

def limpar_terminal():
    """
    Limpa o terminal
    """
    os.system("cls")
    
def menu():
    """
    Apresenta o menu
    """
    print("\n1 - [bold green]Start[/bold green]\n2 - [bold yellow]Como jogar[/bold yellow]\n3 - [bold yellow]Pontuações[/bold yellow]\n4 - [bold red]Quit - Salvar pontuação[bold red]\n")
    
def imprime_instrucoes():
    """
    Apresenta as intruções
    """
    print("\n[bold blue]======Como jogar======[/bold blue]")
    print("As bordas e paredes do labirinto são demarcadas por \"#\";")
    print("As chaves são demarcadas por \"$\";")
    print("vAs portas são demarcadas por \"|\" e podem ser abertas por chaves;")
    print("O jogador é apresentado por \"@\" e pode se movimentar ou verticalmente ou horizontalmente;")
    print("vO fim do jogo é demarcado com \"+\", chegar neste ponto encerra o jogo;")
    print("Basicamente, é isso. Aproveite! :)\n")
    
def imprime_ranking():
    """
    Imprime as pontuações
    """
    with open("aventura_pkg/ranking.csv","r") as rnk:
        for linha in rnk:
            score=linha.split(",")
            print("NOME: ",score[0]," PASSOS: ",score[1])
    