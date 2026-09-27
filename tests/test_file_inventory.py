from pathlib import Path
from src.ingestion.file_inventory import calculate_sha256, inventory_files

def test_calculate_sha256(tmp_path: Path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("hello")
    assert calculate_sha256(file_path) == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"

def test_inventory_files_only_returns_supported_files(tmp_path: Path):
    (tmp_path / "members.xlsx").write_bytes(b"excel")
    (tmp_path / "redemptions.json").write_text("{}")
    (tmp_path / "notes.txt").write_text("ignore")
    results = inventory_files(str(tmp_path))
    assert [x.file_name for x in results] == ["members.xlsx", "redemptions.json"]
