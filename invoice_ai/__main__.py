import argparse
import json
from pathlib import Path

from invoice_ai.amount import extract_amount


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ocr_file", type=Path)
    args = parser.parse_args()
    result = extract_amount(args.ocr_file.read_text(encoding="utf-8"))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
