from unittest.mock import patch, MagicMock

from kubedoctor.clients.kubernetes import get_pods


@patch("kubedoctor.clients.kubernetes.client.CoreV1Api")
@patch("kubedoctor.clients.kubernetes.config.load_kube_config")
def test_get_pods_returns_pod(
    mock_config,
    mock_core_api,
):
    pod = MagicMock()

    pod.metadata.name = "nginx"
    pod.metadata.namespace = "default"
    pod.status.phase = "Running"
    pod.status.container_statuses = []
    pod.spec.node_name = "worker-1"

    mock_core_api.return_value.list_pod_for_all_namespaces.return_value.items = [pod]

    pods = get_pods("nginx")

    assert len(pods) == 1
    assert pods[0]["name"] == "nginx"
    assert pods[0]["status"] == "Running"