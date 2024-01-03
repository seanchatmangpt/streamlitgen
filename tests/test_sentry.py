"""Test Sentry configuration."""

import sentry_sdk

from streamlitgen.sentry import configure_sentry


def test_configure_sentry() -> None:
    """Test that Sentry can be configured."""
    configure_sentry()
    assert sentry_sdk.Hub.current.client is not None
