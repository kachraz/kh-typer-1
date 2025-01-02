# CLI App 1 with tpper
import typer
from rich import print as rprint
from rich.traceback import install

install(show_locals=True)

app = typer.Typer()


@app.command()
def add_user(users: list[str]):
    rprint("Add user")


@app.command()
def delete_user():
    rprint("Delete user")


@app.command()
def list_users():
    rprint("List users")


if __name__ == "__main__":
    app()
