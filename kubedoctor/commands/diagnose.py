from rich.console import Console
from kubedoctor.clients.kubernetes import getnamespace as get_namespaces
console = Console()


def diagnose(application: str) -> None:
    """
    Diagnose a Kubernetes application.
    """
    console.rule("[bold blue]🩺 KubeDoctor")
    
    try:
        namespaces = get_namespaces()
        console.print(f"Diagnosing application: [green]{application}[/green]")
        console.print("[green]✓ Connected to Kubernetes Cluster[/green]\n")
        console.print("[bold]Namespaces[/bold]")
        for namespace in get_namespaces():
            console.print(f"• {namespace}")
    except RuntimeError as error:
        console.print(f"[bold red]✗ {error}[/bold red]")