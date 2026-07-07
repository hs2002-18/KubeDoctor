from kubernetes import client, config

def getnamespace() -> list[str]:
    """
    Retrieve all namespaces from the Kubernetes cluster.
    """
    try:
        config.load_kube_config()
        v1 = client.CoreV1Api()
        namespaces = v1.list_namespace()
        return [namespace.metadata.name for namespace in namespaces.items]
    except ConfigException:
        raise RuntimeError("Unable to load Kubernetes configuration.")
    except ApiException as error:
        raise RuntimeError(
            f"Failed to connect to the Kubernetes API: {error.reason}"
        )