import importlib

cr = importlib.import_module("ci_refresh")


def test_prepare_token_file_fills_missing_keys():
    creds = {"client_secret": "sec", "refresh_token": "r_old"}
    tok = {"access_token": "a", "expires_at": 123}  # Strava sometimes omits these on refresh
    out = cr.prepare_token_file(tok, creds, "r_old")
    assert out["access_token"] == "a"
    assert out["client_secret"] == "sec"
    assert out["refresh_token"] == "r_old"


def test_prepare_token_file_keeps_rotated_refresh():
    creds = {"client_secret": "sec", "refresh_token": "r_old"}
    tok = {"access_token": "a", "refresh_token": "r_new", "expires_at": 123}
    out = cr.prepare_token_file(tok, creds, "r_old")
    assert out["refresh_token"] == "r_new"   # Strava's new value wins
