import streamlit as st
import sys
import os

st.title("Dependency Debugger")

st.header("Python Info")
st.write(f"Python Version: {sys.version}")
st.write(f"Executable: {sys.executable}")
st.write(f"CWD: {os.getcwd()}")

st.header("Package Tests")

# Test 1: Wikipedia
try:
    import wikipedia
    st.success(f"✅ Wikipedia imported successfully! Version: {getattr(wikipedia, '__version__', 'unknown')}")
except ImportError as e:
    st.error(f"❌ Wikipedia Failed: {e}")

# Test 2: DuckDuckGo Search (ddgs)
try:
    import duckduckgo_search
    st.success(f"✅ duckduckgo-search imported! Version: {getattr(duckduckgo_search, '__version__', 'unknown')}")
except ImportError as e:
    st.error(f"❌ duckduckgo-search Failed: {e}")

try:
    import ddgs
    st.success(f"✅ ddgs module imported successfully!")
except ImportError as e:
    st.error(f"❌ ddgs module import Failed: {e}")

st.header("Installed Packages (pip freeze)")
try:
    import subprocess
    result = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True)
    st.code(result.stdout)
except Exception as e:
    st.error(f"Failed to run pip freeze: {e}")
