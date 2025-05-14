# MCP Audio Transcriber

A portable, Dockerized Python tool that implements a **Model Context Protocol (MCP)** for audio transcription using OpenAI's Whisper models—and even ships with a Streamlit-powered web UI so you can upload an audio file and download the transcription as JSON.

## 🚀 Features

- **Modular MCP interface** (`mcp.py`) that defines a standard `ModelContextProtocol`.
- **Whisper-based implementation** (`WhisperMCP`) for high-quality, multi-language transcription.
- **Command-line interface** (`app.py`) for batch or ad-hoc transcription:
  ```bash
  python app.py <input_audio> <output_json> [--model MODEL_NAME]
  ```
- **Docker support** for a consistent runtime:
  ```bash
  docker build -t mcp-transcriber .
  docker run --rm \
    -v /full/path/to/data:/data \
    mcp-transcriber:latest \
    /data/input.wav /data/output.json
  ```
- **Streamlit web app** (`streamlit_app.py`) letting end users:
  - Upload any common audio file (.wav, .mp3, .ogg, .m4a)
  - Choose a Whisper model size
  - Preview the transcription live
  - Download the JSON result with one click

## 📦 Prerequisites

- Python 3.10+
- ffmpeg installed & on your PATH
- (Optional) Docker Engine / Docker Desktop
- (Optional) Streamlit

## 🔧 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/ShreyasTembhare/MCP---Audio-Transcriber.git
   cd MCP---Audio-Transcriber
   ```

2. **Python dependencies & FFmpeg**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   # On Ubuntu/Debian:
   sudo apt update && sudo apt install ffmpeg
   # On Windows:
   #   Download a static build from https://ffmpeg.org and add its bin/ to your PATH
   ```

3. **(Optional) Docker**
   - Install Docker Desktop
   - Enable WSL integration if using WSL2.

4. **(Optional) Streamlit**
   ```bash
   pip install streamlit
   ```

## 🎯 Usage

### 1. CLI Transcription

```bash
python app.py <input_audio> <output_json> [--model tiny|base|small|medium|large]
```
- `<input_audio>`: path to your audio file
- `<output_json>`: path where the JSON result will be saved
- `--model`: choose Whisper model size (default: base)

Example:
```bash
python app.py data/input.ogg data/output.json --model tiny
cat data/output.json
```

### 2. Docker

Build the image:
```bash
docker build -t mcp-transcriber .
```

Run it (mounting your data/ folder):
```bash
docker run --rm \
  -v "/full/path/to/your/project/data:/data" \
  mcp-transcriber:latest \
  /data/input.wav /data/output.json
```

Then inspect:
```bash
ls data/output.json
cat data/output.json
```

### 3. Streamlit Web UI

Launch the app:
```bash
streamlit run streamlit_app.py
```

- Open http://localhost:8501 in your browser
- Upload an audio file
- Select the Whisper model size
- Click Transcribe
- Preview & download the resulting JSON

## 📁 Project Structure

```
MCP-Audio-Transcriber/
├── app.py               # CLI entrypoint
├── mcp.py               # Model Context Protocol + WhisperMCP
├── requirements.txt     # Python dependencies
├── streamlit_app.py     # Streamlit interface
├── Dockerfile           # Container definition
├── .gitignore           # ignore **pycache**, venvs, etc.
├── LICENSE              # MIT license
└── data/                # sample input and output
    ├── input.ogg
    └── output.json
```
