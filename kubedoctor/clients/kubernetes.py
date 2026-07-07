from kubernetes import client, config
from kubernetes.client.exceptions import ApiException
from kubernetes.config.config_exception import ConfigException


def get_namespaces() -> list[str]:
    """
    Retrieve all namespaces from the Kubernetes cluster.
    """
    try:
        config.load_kube_config()

        v1 = client.CoreV1Api()
        namespaces = v1.list_namespace()

        return [
            namespace.metadata.name
            for namespace in namespaces.items
        ]

    except ConfigException:
        raise RuntimeError(
            "Unable to load Kubernetes configuration."
        )

    except ApiException as error:
        raise RuntimeError(
            f"Failed to connect to the Kubernetes API: {error.reason}"
        )


def get_pods(application: str) -> list[dict]:
    """
    Retrieve pods matching the application name.
    """
    try:
        config.load_kube_config()

        v1 = client.CoreV1Api()
        pods = v1.list_pod_for_all_namespaces()

        matching_pods = []

        for pod in pods.items:
            if application.lower() in pod.metadata.name.lower():
                matching_pods.append(
                    {
                        "name": pod.metadata.name,
                        "namespace": pod.metadata.namespace,
                        "status": pod.status.phase,
                    }
                )

        return matching_pods

    except ConfigException:
        raise RuntimeError(
            "Unable to load Kubernetes configuration."
        )

    except ApiException as error:
        raise RuntimeError(
            f"Failed to connect to the Kubernetes API: {error.reason}"
        )