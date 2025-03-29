# credit_rating.py

class Mortgage:
    def __init__(self, credit_score, loan_amount, property_value, annual_income, debt_amount, loan_type, property_type):
        """
        Initialize a mortgage object with the provided attributes.
        
        :param credit_score: Credit score of the borrower (int).
        :param loan_amount: Loan amount for the mortgage (float).
        :param property_value: Value of the mortgaged property (float).
        :param annual_income: Borrower's annual income (float).
        :param debt_amount: Existing debt amount of the borrower (float).
        :param loan_type: Type of loan - "fixed" or "adjustable" (str).
        :param property_type: Type of property - "single_family" or "condo" (str).
        """
        self.credit_score = credit_score
        self.loan_amount = loan_amount
        self.property_value = property_value
        self.annual_income = annual_income
        self.debt_amount = debt_amount
        self.loan_type = loan_type
        self.property_type = property_type

    def calculate_risk(self):
        """
        Calculate the risk score for an individual mortgage based on the given criteria.

        :return: Risk score for this mortgage (int).
        """
        risk_score = 0
        
        # 1. Loan-to-Value (LTV) Ratio
        ltv_ratio = self.loan_amount / self.property_value
        if ltv_ratio > 0.90:
            risk_score += 2  # LTV > 90%
        elif ltv_ratio > 0.80:
            risk_score += 1  # LTV > 80%

        # 2. Debt-to-Income (DTI) Ratio
        dti_ratio = (self.loan_amount + self.debt_amount) / self.annual_income
        if dti_ratio > 0.50:
            risk_score += 2  # DTI > 50%
        elif dti_ratio > 0.40:
            risk_score += 1  # DTI > 40%

        # 3. Credit Score
        if self.credit_score >= 700:
            risk_score -= 1  # Credit Score >= 700
        elif self.credit_score < 650:
            risk_score += 1  # Credit Score < 650

        # 4. Loan Type
        if self.loan_type == "adjustable":
            risk_score += 1  # Adjustable-rate loan

        # 5. Property Type
        if self.property_type == "condo":
            risk_score += 1  # Condo property

        return risk_score

class RMBS:
    def __init__(self, mortgages):
        """
        Initialize RMBS with a list of mortgages.
        
        :param mortgages: List of Mortgage objects.
        """
        self.mortgages = mortgages

    def calculate_total_risk(self):
        """
        Calculate the total risk score for the RMBS by summing the risk scores of individual mortgages.

        :return: Total risk score for RMBS (int).
        """
        total_risk = sum(mortgage.calculate_risk() for mortgage in self.mortgages)
        
        # 6. Adjust final risk score based on average credit score
        average_credit_score = sum(m.credit_score for m in self.mortgages) / len(self.mortgages)
        
        if average_credit_score >= 700:
            total_risk -= 1  # Average credit score >= 700
        elif average_credit_score < 650:
            total_risk += 1  # Average credit score < 650

        return total_risk

    def get_credit_rating(self):
        """
        Based on the total risk score, assign a credit rating.
        
        :return: Credit rating ("AAA", "BBB", or "C").
        """
        total_risk = self.calculate_total_risk()
        
        if total_risk <= 2:
            return "AAA"  # Highly secure
        elif 3 <= total_risk <= 5:
            return "BBB"  # Medium risk
        else:
            return "C"  # Highly speculative or distressed

def calculate_credit_rating(mortgages):
    """
    Main function to calculate the credit rating for RMBS.
    
    :param mortgages: List of Mortgage objects.
    :return: Credit rating as a string ("AAA", "BBB", or "C").
    """
    rmbs = RMBS(mortgages)
    return rmbs.get_credit_rating()
