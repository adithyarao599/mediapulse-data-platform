from app.warehouse.key_resolver import KeyResolver


def test_key_resolution():

    lookup = {"Spotify": 1}

    result = KeyResolver.resolve_key(lookup, "Spotify")

    assert result == 1
