"""ad"""

from rich.console import Console
from rich.layout import Layout

console = Console()

def exibir_vertical(texto: str, isArquivo: bool):
    """
    Exibe um texto dentro de um layout formatado usando rich.
    """
    if isArquivo:
        with open(texto, "r") as f:
            texto = f.read()

    layout = Layout()
    layout.split_column(
        Layout(name="topo"),
        Layout(name="baixo")
    )

    layout["topo"].update("=== PARTE SUPERIOR ===\n" + texto)
    layout["baixo"].update("=== PARTE INFERIOR ===\n" + texto[::-1])  # texto invertido 

    console.print(layout)


def exibir_horizontal(texto: str, isArquivo: bool):
    """
    Exibe um texto dividido em dois painéis verticais usando rich.layout.
    """
    if isArquivo:
        with open(texto, "r") as f:
            texto = f.read()

    layout = Layout()
    layout.split_row(
        Layout(name="esquerda"),
        Layout(name="direita")
    )

    layout["esquerda"].update("ESQUERDA\n" + texto)
    layout["direita"].update("DIREITA\n" + texto[::-1])

    console.print(layout)