"""ad"""

from rich.console import Console
from rich.text import Text

console = Console()

def estilo_colorido(texto: str, isArquivo: bool):
    """Mostra texto colorido e estilizado."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()

    t = Text(texto, style="bold yellow on blue")
    console.print(t)


def estilo_arco_iris(texto: str, isArquivo: bool):
    """Mostra cada letra com um estilo diferente (efeito arco-íris)."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()

    cores = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    t = Text()

    for i, letra in enumerate(texto):
        t.append(letra, style=cores[i % len(cores)])

    console.print(t)
