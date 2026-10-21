from pathlib import Path

def test_reusable_workflow_exists():
    wf = Path(".github/workflows/ci-governance.yml")
    assert wf.exists()
    content = wf.read_text()
    assert "workflow_call" in content
    assert "trivy-severity" in content