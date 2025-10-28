"""
Example usage of PayAgency API Python SDK
"""

import os
from payagency_api import PayAgencyApi

# Initialize the SDK
pay_agency = PayAgencyApi(
    encryption_key=os.getenv("PAYAGENCY_ENCRYPTION_KEY", "89ca59fb3b49ada55851021df12cfbc5"),
    secret_key=os.getenv("PAYAGENCY_SECRET_KEY", "PA_TEST_your-secret-key"),
    # base_url is optional - defaults to https://backend.pay.agency
)


def example_s2s_payment():
    """Example S2S payment"""
    try:
        payment = pay_agency.payment.s2s({
            "first_name": "James",
            "last_name": "Dean",
            "email": "james@gmail.com",
            "address": "64 Hertingfordbury Rd",
            "country": "GB",
            "city": "Newport", 
            "state": "GB",
            "zip": "TF10 8DF",
            "ip_address": "127.0.0.1",
            "phone_number": "7654233212",
            "amount": 100,
            "currency": "GBP",
            "card_number": "4111111111111111",
            "card_expiry_month": "12",
            "card_expiry_year": "2027",
            "card_cvv": "029",
            "redirect_url": "https://pay.agency",
            "webhook_url": "https://pay.agency/webhook",
            "terminal_id": "T12345",
        })
        
        print("Payment successful:", payment)
        return payment
        
    except Exception as e:
        print(f"Payment failed: {e}")
        return None


def example_hosted_payment():
    """Example hosted payment"""
    try:
        payment = pay_agency.payment.hosted({
            "first_name": "James",
            "last_name": "Dean", 
            "email": "james@gmail.com",
            "address": "64 Hertingfordbury Rd",
            "country": "GB",
            "city": "Newport",
            "state": "GB", 
            "zip": "TF10 8DF",
            "ip_address": "127.0.0.1",
            "phone_number": "7654233212",
            "amount": 100,
            "currency": "GBP",
            "redirect_url": "https://pay.agency",
            "webhook_url": "https://pay.agency/webhook",
            "order_id": "ORDER_123",
            "terminal_id": "T12345",
        })
        
        print("Hosted payment successful:", payment)
        return payment
        
    except Exception as e:
        print(f"Hosted payment failed: {e}")
        return None


def example_payout():
    """Example payout"""
    try:
        payout = pay_agency.payout.create_payout({
            "wallet_id": "WAL1234567890",
            "first_name": "James",
            "last_name": "Dean",
            "email": "james@gmail.com",
            "address": "64 Hertingfordbury Rd",
            "country": "US",
            "city": "Newport",
            "state": "US",
            "zip": "TF10 8DF",
            "ip_address": "127.0.0.1",
            "phone_number": "7654233212",
            "amount": 100,
            "currency": "USD",
            "card_number": "4222222222222222",
            "card_expiry_month": "10",
            "card_expiry_year": "2030",
            "webhook_url": "https://pay.agency/webhook",
            "order_id": "ORDER_123",
        })
        
        print("Payout successful:", payout)
        return payout
        
    except Exception as e:
        print(f"Payout failed: {e}")
        return None


def example_get_wallets():
    """Example get wallets"""
    try:
        wallets = pay_agency.payout.get_wallets()
        print("Wallets:", wallets)
        return wallets
        
    except Exception as e:
        print(f"Get wallets failed: {e}")
        return None


def example_payment_link():
    """Example payment link creation"""
    try:
        payment_link = pay_agency.payment_link.create({
            "payment_template_id": "PLI07435325281394735",
            "amount": 1000,
            "currency": "USD",
            "expiry_date": "2024-12-31",
            "terminal_id": "T12345",
            "order_id": "ORDER_123",
        })
        
        print("Payment link created:", payment_link)
        return payment_link
        
    except Exception as e:
        print(f"Payment link creation failed: {e}")
        return None


def example_crypto_onramp():
    """Example crypto OnRamp"""
    try:
        onramp = pay_agency.crypto.on_ramp({
            "first_name": "Diana",
            "last_name": "Prince",
            "email": "diana@pay.agency", 
            "phone_number": "0123456789",
            "fiat_amount": 200,
            "fiat_currency": "EUR",
            "crypto_currency": "BTC",
            "wallet_address": "1BoatSLRHtKNngkdXEeobR76b53LETtpyT",
            "ip_address": "127.0.0.1",
            "country": "GB",
            "crypto_network": "BITCOIN",
            "redirect_url": "https://pay.agency",
            "webhook_url": "https://pay.agency/webhook",
            "order_id": "ORDER_123",
            "terminal_id": "T12345",
        })
        
        print("OnRamp successful:", onramp)
        return onramp
        
    except Exception as e:
        print(f"OnRamp failed: {e}")
        return None


def example_crypto_offramp():
    """Example crypto OffRamp"""
    try:
        offramp = pay_agency.crypto.off_ramp({
            "first_name": "Ethan",
            "last_name": "Hunt",
            "email": "ethan@pay.agency",
            "phone_number": "0123456789",
            "fiat_currency": "GBP",
            "crypto_currency": "BTC",
            "crypto_amount": "0.05",
            "wallet_address": "1BoatSLRHtKNngkdXEeobR76b53LETtpyT",
            "ip_address": "127.0.0.1",
            "country": "GB",
            "crypto_network": "BITCOIN",
            "redirect_url": "https://pay.agency",
            "webhook_url": "https://pay.agency/webhook",
            "order_id": "ORDER_123",
            "terminal_id": "T12345",
        })
        
        print("OffRamp successful:", offramp)
        return offramp
        
    except Exception as e:
        print(f"OffRamp failed: {e}")
        return None


def example_get_transactions():
    """Example get transactions"""
    try:
        transactions = pay_agency.txn.get_transactions({
            "transaction_start_date": "2023-01-01",
            "transaction_end_date": "2023-12-31",
        })
        
        print("Transactions:", transactions)
        return transactions
        
    except Exception as e:
        print(f"Get transactions failed: {e}")
        return None


def example_refund():
    """Example refund"""
    try:
        refund = pay_agency.refund({
            "reason": "Customer request",
            "transaction_id": "TXN_123",
        })
        
        print("Refund successful:", refund)
        return refund
        
    except Exception as e:
        print(f"Refund failed: {e}")
        return None


if __name__ == "__main__":
    print("PayAgency API Python SDK Examples")
    print("=" * 40)
    
    # Run examples
    print("\n1. S2S Payment Example:")
    example_s2s_payment()
    
    print("\n2. Hosted Payment Example:")
    example_hosted_payment()
    
    print("\n3. Payout Example:")
    example_payout()
    
    print("\n4. Get Wallets Example:")
    example_get_wallets()
    
    print("\n5. Payment Link Example:")
    example_payment_link()
    
    print("\n6. Crypto OnRamp Example:")
    example_crypto_onramp()
    
    print("\n7. Crypto OffRamp Example:") 
    example_crypto_offramp()
    
    print("\n8. Get Transactions Example:")
    example_get_transactions()
    
    print("\n9. Refund Example:")
    example_refund()
