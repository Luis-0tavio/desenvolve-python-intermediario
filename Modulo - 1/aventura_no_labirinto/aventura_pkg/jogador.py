"""
Funções de movimentação do jogador
"""

def mover(tecla, px, py, keys, matriz,cont):
    """
    Move o personagem 
    """
    
    
    # Deltas de movimento
    dx, dy = 0, 0
    if tecla == "w": dx = -1
    elif tecla == "s": dx = 1
    elif tecla == "a": dy = -1
    elif tecla == "d": dy = 1
    else:
        return px, py, keys,matriz,cont  # tecla inválida

    # Próxima posição
    nx, ny = px + dx, py + dy

    # Impede sair da matriz
    if nx < 0 or ny < 0 or nx >= len(matriz) or ny >= len(matriz[0]):
        return px, py, keys,matriz,cont

    alvo = matriz[nx][ny]

    # PAREDE
    if alvo == 1:
        return px, py, keys,matriz,cont

    # PORTA (4)
    if alvo == 4:
        if keys == 0:
            return px, py, keys,matriz,cont  # sem chave → não entra
        else:
            keys -= 1  # gasta chave

    # CHAVE (3)
    if alvo == 3:
        keys += 1

    # Movimento
    matriz[px][py] = 0
    px, py = nx, ny
    matriz[px][py] = 2
    cont+=1

    return px, py, keys, matriz,cont

    
def iniciar_jogador(x,y,matriz):
    """
    Inicia o jogador na posição x,y
    """
    matriz[x][y]=2
    return x,y,matriz

def salva_pontuação(nome,cont):
    with open("aventura_pkg/ranking.csv","a") as rnk:
        rnk.write(f"{nome},{cont}\n")