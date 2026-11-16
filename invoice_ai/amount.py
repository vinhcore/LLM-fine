import re

TOTAL_LINE = re.compile(r"^\s*Tổng thanh toán\s*:\s*(.*?)\s*$", re.IGNORECASE)
AMOUNT = re.compile(r"(?:[0-9]{1,15}|[0-9]{1,3}(?:\.[0-9]{3}){1,4})(?:\s*(?:đ|VND))?", re.IGNORECASE)


def extract_amount(ocr_text: str) -> dict:
    candidates = [
        match.group(1)
        for line in ocr_text.splitlines()
        if (match := TOTAL_LINE.fullmatch(line))
    ]
    source = candidates[0] if len(candidates) == 1 else None
    if source is None or not AMOUNT.fullmatch(source):
        return {"status": "needs_review", "total_amount": None, "source_text": source}

    digits = re.match(r"[0-9.]+", source).group()
    return {
        "status": "ok",
        "total_amount": int(digits.replace(".", "")),
        "source_text": source,
    }
