from pathlib import Path

def load_document(file_path):
    return Path(file_path).read_text(encoding="utf-8")



