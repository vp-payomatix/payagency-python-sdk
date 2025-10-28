# Makefile for PayAgency Python SDK

.PHONY: help install install-dev test test-cov lint format type-check clean build upload docs

help:
	@echo "Available commands:"
	@echo "  install         Install package dependencies"
	@echo "  install-dev     Install package and development dependencies"
	@echo "  test            Run basic tests"
	@echo "  test-cov        Run tests with coverage"
	@echo "  test-unit       Run unit tests (mocked)"
	@echo "  test-integration Run integration tests (real API calls)"
	@echo "  test-all        Run both unit and integration tests"
	@echo "  lint            Run linting (flake8)"
	@echo "  format          Format code (black)"
	@echo "  type-check      Run type checking (mypy)"
	@echo "  clean           Clean build artifacts"
	@echo "  build           Build package"
	@echo "  upload          Upload to PyPI (requires credentials)"
	@echo "  docs            Generate documentation"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt -r requirements-dev.txt
	pip install -e .

test:
	pytest

test-cov:
	pytest --cov=payagency_api --cov-report=html --cov-report=term

test-unit:
	python run_tests.py unit

test-integration:
	python run_tests.py integration

test-all:
	python run_tests.py

lint:
	flake8 payagency_api/ tests/ examples.py

format:
	black payagency_api/ tests/ examples.py

type-check:
	mypy payagency_api/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build

upload: build
	python -m twine upload dist/*

docs:
	@echo "Documentation generation not implemented yet"

# Development workflow
dev-setup: install-dev
	@echo "Development environment setup complete"

dev-check: lint type-check test
	@echo "All development checks passed"
