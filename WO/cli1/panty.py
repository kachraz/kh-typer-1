# CLI App 1 with tpper
import typer
from typing import Annotated
from rich import print as rprint
from rich.traceback import install

from src.uti import *

install(show_locals=True)

app = typer.Typer()

# Fake Active DB
active_users = ["Jan", "Joe", "Jill", "Jack", "Jill"]

# For adding more help
USERLIST_TYPE = Annotated[list[str], typer.Argument(help="List of users to add")]
VERBOSE_TYPE = Annotated[bool, typer.Option("--verbose", "-v", help="Verbose output")]


@app.command()
def add_user(users: USERLIST_TYPE, verbose: VERBOSE_TYPE = False):
    """Add Users to the active userdb"""
    label1("Add Command")
    for user in users:
        if verbose:
            rprint(f"Users {user} added")
    rprint("[bold green]🟢: Completed Added Users[/bold green]")


@app.command()
def delete_user(users: USERLIST_TYPE, verbose: VERBOSE_TYPE = False):
    """Delete Users from the active userdb"""
    label1("Delete Command")
    for user in users:
        if user not in active_users:
            rprint(f"User {user} not found")
        else:
            rprint(f"Users {user} deleted")
            rprint("🟢❌: Completed Deleted Users")


@app.command()
def list_users():
    rprint("List users")


if __name__ == "__main__":
    app()
