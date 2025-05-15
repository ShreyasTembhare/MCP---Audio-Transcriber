import os
import tempfile
import json
import streamlit as st
from mcp import AssemblyMCP
from dotenv import load_dotenv

load_dotenv()    

st.set_page_config(page_title="MCP Audio Transcriber", layout="centered")
st.title("🎙️ MCP Audio Transcriber")

# Load API key
if not os.getenv("ASSEMBLYAI_API_KEY"):
    st.error("Please set ASSEMBLYAI_API_KEY in your .env file before running the app.")

uploaded_file = st.file_uploader(
    "Upload an audio file (wav, mp3, ogg, m4a):", type=["wav", "mp3", "ogg", "m4a"]
)

if uploaded_file is not None:
    st.audio(uploaded_file, format=uploaded_file.type)
    if st.button("Transcribe"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        try:
            mcp = AssemblyMCP()
        except Exception as e:
            st.error(str(e))
            st.stop()

        with st.spinner("Transcribing..."):
            result = mcp.transcribe(tmp_path)

        st.subheader("Transcription Result")
        st.json(result)

        json_str = json.dumps(result, ensure_ascii=False, indent=2)
        st.download_button(
            label="Download JSON",
            data=json_str,
            file_name="transcription.json",
            mime="application/json"
        )

        try:
            os.remove(tmp_path)
        except OSError:
            pass