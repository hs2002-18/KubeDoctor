import json
import subprocess


def get_release(application: str) -> dict | None:
    """
    Retrieve Helm release information.
    """
    try:
        result = subprocess.run(
            [
                "helm",
                "list",
                "--output",
                "json",
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        releases = json.loads(result.stdout)

        for release in releases:
            if application.lower() == release["name"].lower():
                return {
                    "name": release["name"],
                    "namespace": release["namespace"],
                    "status": release["status"],
                    "chart": release["chart"],
                    "revision": release["revision"],
                }

        return None

    except subprocess.CalledProcessError as error:
        raise RuntimeError(
            # "Failed to retrieve Helm releases."
            error.stderr.strip() or error.stdout.strip()
        )

    except FileNotFoundError:
        raise RuntimeError(
            "Helm is not installed."
        )