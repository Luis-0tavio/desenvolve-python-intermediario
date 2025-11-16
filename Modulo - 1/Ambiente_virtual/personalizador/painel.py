"""ad"""

from rich.console import Console
from rich.panel import Panel

console = Console()

def painel_simples(texto: str, isArquivo: bool):
    """Exibe um painel simples com o texto."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()

    panel = Panel(texto, title="Painel Simples", border_style="green")
    console.print(panel)


def painel_com_estilo(texto: str, isArquivo: bool):
    """Exibe um painel com estilo customizado."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()

    panel = Panel(
        texto,
        title="[bold yellow]Painel Estilizado[/bold yellow]",
        subtitle="Texto formatado com rich",
        border_style="magenta",
        padding=(1, 4)
    )
    console.print(panel)
