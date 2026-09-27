from dataclasses import dataclass
from pathlib import Path
import hashlib

SUPPORTED_EXTENSIONS = {".csv", ".xlsx", ".json"}

@dataclass(frozen=True)
class FileMetadata:
    file_name: str
    file_path: str
    extension: str
    size_bytes: int
    sha256: str

def calculate_sha256(file_path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with file_path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()

def inventory_files(input_dir: str = "data/input") -> list[FileMetadata]:
    root = Path(input_dir)
    if not root.exists():
        raise FileNotFoundError(f"Input directory does not exist: {root}")

    results = []
    for path in sorted(root.iterdir()):
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            results.append(FileMetadata(
                file_name=path.name,
                file_path=str(path),
                extension=path.suffix.lower(),
                size_bytes=path.stat().st_size,
                sha256=calculate_sha256(path),
            ))
    return results

if __name__ == "__main__":
    for item in inventory_files():
        print(f"{item.file_name} | {item.extension} | {item.size_bytes} bytes | {item.sha256}")
