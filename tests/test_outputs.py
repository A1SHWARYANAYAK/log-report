import json
from pathlib import Path


def load_report():
    """Load the generated report from the expected output path."""
    report = Path("/app/report.json")
    assert report.exists(), "report.json was not created"
    return json.loads(report.read_text())


def test_total_requests():
    """Success Criterion 1: report contains the correct total request count."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success Criterion 2: report contains the correct number of unique client IP addresses."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Success Criterion 3: report contains the most frequently requested path."""
    report = load_report()
    assert report["top_path"] == "/index.html"


def test_schema():
    """Success Criterion 4: report is valid JSON containing exactly the required fields."""
    report = load_report()

    expected_keys = {
        "total_requests",
        "unique_ips",
        "top_path",
    }

    assert set(report.keys()) == expected_keys
    assert isinstance(report["total_requests"], int)
    assert isinstance(report["unique_ips"], int)
    assert isinstance(report["top_path"], str)