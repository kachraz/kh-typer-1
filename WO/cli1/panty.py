# CLI App 1 with tpper
import typer
from typing import Annotated
from functools import wraps
from rich import print as rprint
from rich.progress import track
from rich.table import Table
from time import sleep

from rich.traceback import install

from src.uti import *

install(show_locals=True)

app = typer.Typer()

# Fake Account for authentication
admin = {
    "username": "admin",
    "password": "admin",
}

# Fake Active DB
active_users = ["Jan", "Joe", "Jill", "Jack", "Jill"]

# For adding more help
USERLIST_TYPE = Annotated[list[str], typer.Argument(help="List of users to add")]
VERBOSE_TYPE = Annotated[bool, typer.Option("--verbose", "-v", help="Verbose output")]
USERNAME_TYPE = Annotated[str, typer.Option(help="Username ?", envvar="USERNAME")]
PASSWORD_TYPE = Annotated[
    str,
    typer.Option(help="Password ? ", prompt=True, hide_input=True, envvar="PASSWORD"),
]


# Deccorator function for validation
def req_cred(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs["username"] != admin["username"]:
            rprint("[bold red]🔴: Invalid Username[/bold red]")
            exit(1)
        if kwargs["password"] != admin["password"]:
            rprint("[bold red]🔴: Invalid Password[/bold red]")
            exit(1)
        return func(*args, **kwargs)

    return wrapper


@app.command()
@req_cred
def add_user(
    users: USERLIST_TYPE,
    verbose: VERBOSE_TYPE = False,
    username: USERNAME_TYPE = "admin",
    password: PASSWORD_TYPE = None,
):
    """Add Users to the active userdb"""
    label1("Add Command")
    for user in users:
        if verbose:
            rprint(f"Users {user} added")
    rprint("[bold green]🟢: Completed Added Users[/bold green]")


@app.command()
@req_cred
def delete_user(
    users: USERLIST_TYPE,
    verbose: VERBOSE_TYPE = False,
    username: USERNAME_TYPE = "admin",
    password: PASSWORD_TYPE = None,
):
    """Delete Users from the active userdb"""
    label1("Delete Command")
    for user in users:
        if user not in active_users:
            rprint(f"User {user} not found")
        else:
            rprint(f"Users {user} deleted")
            rprint("🟢❌: Completed Deleted Users")


@app.command()
def list_users(verbose: VERBOSE_TYPE = False):
    table = Table(title="Active Users")
    table.add_column("UserName", justify="center", style="cyan")
    table.add_column("Password", justify="center", style="cyan")

    for user in track(active_users, description="Loading Users.."):
        sleep(1)
        table.add_row(user)
        if verbose:
            rprint(f"Users: {user}")
    rprint("DoneLoading")
    console.print(table)


if __name__ == "__main__":
    app()
