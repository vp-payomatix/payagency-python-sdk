# PayAgency Python SDK - Deployment Guide

## Overview

This guide will help you deploy the PayAgency Python SDK to PyPI (Python Package Index) for public distribution.

## Prerequisites

1. **Python 3.7+** installed
2. **Build tools** installed: `pip install build twine`
3. **PyPI Account** (for production) and/or **TestPyPI Account** (for testing)

## Step 1: Create PyPI Accounts

### TestPyPI (for testing)

1. Go to [https://test.pypi.org](https://test.pypi.org)
2. Click "Register" and create an account
3. Verify your email address

### PyPI (for production)

1. Go to [https://pypi.org](https://pypi.org)
2. Click "Register" and create an account
3. Verify your email address

## Step 2: Generate API Tokens

### For TestPyPI:

1. Log in to [https://test.pypi.org](https://test.pypi.org)
2. Go to Account Settings
3. Scroll to "API tokens" section
4. Click "Add API token"
5. Token name: `payagency-api-deployment`
6. Scope: "Entire account" (or specific project if exists)
7. Click "Add token"
8. **IMPORTANT**: Copy the token immediately (starts with `pypi-`)

### For PyPI:

1. Log in to [https://pypi.org](https://pypi.org)
2. Follow the same steps as TestPyPI above

## Step 3: Build the Package

Run the automated deployment script:

```bash
./deploy.sh
```

Or manually:

```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build the package
python3 -m build
```

This creates:

- `dist/payagency_api-1.0.0.tar.gz` (source distribution)
- `dist/payagency_api-1.0.0-py3-none-any.whl` (wheel distribution)

## Step 4: Deploy to TestPyPI (Recommended First)

```bash
python3 -m twine upload --repository testpypi dist/*
```

When prompted:

- **Username**: `__token__`
- **Password**: Your TestPyPI API token (starts with `pypi-`)

## Step 5: Test the TestPyPI Package

```bash
# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ payagency-api

# Test it works
python3 -c "from payagency_api import PayAgencyApi; print('✅ Package imported successfully!')"
```

## Step 6: Deploy to PyPI (Production)

Once testing is successful:

```bash
python3 -m twine upload dist/*
```

When prompted:

- **Username**: `__token__`
- **Password**: Your PyPI API token (starts with `pypi-`)

## Step 7: Verify Production Deployment

```bash
# Install from PyPI
pip install payagency-api

# Test it works
python3 -c "from payagency_api import PayAgencyApi; print('✅ Production package works!')"
```

## Package Information

- **Package Name**: `payagency-api`
- **Version**: `1.0.0`
- **PyPI URL**: https://pypi.org/project/payagency-api/
- **TestPyPI URL**: https://test.pypi.org/project/payagency-api/

## Installation Commands

### From PyPI (Production)

```bash
pip install payagency-api
```

### From TestPyPI (Testing)

```bash
pip install --index-url https://test.pypi.org/simple/ payagency-api
```

## Usage After Installation

```python
from payagency_api import PayAgencyApi

# Initialize the SDK
pay_agency = PayAgencyApi(
    encryption_key="89ca59fb3b49ada55851021df12cfbc5",
    secret_key="PA_TEST_your-secret-key"
)

# Make a payment
payment = pay_agency.payment.s2s({
    "first_name": "James",
    "last_name": "Dean",
    "email": "james@gmail.com",
    "amount": 100,
    "currency": "GBP",
    # ... other fields
})
```

## Troubleshooting

### Common Issues:

1. **403 Forbidden**: Invalid API token or insufficient permissions
2. **Package already exists**: Version number needs to be incremented
3. **Build fails**: Check dependencies and Python version compatibility

### Solutions:

1. **Increment Version**: Update version in `pyproject.toml` and `setup.py`
2. **Check Token**: Ensure API token is correct and has proper scope
3. **Clean Build**: Run `rm -rf build/ dist/ *.egg-info/` before building

## Security Notes

- **Never commit API tokens** to version control
- **Use environment variables** for tokens in CI/CD
- **Regenerate tokens** if compromised
- **Use scoped tokens** when possible

## Maintenance

To update the package:

1. Update version in `pyproject.toml` and `setup.py`
2. Update `CHANGELOG.md` (if exists)
3. Rebuild and redeploy following steps above

## Support

- Documentation: https://docs.pay.agency
- GitHub Issues: https://github.com/vp-payomatix/payagency-python/issues
- Email: support@pay.agency
