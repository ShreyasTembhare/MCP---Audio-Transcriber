import argparse
import json
from mcp import WhisperMCP

def main():
    parser = argparse.ArgumentParser(
        description="Transcribe audio via MCP and emit JSON."
    )
    parser.add_argument("input_audio", help="Path to input audio file")
    parser.add_argument("output_json", help="Path to output JSON file")
    parser.add_argument("--model", default="base", help="Whisper model size")
    args = parser.parse_args()


    print(f"[DEBUG] Running transcription: {args.input_audio} → {args.output_json}, model={args.model}")

    mcp = WhisperMCP(model_name=args.model)
    result = mcp.transcribe(args.input_audio)
    print(f"[DEBUG] Transcription returned keys: {list(result.keys())}")


    with open(args.output_json, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
