"""ad"""

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def progresso_spinner(texto: str, isArquivo: bool):
    """Mostra um spinner enquanto exibe o texto."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()

    with Progress(SpinnerColumn(), TextColumn("[cyan]{task.description}")) as progress:
        progress.add_task(description="Processando texto...", total=None)
        console.print("[bold green]Conteúdo:[/bold green]\n" + texto)


def progresso_barra(texto: str, isArquivo: bool):
    """Mostra uma barra de progresso enquanto exibe o texto."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()

    with Progress() as progress:
        tarefa = progress.add_task("Carregando...", total=100)
        for _ in range(100):
            progress.update(tarefa, advance=1)

    console.print("[bold blue]Texto carregado:[/bold blue]\n" + texto)
