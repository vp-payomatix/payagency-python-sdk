#!/bin/bash

# PayAgency Python SDK Deployment Script
# This script helps deploy the package to PyPI repositories

echo "🚀 PayAgency Python SDK Deployment"
echo "======================================"

# Check if we have the required tools
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

if ! python3 -c "import build, twine" &> /dev/null; then
    echo "❌ Required tools not found. Installing build and twine..."
    pip3 install --upgrade build twine
fi

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info/

# Build the package
echo "📦 Building the package..."
python3 -m build

if [ $? -ne 0 ]; then
    echo "❌ Build failed!"
    exit 1
fi

echo "✅ Package built successfully!"
echo ""
echo "📝 Files created:"
ls -la dist/

echo ""
echo "🎯 Next Steps:"
echo "=============="
echo ""
echo "To deploy to TestPyPI:"
echo "1. Create an account at https://test.pypi.org"
echo "2. Generate an API token in Account Settings"
echo "3. Run: python3 -m twine upload --repository testpypi dist/*"
echo ""
echo "To deploy to PyPI (production):"
echo "1. Create an account at https://pypi.org"
echo "2. Generate an API token in Account Settings"
echo "3. Run: python3 -m twine upload dist/*"
echo ""
echo "🔐 API Token Setup:"
echo "==================="
echo "1. Go to Account Settings on PyPI/TestPyPI"
echo "2. Scroll to API tokens section"
echo "3. Click 'Add API token'"
echo "4. Name it 'payagency-api-deployment'"
echo "5. Scope: 'Entire account' (or specific project if it exists)"
echo "6. Copy the token (starts with pypi-)"
echo "7. Use this token when prompted during upload"
echo ""
echo "🧪 Test the deployed package:"
echo "============================"
echo "From TestPyPI:"
echo "pip install --index-url https://test.pypi.org/simple/ payagency-api"
echo ""
echo "From PyPI:"
echo "pip install payagency-api"
echo ""
echo "✨ Package is ready for deployment!"
