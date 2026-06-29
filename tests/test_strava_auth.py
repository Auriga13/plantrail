import json
import importlib
import pytest

ta = importlib.import_module("trail_analyzer")


def test_credentials_prefer_env(monkeypatch, tmp_path):
    monkeypatch.setenv("STRAVA_CLIENT_SECRET", "env_secret")
    monkeypatch.setenv("STRAVA_REFRESH_TOKEN", "env_refresh")
    creds = ta.load_strava_credentials()
    assert creds["client_secret"] == "env_secret"
    assert creds["refresh_token"] == "env_refresh"


def test_credentials_fall_back_to_token_file(monkeypatch, tmp_path):
    monkeypatch.delenv("STRAVA_CLIENT_SECRET", raising=False)
    monkeypatch.delenv("STRAVA_REFRESH_TOKEN", raising=False)
    tok = tmp_path / "tok.json"
    tok.write_text(json.dumps({"client_secret": "file_secret", "refresh_token": "file_refresh"}))
    monkeypatch.setattr(ta, "TOKEN_FILE", tok)
    creds = ta.load_strava_credentials()
    assert creds["client_secret"] == "file_secret"
    assert creds["refresh_token"] == "file_refresh"


def test_no_secret_raises(monkeypatch, tmp_path):
    monkeypatch.delenv("STRAVA_CLIENT_SECRET", raising=False)
    monkeypatch.setattr(ta, "TOKEN_FILE", tmp_path / "missing.json")
    with pytest.raises(RuntimeError):
        ta.load_strava_credentials()


def test_no_secret_literal_in_source():
    # Never hard-code the secret here. Read the real value from the gitignored
    # token file and assert it does not appear in the tracked source.
    import json, pathlib
    src = pathlib.Path(ta.__file__).read_text(encoding="utf-8")
    tok = pathlib.Path(ta.__file__).with_name("strava_token.json")
    if not tok.exists():
        return  # nothing to compare against locally
    secret = json.loads(tok.read_text()).get("client_secret")
    if secret:
        assert secret not in src, "Strava client secret literal found in source"


def test_build_refresh_payload():
    creds = {"client_id": "114720", "client_secret": "s", "refresh_token": "r"}
    p = ta.build_refresh_payload(creds)
    assert p == {"client_id": "114720", "client_secret": "s",
                 "grant_type": "refresh_token", "refresh_token": "r"}


def test_detect_refresh_rotation_changed():
    assert ta.detect_refresh_rotation("old", {"refresh_token": "new"}) == "new"


def test_detect_refresh_rotation_unchanged():
    assert ta.detect_refresh_rotation("same", {"refresh_token": "same"}) is None
    assert ta.detect_refresh_rotation("old", {}) is None


def test_refresh_strava_token_requires_refresh_token():
    import pytest
    with pytest.raises(RuntimeError):
        ta.refresh_strava_token({"client_id": "x", "client_secret": "y", "refresh_token": None})
