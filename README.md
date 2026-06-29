# Basic RAG

This folder contains a simple retrieval-augmented generation (RAG) project that answers questions using a local document as context.

## What it does

- Loads a document from the `documents/` folder
- Splits the text into smaller chunks
- Retrieves the most relevant chunks for a question using vector embeddings now ,as normal chunk retrieval failed when we modified the question keeping the context same.
- Sends the retrieved context to the LLM for an answer

## Main files

- `rag.py` — the main entry point that runs the full workflow
- `loader.py` — loads the document content
- `chunker.py` — splits the text into chunks
- `retriever.py` — finds relevant chunks for the question
- `llm.py` — sends the prompt to the LLM

## Environment

This project reuses the virtual environment from the `githubcodeforces` project.

### macOS / Linux

```bash
source ../githubcodeforces/.venv/bin/activate
```

### Windows PowerShell

```powershell
..\githubcodeforces\.venv\Scripts\Activate.ps1
```

### Run the project

```bash
python rag.py
```

You can then enter your question and the app will answer based on the document context.
