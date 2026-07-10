from unittest.mock import patch, MagicMock

from kubedoctor.clients.helm_client import get_release


@patch("subprocess.run")
def test_get_helm_release(mock_run):
    process = MagicMock()

    process.returncode = 0
    process.stdout = """
    [
        {
            "name": "nginx",
            "namespace": "default",
            "revision": "1",
            "status": "deployed",
            "chart": "nginx-18.3.6"
        }
    ]
    """

    mock_run.return_value = process

    release = get_release("nginx")

    assert release is not None