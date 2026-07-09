from rich.console import Console

from kubedoctor.clients.kubernetes import(
     get_pods,
     get_pod_events,
     )
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
            console.print(f"  Status    : {pod['status']}")
            console.print(f"  Restarts    : {pod['restarts']}")
            console.print(f"  Node    : {pod['node']}\n")
            events = get_pod_events(namespace, pod["name"])
            console.print(" Recent Events")
            if events:
                for event in events:
                    console.print(f"    • {event}")
            else:
                console.print("    No recent events found.")
        console.print()


    except RuntimeError as error:
        console.print(f"[bold red]✗ {error}[/bold red]")