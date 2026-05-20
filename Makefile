run:
	uv run python3 -B -m src

install:
	uv sync

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

fclean: clean
	rm -rf .venv

.PHONY: run clean fclean install