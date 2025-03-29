import unittest
from credit_rating import Mortgage, calculate_credit_rating

class TestRMBSCreditRating(unittest.TestCase):
    
    def test_valid_mortgages(self):
    
        mortgages = [
            Mortgage(750, 200000, 250000, 60000, 20000, "fixed", "single_family"),
            Mortgage(680, 150000, 175000, 45000, 10000, "adjustable", "condo")
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "BBB")
    
    def test_aaa_rating(self):
       
        mortgages = [
            Mortgage(750, 100000, 200000, 80000, 5000, "fixed", "single_family"),
            Mortgage(720, 120000, 150000, 70000, 7000, "fixed", "single_family")
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "AAA")
    
    def test_c_rating(self):
        
        mortgages = [
            Mortgage(600, 300000, 250000, 50000, 40000, "adjustable", "condo"),
            Mortgage(620, 250000, 200000, 40000, 30000, "adjustable", "condo")
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "C")
    
    def test_edge_cases(self):
        
        mortgages = [
            Mortgage(640, 300000, 250000, 40000, 30000, "adjustable", "condo")
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "C")
    
    def test_average_credit_score_adjustment(self):
        
        mortgages = [
            Mortgage(750, 200000, 250000, 60000, 20000, "fixed", "single_family"),
            Mortgage(680, 150000, 175000, 45000, 10000, "adjustable", "condo"),
            Mortgage(700, 180000, 200000, 50000, 15000, "fixed", "single_family")
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "BBB")

if __name__ == '__main__':
    unittest.main()
