import typer

from kubedoctor.commands.diagnose import diagnose

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
    
@app.command("logs")
def logs() -> None:
    """View application logs."""
    raise typer.Exit()

@app.command("health")
def health() -> None:
    """Check application health."""
    raise typer.Exit()