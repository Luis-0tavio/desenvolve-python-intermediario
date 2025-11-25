"""
Jogo de resolução de labirinto.

Movimentação:
- w: cima
- s: baixo
- a: esquerda
- d: direita

Abra as portas para se chegar ao final!!
"""

from .jogador import (
    iniciar_jogador,
    salva_pontuação,
)

from .labirinto import (
    jogo_com_live,
    render_labirinto,
    criar_labirinto,
)

from .utils import (
    limpar_terminal,
    menu,
    imprime_instrucoes,
    imprime_ranking,
)

__all__ = [
    "iniciar_jogador",
    "salva_pontuação",
    "jogo_com_live",
    "render_labirinto",
    "criar_labirinto",
    "limpar_terminal",
    "menu",
    "imprime_instrucoes",
    "imprime_ranking",
]