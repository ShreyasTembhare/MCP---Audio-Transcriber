# MCP Audio Transcriber

A Dockerized Python tool that implements the Model Context Protocol (MCP) via AssemblyAI's API. Upload or point to an audio file, and receive a structured JSON transcription.

## Features

- **AssemblyMCP**: a concrete MCP implementation that uses AssemblyAI's REST API  
- **Command-line interface** (`app.py`):  
  ```bash
  python app.py <input_audio> <output_json>
  ```
- **Streamlit web UI** (`streamlit_app.py`):
  - Upload local files or paste URLs
  - Click Transcribe
  - Preview transcript and download JSON
- **Docker support** for environment consistency and portability

## Prerequisites

- Python 3.10+
- An AssemblyAI API key
- ffmpeg (for local decoding, if using local files)
- (Optional) Docker Desktop / Engine
- (Optional) Streamlit (`pip install streamlit`)

## 🔧 Installation

1. Clone the repo
   ```bash
   git clone https://github.com/ShreyasTembhare/MCP---Audio-Transcriber.git
   cd MCP---Audio-Transcriber
   ```

2. Create a `.env`
   ```
   ASSEMBLYAI_API_KEY=your_assemblyai_api_key_here
   ```

3. Ensure `.gitignore` contains:
   ```gitignore
   .env
   ```

4. Install Python dependencies
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. Install ffmpeg
   - Ubuntu/Debian: `sudo apt update && sudo apt install ffmpeg -y`
   - Windows: download from https://ffmpeg.org and add its `bin/` to your PATH

## Usage

### 1. CLI Transcription

```bash
python app.py <input_audio> <output_json>
```
- `<input_audio>`: any file or URL supported by AssemblyAI
- `<output_json>`: path for the generated JSON

Example:
```bash
python app.py data/input.ogg data/output.json
cat data/output.json
```

### 2. Streamlit Web UI

```bash
streamlit run streamlit_app.py
```
- Open http://localhost:8501
- Upload or enter an audio URL
- Click Transcribe
- Download the JSON result

### 3. Docker

Build the image:
```bash
docker build -t mcp-transcriber .
```

Run it (mounting your data/ folder):
```bash
docker run --rm \
  -e ASSEMBLYAI_API_KEY="$ASSEMBLYAI_API_KEY" \
  -v "$(pwd)/data:/data" \
  mcp-transcriber:latest \
  /data/input.ogg /data/output.json
```

Then inspect:
```bash
ls data/output.json
cat data/output.json
```

Windows PowerShell:
```powershell
docker run --rm `
  -e ASSEMBLYAI_API_KEY=$env:ASSEMBLYAI_API_KEY `
  -v "${PWD}\data:/data" `
  mcp-transcriber:latest `
  /data/input.ogg /data/output.json
```

## Project Structure

```
MCP-Audio-Transcriber/
├── app.py               # CLI entrypoint (AssemblyMCP only)
├── mcp.py               # ModelContextProtocol + AssemblyMCP
├── streamlit_app.py     # Streamlit interface
├── requirements.txt     # assemblyai, python-dotenv, streamlit, etc.
├── Dockerfile           # builds the container
├── .gitignore           # ignores .env, __pycache__, etc.
├── LICENSE              # MIT license
└── data/                # sample input and output
    ├── input.ogg
    └── output.json
```