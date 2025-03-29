class Mortgage:
    def __init__(self, credit_score, loan_amount, property_value, annual_income, debt_amount, loan_type, property_type):
    
        self.credit_score = credit_score
        self.loan_amount = loan_amount
        self.property_value = property_value
        self.annual_income = annual_income
        self.debt_amount = debt_amount
        self.loan_type = loan_type
        self.property_type = property_type

    def calculate_risk(self):
        
        risk_score = 0
        
        ltv_ratio = self.loan_amount / self.property_value
        if ltv_ratio > 0.90:
            risk_score += 2  
        elif ltv_ratio > 0.80:
            risk_score += 1  

       
        dti_ratio = (self.loan_amount + self.debt_amount) / self.annual_income
        if dti_ratio > 0.50:
            risk_score += 2  
        elif dti_ratio > 0.40:
            risk_score += 1  

        
        if self.credit_score >= 700:
            risk_score -= 1  
        elif self.credit_score < 650:
            risk_score += 1  

        
        if self.loan_type == "adjustable":
            risk_score += 1  

        
        if self.property_type == "condo":
            risk_score += 1 

        return risk_score

class RMBS:
    def __init__(self, mortgages):
       
        self.mortgages = mortgages

    def calculate_total_risk(self):
       
        total_risk = sum(mortgage.calculate_risk() for mortgage in self.mortgages)
        
        
        average_credit_score = sum(m.credit_score for m in self.mortgages) / len(self.mortgages)
        
        if average_credit_score >= 700:
            total_risk -= 1  
        elif average_credit_score < 650:
            total_risk += 1  

        return total_risk

    def get_credit_rating(self):
       
        total_risk = self.calculate_total_risk()
        
        if total_risk <= 2:
            return "AAA"  
        elif 3 <= total_risk <= 5:
            return "BBB"  
        else:
            return "C"  

def calculate_credit_rating(mortgages):
   
    rmbs = RMBS(mortgages)
    return rmbs.get_credit_rating()
