import personalizador.layout as l
from personalizador.painel import painel_simples
from personalizador.progresso import progresso_spinner
from personalizador.estilo import estilo_colorido

import argparse


parser = argparse.ArgumentParser(description="Ferramenta de CLI para formatação de texto ou arquivos.")


parser.add_argument('entrada', type=str, help='Texto ou nome do arquivo que deseja imprimir formatado.')

parser.add_argument('-a', '--arquivo', action='store_true', help='Ativada quando o argumento "entrada" é o caminho para um arquivo.')

parser.add_argument('-m', '--modulo', type=str, help='Escolhe o módulo que a pessoa quer acessar (por nome ou por id). Opções disponíveis: [estilo,layout,painel,progresso]')

parser.add_argument('-f', '--funcao', type=str, help='Escolhe a função do módulo que quer acessar (por nome ou por id). Opções disponíveis: [estilo: estilo_colorido, estilo_arco_iris; layout: exibir_vertical, exibir_horizontal; painel: painel_simples, painel_com_estilo; progresso: progresso_spinner, progresso_barra]')

args=parser.parse_args()

print(args)
