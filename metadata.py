from dataclasses import dataclass

@dataclass
class ChunkMetadata:

    chunk_id: int

    document_name: str

    text: str