"""Streamlit app."""

from importlib.metadata import version

import streamlit as st

st.title(f"streamlitgen v{version('streamlitgen')}")  # type: ignore[no-untyped-call]
