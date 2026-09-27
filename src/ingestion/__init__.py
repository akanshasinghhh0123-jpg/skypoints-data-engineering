"""Ingestion package entry point."""


def main() -> int:
	"""Run the file inventory workflow using its configured settings."""
	from .file_inventory import main as file_inventory_main

	result = file_inventory_main()
	return result if isinstance(result, int) else 0


if __name__ == "__main__":
	raise SystemExit(main())
