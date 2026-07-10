from kubedoctor.core.recommendations import generate_recommendations


def test_running_pod_has_no_recommendations():
    recommendations = generate_recommendations(
        status="Running",
        events=["Started", "Pulled"],
    )

    assert recommendations == []


def test_pending_pod_recommends_image_check():
    recommendations = generate_recommendations(
        status="Pending",
        events=["Failed", "BackOff"],
    )

    assert "Check the container image name and tag." in recommendations


def test_crashloop_recommends_log_inspection():
    recommendations = generate_recommendations(
        status="CrashLoopBackOff",
        events=["BackOff"],
    )

    assert "Inspect container logs for startup failures." in recommendations