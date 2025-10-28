# PayAgency Python SDK - Deployment Guide

This document provides instructions for deploying and publishing the PayAgency Python SDK.

## Pre-requisites

- Python 3.7 or higher
- pip and setuptools
- twine (for PyPI publishing)
- Git

## Installation & Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vp-payomatix/payagency-python.git
cd payagency-python
```

### 2. Set up Development Environment

```bash
# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt

# Install package in editable mode
pip install -e .
```

### 3. Using Make Commands

The project includes a Makefile for common tasks:

```bash
# Set up development environment
make dev-setup

# Run tests
make test

# Run tests with coverage
make test-cov

# Format code
make format

# Lint code
make lint

# Type check
make type-check

# Run all checks
make dev-check

# Build package
make build

# Clean build artifacts
make clean
```

## Testing

### Run Unit Tests

```bash
# Basic test run
pytest

# With coverage
pytest --cov=payagency_api --cov-report=html --cov-report=term

# Or use make
make test-cov
```

### Manual Testing

```python
from payagency_api import PayAgencyApi

# Initialize client
client = PayAgencyApi(
    encryption_key="your-32-character-encryption-key",
    secret_key="PA_TEST_your-secret-key"
)

# Test basic functionality
wallets = client.payout.get_wallets()
print(wallets)
```

## Code Quality

### Formatting

```bash
# Format with black
black payagency_api/ tests/ examples.py

# Or use make
make format
```

### Linting

```bash
# Lint with flake8
flake8 payagency_api/ tests/ examples.py

# Or use make
make lint
```

### Type Checking

```bash
# Type check with mypy
mypy payagency_api/

# Or use make
make type-check
```

## Building the Package

### Build Distribution Files

```bash
# Clean previous builds
make clean

# Build wheel and source distribution
python -m build

# Or use make
make build
```

This creates:

- `dist/payagency_api-1.0.0-py3-none-any.whl`
- `dist/payagency-api-1.0.0.tar.gz`

### Verify Build

```bash
# Check distribution
python -m twine check dist/*

# Test install from wheel
pip install dist/payagency_api-1.0.0-py3-none-any.whl
```

## Publishing

### Test PyPI (Recommended First)

```bash
# Upload to Test PyPI
python -m twine upload --repository testpypi dist/*

# Test install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ payagency-api
```

### Production PyPI

```bash
# Upload to PyPI
python -m twine upload dist/*

# Or use make
make upload
```

### Environment Variables

Set up your PyPI credentials:

```bash
# ~/.pypirc
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-your-api-token

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-your-test-api-token
```

## Release Process

### 1. Update Version

Update version in:

- `setup.py`
- `pyproject.toml`
- `payagency_api/__init__.py`

### 2. Update Changelog

Add release notes to `CHANGELOG.md` (create if needed).

### 3. Commit and Tag

```bash
git add .
git commit -m "Release v1.0.0"
git tag v1.0.0
git push origin main --tags
```

### 4. Build and Publish

```bash
make clean
make dev-check  # Run all quality checks
make build
make upload
```

### 5. Create GitHub Release

1. Go to GitHub repository
2. Click "Releases" → "Create a new release"
3. Select the tag (v1.0.0)
4. Add release notes
5. Attach distribution files from `dist/`

## Installation for Users

Once published, users can install the package:

```bash
# From PyPI
pip install payagency-api

# Specific version
pip install payagency-api==1.0.0

# With development dependencies
pip install payagency-api[dev]
```

## Continuous Integration

### GitHub Actions Example

Create `.github/workflows/ci.yml`:

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.7, 3.8, 3.9, "3.10", "3.11"]

    steps:
      - uses: actions/checkout@v3
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v3
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt -r requirements-dev.txt
          pip install -e .

      - name: Run tests
        run: |
          pytest --cov=payagency_api --cov-report=xml

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
```

## Security Considerations

1. **API Keys**: Never commit real API keys to version control
2. **Environment Variables**: Use environment variables for sensitive data
3. **HTTPS**: Always use HTTPS endpoints in production
4. **Dependencies**: Regularly update dependencies for security patches
5. **Code Scanning**: Enable GitHub security scanning

## Documentation

### API Documentation

Generate documentation with Sphinx (optional):

```bash
pip install sphinx sphinx-rtd-theme
sphinx-quickstart docs
# Configure and build documentation
```

### Examples

Maintain comprehensive examples in:

- `examples.py` - Basic usage examples
- `docs/examples/` - Advanced examples
- `README.md` - Quick start guide

## Support and Maintenance

### Issue Tracking

- Use GitHub Issues for bug reports and feature requests
- Label issues appropriately (bug, enhancement, documentation, etc.)
- Provide issue templates for consistent reporting

### Version Management

Follow semantic versioning (SemVer):

- MAJOR: Incompatible API changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes (backward compatible)

### Deprecation Policy

- Announce deprecations in advance
- Maintain backward compatibility for at least one major version
- Provide clear migration guides

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed
2. **SSL Warnings**: Update urllib3 or use virtual environment
3. **Permission Errors**: Use virtual environment or user installation
4. **Build Failures**: Check Python version compatibility

### Debug Mode

Enable debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Use the SDK
client = PayAgencyApi(...)
```

## Contact

- **Email**: support@pay.agency
- **Documentation**: https://docs.pay.agency
- **GitHub**: https://github.com/vp-payomatix/payagency-python
- **Issues**: https://github.com/vp-payomatix/payagency-python/issues
