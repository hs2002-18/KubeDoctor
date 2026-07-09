import typer

from kubedoctor.commands.diagnose import diagnose
from kubedoctor.commands.helm import helm as helm_command

app = typer.Typer(
    help="KubeDoctor - Kubernetes Troubleshooting CLI",
    no_args_is_help=True,
)


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
    
