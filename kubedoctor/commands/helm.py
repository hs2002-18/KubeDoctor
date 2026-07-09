from rich.console import Console

from kubedoctor.clients.helm_client import get_release

console = Console()


def helm(application: str) -> None:
    """
    Display Helm release information.
    """
    console.rule("[bold blue]⎈ Helm Information")

    try:
        release = get_release(application)

        if not release:
            console.print(
                f"[yellow]No Helm release found for '{application}'.[/yellow]"
            )
            return

        console.print(f"[bold]Application:[/bold] {application}\n")

        console.print(f"Release Name : {release['name']}")
        console.print(f"Namespace    : {release['namespace']}")
        console.print(f"Chart        : {release['chart']}")
        console.print(f"Revision     : {release['revision']}")
        console.print(f"Status       : {release['status']}")

    except RuntimeError as error:
        console.print(f"[bold red]✗ {error}[/bold red]")