from rich.console import Console

from kubedoctor.clients.kubernetes import (
    get_namespaces,
    get_pods,
)

console = Console()


def diagnose(application: str) -> None:
    """
    Diagnose a Kubernetes application.
    """
    console.rule("[bold blue]🩺 KubeDoctor")

    try:
        namespaces = get_namespaces()
        pods = get_pods(application)

        console.print(f"[bold]Application:[/bold] {application}\n")
        console.print("[green]✓ Connected to Kubernetes Cluster[/green]\n")

        console.print("[bold]Namespaces[/bold]")
        for namespace in namespaces:
            console.print(f"• {namespace}")

        console.print()

        if not pods:
            console.print(
                f"[yellow]No pods found for application '{application}'.[/yellow]"
            )
            return

        console.print("[bold green]Pods Found[/bold green]\n")

        for pod in pods:
            console.print(f"✓ {pod['name']}")
            console.print(f"  Namespace : {pod['namespace']}")
            console.print(f"  Status    : {pod['status']}\n")

    except RuntimeError as error:
        console.print(f"[bold red]✗ {error}[/bold red]")