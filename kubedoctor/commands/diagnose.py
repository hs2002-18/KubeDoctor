from rich.console import Console

from kubedoctor.clients.kubernetes import get_pods
console = Console()


def diagnose(application: str) -> None:
    """
    Diagnose a Kubernetes application.
    """
    console.rule("[bold blue]🩺 KubeDoctor")

    try:
        pods = get_pods(application)
        namespace = pods[0]["namespace"] if pods else None

        console.print(f"[bold]Application:[/bold] {application}")
        console.print(f"[bold]Namespace:[/bold] {namespace}\n")
        console.print("[green]✓ Connected to Kubernetes Cluster[/green]\n")

        if not pods:
            console.print(
                f"[yellow]No pods found for application '{application}'.[/yellow]"
            )
            return

        console.print("[bold green]Pods Found[/bold green]\n")

        for pod in pods:
            console.print(f"✓ {pod['name']}")
            console.print(f"  Status    : {pod['status']}\n")

    except RuntimeError as error:
        console.print(f"[bold red]✗ {error}[/bold red]")