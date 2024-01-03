"""Test streamlitgen."""

import streamlitgen


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(streamlitgen.__name__, str)
