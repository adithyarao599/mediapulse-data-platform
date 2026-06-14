from app.ml.drift_detector import DriftDetector


def test_drift():

    result = DriftDetector.detect(100, 200, threshold=50)

    assert result is True
