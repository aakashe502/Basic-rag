# basic_rag

A small retrieval-augmented generation (RAG) project that loads a local document, chunks it, retrieves the most relevant passages for a user question, and then asks the LLM to answer using only that retrieved context.

## What it does

- loads text from `documents/company.txt`
- splits the document into smaller chunks via `chunker.py`
- performs a simple relevance search in `retriever.py`
- builds a prompt and sends the retrieved context to the LLM in `llm.py`
- runs the full flow from a question to an answer in `rag.py`

## Source of truth

The main source of truth is `rag.py` — it orchestrates the full RAG pipeline.

Other important files:

- `llm.py` — LLM request logic and prompt formatting
- `loader.py` — loads the base document text
- `chunker.py` — divides the document into chunks
- `retriever.py` — finds the best chunk matches for the question

## Virtual environment

This folder reuses the `githubcodeforces/.venv` virtual environment.

To activate it on macOS / Linux:

```bash
source ../githubcodeforces/.venv/bin/activate
```

On Windows PowerShell:

```powershell
..\githubcodeforces\.venv\Scripts\Activate.ps1
```

Once activated, run the main script with:

```bash
python rag.py
```
