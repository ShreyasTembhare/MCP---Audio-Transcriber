import streamlit as st
import json
import os
import tempfile
from mcp import WhisperMCP

st.set_page_config(page_title="MCP Audio Transcriber", layout="centered")
st.title("🎙️ MCP Audio Transcriber")

# Sidebar for model selection
model_size = st.sidebar.selectbox(
    "Choose Whisper model size:",
    ("tiny", "base", "small", "medium", "large"),
    index=1
)

# File uploader
uploaded_file = st.file_uploader(
    "Upload an audio file (wav, mp3, ogg, m4a):", type=["wav", "mp3", "ogg", "m4a"]
)

if uploaded_file is not None:
    st.audio(uploaded_file, format=uploaded_file.type)
    if st.button("Transcribe"):
        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        # Transcribe
        mcp = WhisperMCP(model_name=model_size)
        with st.spinner("Transcribing..."):
            result = mcp.transcribe(tmp_path)

        # Show result JSON
        st.subheader("Transcription Result")
        st.json(result)

        # Prepare download
        json_str = json.dumps(result, ensure_ascii=False, indent=2)
        st.download_button(
            label="Download JSON",
            data=json_str,
            file_name="transcription.json",
            mime="application/json"
        )

        # Clean up temp file
        try:
            os.remove(tmp_path)
        except Exception:
            pass
