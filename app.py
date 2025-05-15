# app.py
import argparse
import json
from mcp import AssemblyMCP, ModelContextProtocol


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe audio using AssemblyAI"
    )
    parser.add_argument(
        "input_audio", help="Path to input audio file"
    )
    parser.add_argument(
        "output_json", help="Path to output JSON file"
    )
    args = parser.parse_args()

    mcp: ModelContextProtocol = AssemblyMCP()
    print("[INFO] Using AssemblyAI engine")
    result = mcp.transcribe(args.input_audio)

    with open(args.output_json, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"[INFO] Wrote output to {args.output_json}")


if __name__ == "__main__":
    main()