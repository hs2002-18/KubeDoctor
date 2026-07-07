from rich.console import Console

console = Console()


def diagnose(application: str) -> None:
    """
    Diagnose a Kubernetes application.
    """
    console.rule("[bold blue]🩺 KubeDoctor")
    console.print(f"Diagnosing application: [green]{application}[/green]")