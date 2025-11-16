"""
Pacote personalizado que utiliza funcionalidades da biblioteca Rich para
formatar, estilizar e exibir textos no terminal.

Módulos incluídos:
- layout: recursos de rich.layout
- painel: recursos de rich.panel
- progresso: barras de progresso de rich.progress
- estilo: estilização de texto com rich.text
"""

from .layout import (
    exibir_vertical,
    exibir_horizontal,
)

from .painel import (
    painel_simples,
    painel_com_estilo,
)

from .progresso import (
    progresso_spinner,
    progresso_barra,
)

from .estilo import (
    estilo_colorido,
    estilo_arco_iris,
)
__all__ = [
    # layout
    "exibir_vertical",
    "exibir_horizontal",

    # painel
    "painel_simples",
    "painel_com_estilo",

    # progresso
    "progresso_spinner",
    "progresso_barra",

    # estilo
    "estilo_colorido",
    "estilo_arco_iris",
]