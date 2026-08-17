"""Four required tests. Make them pass. Add more for the testing mark."""

import pytest
from unittest.mock import patch

from app import app
import summariser


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_health_responds(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_empty_code_is_rejected(client):
    resp = client.post("/summarize", json={"code": "   "})
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_valid_request_returns_summary(client):
    with patch.object(summariser, "summarise_code", return_value={"summary": "stub"}):
        # TODO (learner): app.py imported summarise_code directly, so patching
        # the module attribute is not enough. Work out why this test fails and
        # fix either the import style or the patch target. This is deliberate.
        resp = client.post("/summarize", json={"code": "def f(): pass"})
        assert resp.status_code == 200
        assert "summary" in resp.get_json()


def test_upstream_failure_returns_502(client):
    def boom(_code):
        raise summariser.SummariserError("upstream summarisation failed")

    with patch("app.summarise_code", side_effect=boom):
        resp = client.post("/summarize", json={"code": "def f(): pass"})
        assert resp.status_code == 502
        assert resp.get_json()["error"] == "upstream summarisation failed"
