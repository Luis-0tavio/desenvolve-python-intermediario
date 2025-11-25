import os
import argparse
from playsound import playsound
from time import sleep

from rich import print

from aventura_pkg import labirinto as lab
from aventura_pkg import utils as utl
from aventura_pkg import jogador as jog

def main():
    parser = argparse.ArgumentParser(description="Jogo LABIRINTO.")
    parser.add_argument('nome', type=str, help='Nome do jogador.')
    parser.add_argument('-c', '--color', type=str, help='Escolhe a cor do personagem: yellow , blue, green, red.', default="green")
    parser.add_argument('-d', '--dificuldade', type=str, help='Escolhe a dificuldade do jogo: facil, medio, deificil', default="medio")
    parser.add_argument('-s', '--disable', action='store_false', help='Desabilita a música')
    parser.add_argument('-r', '--rmsave', action='store_false', help='Desabilita o salvamento da pontuação')
    
    args = parser.parse_args()
    nome = args.nome
    cor = args.color
    dif=args.dificuldade
    musica=args.disable
    
    if musica:
        playsound('aventura_pkg\play.mp3',False)

    arq_mapa = os.path.join("aventura_pkg", f"{dif}.csv")
    matriz = lab.criar_labirinto(arq_mapa)

    # iniciar jogador 
    px, py, matriz = jog.iniciar_jogador(1, 1, matriz)  # posição padrão (1,1)
    keys = 0
    cont = 0

    while True:
        utl.limpar_terminal()
        utl.menu()
        opcao = input("Digite a opção desejada: ").lower()

        match opcao:
            case '1':
               
                px, py, keys, matriz,cont = lab.jogo_com_live(matriz, px, py, keys, nome, cor,cont)
                # ao voltar para o menu, limpar terminal para evitar restos na tela
                utl.limpar_terminal()

            case '2':
                utl.limpar_terminal()
                utl.imprime_instrucoes()
                input("\nPressione ENTER para voltar ao menu...")
            
            case '3':
                utl.limpar_terminal()
                utl.imprime_ranking()
                input("\nPressione ENTER para voltar ao menu...")

            case '4':
                print("[red]Encerrando...[/]")
                if args.rmsave:
                    if cont != 0:
                        jog.salva_pontuação(nome,cont)
                break

            case _:
                print("Opção inválida. Tente novamente.")
                sleep(0.8)

if __name__ == "__main__":
    main()
