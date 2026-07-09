def generate_recommendations(
    status: str,
    events: list[str],
) -> list[str]:
    """
    Generate troubleshooting recommendations
    based on pod status and events.
    """
    recommendations = []
    if "Failed" in events:
        recommendations.append(
            "Check the container image name and tag."
        )

    if "BackOff" in events:
        recommendations.append(
            "Inspect container logs for startup failures."
        )

    if "ImagePullBackOff" in events:
        recommendations.append(
            "Verify the image exists and registry credentials are correct."
        )
    return recommendations