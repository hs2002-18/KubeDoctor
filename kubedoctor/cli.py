from kubedoctor import __version__
from rich.console import Console
import typer

from kubedoctor.commands.diagnose import diagnose
from kubedoctor.commands.helm import helm as helm_command

app = typer.Typer(
    help="KubeDoctor - Kubernetes Troubleshooting CLI",
    no_args_is_help=True,
)

console = Console()

@app.command("version")
def version() -> None:
    """
    Display the installed KubeDoctor version.
    """
    console.print(f"[bold yellow]KubeDoctor[/bold yellow] v{__version__}")

@app.command("diagnose")
def run_diagnose(application: str) -> None:
    """
    Diagnose a Kubernetes application.
    """
    diagnose(application)

@app.command()
def helm(application: str):
    """
    Display Helm release information.
    """
    helm_command(application)
    
