from kubernetes import client, config
from kubernetes.client.exceptions import ApiException
from kubernetes.config.config_exception import ConfigException

# diagnose.py is not using get_namespaces(), will remove it if it is not needed, later.
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
                        "restarts": sum(
                            container.restart_count
                            for container in (pod.status.container_statuses or [])
                        ),
                        "node": pod.spec.node_name,
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

def get_pod_events(namespace: str, pod_name: str) -> list[str]:
    """
    Retrieve events for a specific pod.
    """
    try:
        config.load_kube_config()
        v1=client.CoreV1Api()
        events=v1.list_namespaced_event(namespace)
        pod_events = []

        for event in events.items:
            if event.involved_object.name==pod_name:
                pod_events.append(event.reason)
        return pod_events
    except ConfigException:
        raise RuntimeError(
            "Unable to load Kubernetes configuration."
            )
    except ApiException as error:
        raise RuntimeError(
            f"Failed to connect to the Kubernetes API: {error.reason}"
        )