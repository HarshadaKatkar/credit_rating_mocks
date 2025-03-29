# Residential Mortgage-Backed Security (RMBS) Credit Rating Calculator

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
   git clone https://github.com/HarshadaKatkar/credit_rating_mocks.git

### 4. Install dependencies (if any):
     pip install -r requirements.txt

### 5. Run the program:
    python test_credit_rating.py

### 6. Testing:
    python -m unittest test_credit_rating.py

### 7. License:

### Key Decisions and Design:
- The `Mortgage` class encapsulates the attributes of each mortgage and calculates individual risk.
- The `RMBS` class aggregates all mortgages and calculates the total risk score, adjusting based on the average credit score.
- We used unit tests to verify the correctness of the business logic.
- `unittest` is used for unit testing as it is built into Python and widely adopted for testing purposes.

### Conclusion:
This solution provides a clear structure for calculating the credit rating for an RMBS based on the given mortgage attributes. The implementation follows modular principles, separating the logic into easy-to-manage classes. The unit tests ensure that the algorithm works as expected across various scenarios.
