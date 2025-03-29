This repository contains a solution for calculating the credit rating of Residential Mortgage-Backed Securities (RMBS) based on the following mortgage attributes:

- Credit Score
- Loan-to-Value (LTV) Ratio
- Debt-to-Income (DTI) Ratio
- Loan Type (Fixed vs Adjustable)
- Property Type (Single-family vs Condo)

## How It Works

### 1. Input:
The solution takes a list of mortgages, each with the following attributes:
- `credit_score`: The credit score of the borrower (integer between 300 and 850).
- `loan_amount`: The total loan amount of the mortgage (float).
- `property_value`: The value of the mortgaged property (float).
- `annual_income`: The annual income of the borrower (float).
- `debt_amount`: The existing debt amount of the borrower (float).
- `loan_type`: The type of mortgage loan (either "fixed" or "adjustable").
- `property_type`: The type of property (either "single_family" or "condo").

### 2. Calculation:
The credit rating is calculated based on a risk score derived from:
- Loan-to-Value (LTV) Ratio
- Debt-to-Income (DTI) Ratio
- Credit Score
- Loan Type
- Property Type

The final credit rating is one of the following:
- "AAA" (Highly secure)
- "BBB" (Medium risk)
- "C" (Highly speculative or distressed)

### 3. Running the Code:
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/rmbs-credit-rating.git
