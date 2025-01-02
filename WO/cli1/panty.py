# CLI App 1 with tpper
import typer
from typing import Annotated
from rich import print as rprint
from rich.traceback import install

from src.uti import *

install(show_locals=True)

app = typer.Typer()
USERLIST_TYPE = Annotated[list[str], typer.Argument(description="List of users to add")]


@app.command()
def add_user(users: list[str], verbose: bool = False):
    """Add Users to the active userdb"""
    label1("Add Command")
    for user in users:
        if verbose:
            rprint(f"Users {user} added")
    rprint("🟢: Completed Added Users")


@app.command()
def delete_user():
    rprint("Delete user")


@app.command()
def list_users():
    rprint("List users")


if __name__ == "__main__":
    app()
