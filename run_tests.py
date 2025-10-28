"""
Integration test runner script - Run real API tests
"""

import os
import sys
import pytest

def run_integration_tests():
    """Run integration tests with real API calls"""
    
    print("🚀 Running PayAgency Python SDK Integration Tests")
    print("=" * 60)
    print("⚠️  WARNING: These tests make REAL API calls!")
    print("📋 Using the same test credentials as Node.js version")
    print("🔗 Base URL: https://api.pay.agency")
    print("🔑 Secret Key: PA_TEST_94bf3520bcbe435f2ed558c31ac664f3e72dfa3114a3232e436e25f9")
    print("=" * 60)
    
    # Set environment variables if not already set
    if not os.getenv("AUTH_TOKEN"):
        os.environ["AUTH_TOKEN"] = "PA_TEST_94bf3520bcbe435f2ed558c31ac664f3e72dfa3114a3232e436e25f9"
    
    if not os.getenv("ENCRYPTION_KEY"):
        os.environ["ENCRYPTION_KEY"] = "89ca59fb3b49ada55851021df12cfbc5"
    
    # Run integration tests
    integration_test_files = [
        "tests/test_s2s_integration.py",
        "tests/test_hosted_integration.py", 
        "tests/test_apm_integration.py",
        "tests/test_payout_integration.py",
        "tests/test_crypto_integration.py",
        "tests/test_payment_link_integration.py",
        "tests/test_txn_integration.py",
    ]
    
    # Run tests with verbose output
    args = [
        "-v",  # Verbose output
        "-s",  # Don't capture stdout (so we see print statements)
        "--tb=short",  # Short traceback format
        "--color=yes",  # Colored output
    ] + integration_test_files
    
    print("🧪 Running integration tests...")
    print("📝 Test output will show API responses for verification")
    print()
    
    result = pytest.main(args)
    
    if result == 0:
        print()
        print("🎉 All integration tests passed!")
        print("✅ PayAgency Python SDK is working correctly with real API")
    else:
        print()
        print("❌ Some integration tests failed")
        print("🔍 Check the output above for details")
    
    return result

def run_unit_tests():
    """Run unit tests (mocked)"""
    
    print("🧪 Running PayAgency Python SDK Unit Tests (Mocked)")
    print("=" * 60)
    
    # Run unit tests
    unit_test_files = [
        "tests/test_client.py",
        "tests/test_payment.py",
        "tests/test_payout.py",
    ]
    
    args = [
        "-v",  # Verbose output
        "--tb=short",  # Short traceback format
        "--color=yes",  # Colored output
        "--cov=payagency_api",  # Coverage
        "--cov-report=term-missing",  # Show missing lines
    ] + unit_test_files
    
    result = pytest.main(args)
    
    if result == 0:
        print()
        print("🎉 All unit tests passed!")
    else:
        print()
        print("❌ Some unit tests failed")
    
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "integration":
            exit(run_integration_tests())
        elif sys.argv[1] == "unit":
            exit(run_unit_tests())
        else:
            print("Usage: python run_tests.py [integration|unit]")
            print("  integration: Run real API tests")
            print("  unit: Run mocked unit tests")
            exit(1)
    else:
        print("Choose test type:")
        print("1. Integration tests (real API calls)")
        print("2. Unit tests (mocked)")
        print("3. Both")
        
        choice = input("Enter choice (1/2/3): ").strip()
        
        if choice == "1":
            exit(run_integration_tests())
        elif choice == "2":
            exit(run_unit_tests())
        elif choice == "3":
            unit_result = run_unit_tests()
            print("\n" + "="*60 + "\n")
            integration_result = run_integration_tests()
            exit(max(unit_result, integration_result))
        else:
            print("Invalid choice")
            exit(1)
