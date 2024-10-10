import os
import typer
from PyInstaller import __main__ as pyi

typer = typer.Typer()

CUR_PATH = os.path.dirname(os.path.abspath(__file__))


@typer.command()
def build():
    if not os.path.exists("./main.spec"):
        pyi.run(["-F", '--add-data', 'templates:templates', "main.py"])
    pyi.run(['main.spec'])


@typer.command()
def build_pro():
    if not os.path.exists("./main_pro.spec"):
        pyi.run(["-F", '--add-data', 'templates:templates', "main.py"])
    pyi.run(['main_pro.spec'])


if __name__ == "__main__":
    typer()
