# TypeScript vs Python SDK Comparison

This document compares the TypeScript (Node.js) and Python versions of the PayAgency SDK.

## Installation

### TypeScript/Node.js

```bash
npm install payagency-api-beta
```

### Python

```bash
pip install payagency-api
```

## Initialization

### TypeScript/Node.js

```typescript
import { PayAgencyApi } from "payagency-api-beta";

const payAgency = new PayAgencyApi({
  encryptionKey: "89ca59fb3b49ada55851021df12cfbc5",
  secretKey: "PA_TEST_your-secret-key",
  baseUrl: "https://backend.pay.agency", // optional
});
```

### Python

```python
from payagency_api import PayAgencyApi

pay_agency = PayAgencyApi(
    encryption_key="89ca59fb3b49ada55851021df12cfbc5",
    secret_key="PA_TEST_your-secret-key",
    base_url="https://backend.pay.agency",  # optional
)
```

## API Usage Comparison

### S2S Payment

#### TypeScript/Node.js

```typescript
const payment = await payAgency.Payment.S2S({
  first_name: "James",
  last_name: "Dean",
  email: "james@gmail.com",
  // ... other fields
  amount: 100,
  currency: "GBP",
  card_number: "4111111111111111",
  card_expiry_month: "12",
  card_expiry_year: "2027",
  card_cvv: "029",
  redirect_url: "https://pay.agency",
});
```

#### Python

```python
payment = pay_agency.payment.s2s({
    "first_name": "James",
    "last_name": "Dean",
    "email": "james@gmail.com",
    # ... other fields
    "amount": 100,
    "currency": "GBP",
    "card_number": "4111111111111111",
    "card_expiry_month": "12",
    "card_expiry_year": "2027",
    "card_cvv": "029",
    "redirect_url": "https://pay.agency",
})
```

### Payout Operations

#### TypeScript/Node.js

```typescript
// Get wallets
const wallets = await payAgency.Payout.wallets;
// OR
const wallets = await payAgency.Payout.get_wallets();

// Create payout
const payout = await payAgency.Payout.payout(payoutData);

// Estimate fee
const fee = await payAgency.Payout.esitimate_fee(feeData);
```

#### Python

```python
# Get wallets
wallets = pay_agency.payout.get_wallets()

# Create payout
payout = pay_agency.payout.create_payout(payout_data)

# Estimate fee
fee = pay_agency.payout.estimate_fee(fee_data)
```

### Crypto Operations

#### TypeScript/Node.js

```typescript
// OnRamp
const onRamp = await payAgency.Crypto.on_ramp(onRampData);

// OffRamp
const offRamp = await payAgency.Crypto.off_ramp(offRampData);

// Payment link
const link = await payAgency.Crypto.on_ramp_link(linkData);
```

#### Python

```python
# OnRamp
on_ramp = pay_agency.crypto.on_ramp(on_ramp_data)

# OffRamp
off_ramp = pay_agency.crypto.off_ramp(off_ramp_data)

# Payment link
link = pay_agency.crypto.on_ramp_link(link_data)
```

### Payment Links

#### TypeScript/Node.js

```typescript
const paymentLink = await payAgency.PaymentLink.create(linkData);
const templates = await payAgency.PaymentLink.templates;
```

#### Python

```python
payment_link = pay_agency.payment_link.create(link_data)
templates = pay_agency.payment_link.get_templates()
```

### Transactions

#### TypeScript/Node.js

```typescript
const transactions = await payAgency.TXN.transactions(queryParams);
const walletTxns = await payAgency.TXN.wallet_transaction(queryParams);
```

#### Python

```python
transactions = pay_agency.txn.get_transactions(query_params)
wallet_txns = pay_agency.txn.get_wallet_transactions(query_params)
```

### Refunds

#### TypeScript/Node.js

```typescript
const refund = await payAgency.refund(refundData);
```

#### Python

```python
refund = pay_agency.refund(refund_data)
```

## Key Differences

### 1. Naming Conventions

| TypeScript   | Python       | Description               |
| ------------ | ------------ | ------------------------- |
| `camelCase`  | `snake_case` | Method and property names |
| `PascalCase` | `snake_case` | Module names              |
| `baseUrl`    | `base_url`   | Constructor parameters    |

### 2. Object Access Patterns

| TypeScript                        | Python                                    | Description          |
| --------------------------------- | ----------------------------------------- | -------------------- |
| `payAgency.Payment.S2S()`         | `pay_agency.payment.s2s()`                | Module method access |
| `payAgency.Payout.wallets`        | `pay_agency.payout.get_wallets()`         | Property vs method   |
| `payAgency.PaymentLink.templates` | `pay_agency.payment_link.get_templates()` | Getter vs method     |

### 3. Data Structures

#### TypeScript (Object)

```typescript
const data = {
  firstName: "John",
  lastName: "Doe",
  amount: 100,
};
```

#### Python (Dictionary)

```python
data = {
    "first_name": "John",
    "last_name": "Doe",
    "amount": 100
}
```

### 4. Error Handling

#### TypeScript

```typescript
try {
  const payment = await payAgency.Payment.S2S(data);
} catch (error) {
  if (error.response) {
    console.error("API Error:", error.response.data);
  } else {
    console.error("Network Error:", error.message);
  }
}
```

#### Python

```python
from payagency_api import PayAgencyAPIError, PayAgencyNetworkError

try:
    payment = pay_agency.payment.s2s(data)
except PayAgencyAPIError as e:
    print(f"API Error: {e.message}")
    print(f"Status: {e.status_code}")
except PayAgencyNetworkError as e:
    print(f"Network Error: {e.message}")
```

### 5. Type Support

#### TypeScript

```typescript
import { S2SInput, S2SOutput } from "payagency-api-beta";

const data: S2SInput = {
  // TypeScript provides compile-time type checking
};

const result: S2SOutput = await payAgency.Payment.S2S(data);
```

#### Python

```python
from payagency_api.types import S2SInput, PaymentResponse

# Type hints for better IDE support
data: S2SInput = {
    # Python provides runtime type hints
}

result: PaymentResponse = pay_agency.payment.s2s(data)
```

### 6. Async/Await vs Synchronous

#### TypeScript (Async)

```typescript
// All methods are async and return Promises
const payment = await payAgency.Payment.S2S(data);
```

#### Python (Synchronous)

```python
# All methods are synchronous and return directly
payment = pay_agency.payment.s2s(data)
```

### 7. Environment Detection

Both SDKs automatically detect environment based on secret key:

- `PA_TEST_` → test environment
- `PA_LIVE_` → live environment

### 8. Encryption

Both SDKs automatically handle:

- AES-256-CBC encryption of request payloads
- Skip encryption for certain endpoints (payment links, refunds)
- Environment-based endpoint selection

## Feature Parity

| Feature               | TypeScript | Python | Notes                     |
| --------------------- | ---------- | ------ | ------------------------- |
| S2S Payments          | ✅         | ✅     | Full support              |
| Hosted Payments       | ✅         | ✅     | Full support              |
| APM Payments          | ✅         | ✅     | Full support              |
| Payouts               | ✅         | ✅     | Full support              |
| Wallets               | ✅         | ✅     | Mock data in test env     |
| Fee Estimation        | ✅         | ✅     | Mock data in test env     |
| Payment Links         | ✅         | ✅     | Full support              |
| Crypto OnRamp         | ✅         | ✅     | Full support              |
| Crypto OffRamp        | ✅         | ✅     | Full support              |
| Crypto PayIn          | ✅         | ✅     | Full support              |
| Transactions          | ✅         | ✅     | Full support              |
| Refunds               | ✅         | ✅     | Full support              |
| Type Definitions      | ✅         | ✅     | TypeScript vs Type Hints  |
| Error Handling        | ✅         | ✅     | Different exception types |
| Environment Detection | ✅         | ✅     | Same logic                |
| Encryption            | ✅         | ✅     | Same algorithm            |

## Migration Guide

### From TypeScript to Python

1. **Installation**: Replace `npm install` with `pip install`
2. **Import**: Change `import` to `from ... import`
3. **Initialization**: Convert object to keyword arguments
4. **Method calls**: Convert camelCase to snake_case
5. **Data structures**: Convert objects to dictionaries
6. **Error handling**: Use Python exception classes
7. **Async/await**: Remove async/await keywords

### From Python to TypeScript

1. **Installation**: Replace `pip install` with `npm install`
2. **Import**: Change `from ... import` to `import`
3. **Initialization**: Convert keyword arguments to object
4. **Method calls**: Convert snake_case to camelCase
5. **Data structures**: Convert dictionaries to objects
6. **Error handling**: Use try/catch with axios errors
7. **Async/await**: Add async/await keywords

## Best Practices

### Both Platforms

1. Store API keys in environment variables
2. Use HTTPS for webhook URLs
3. Implement proper error handling
4. Log transactions for auditing
5. Validate webhook signatures
6. Use test environment for development

### TypeScript Specific

1. Leverage TypeScript's type system
2. Use async/await for better readability
3. Handle Promise rejections properly

### Python Specific

1. Use type hints for better IDE support
2. Follow PEP 8 style guidelines
3. Use virtual environments for isolation

## Performance Considerations

- **TypeScript**: Event-driven, non-blocking I/O
- **Python**: Blocking I/O by default, consider async libraries for high concurrency
- **Both**: Connection pooling, request timeouts, retry mechanisms

## Support and Documentation

- **TypeScript**: https://github.com/vp-payomatix/payagency-npm
- **Python**: https://github.com/vp-payomatix/payagency-python
- **Common**: https://docs.pay.agency
