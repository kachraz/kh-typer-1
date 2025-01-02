# Utility funtions here

from rich import print as rprint
from rich.panel import Panel
from rich.console import Console
from rich.traceback import install

install(show_locals=True)
console = Console()


def label1(label):
    panel = Panel.fit(
        f"""[green_yellow]{label}[/green_yellow]""",
        title="(:",
        subtitle=":)",
        style="Italic",
        border_style="magenta",
    )

    # Print the Panel
    console.print(panel)
