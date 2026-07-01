from pathlib import Path

def load_document(file_path):
    return Path(file_path).read_text(encoding="utf-8")

def load_documents(folder_path):
    documents=[]
    folder=Path (folder_path)
    for file in folder.glob("*.txt"):
        text=file.read_text(encoding="utf-8")
        documents.append(
            {
                "name":file.name,
                "text":text
            }
        )
    return documents




