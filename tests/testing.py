import unittest
import sys

# Add the root directory to sys.path to find the main module
sys.path.append('..')

from main import *
from test_cases import *

class Test(unittest.TestCase):
    def test_algebraic_template_generation(self):
        results = []
        for index, test in enumerate(test_cases, start=1):
            try:
                question_template, mapping = generating_algebraic_template(test['q'])
                print("------------------------------")
                print(f"TEST {index}")
                print("Question:", test['q'])
                print("Question Transformed:", question_template)
                print("Calculated Mapping:", mapping)
                print("Expected Template:", test['qt'])
                print("Expected Mapping:", test['Mapping'])
                self.assertEqual(question_template, test['qt'])
                self.assertEqual(mapping, test['Mapping'])
                results.append(True)
            except AssertionError as e:
                print(f"FAILED: {str(e)}")
                results.append(False)
        
        self.assertTrue(all(results), "Some algebra templates did not match the expectations.")
    
    def test_compute_verification(self):
        results = []
        for index, test in enumerate(test_cases, start=1):
            try:
                question_template, variable_mapping = generating_algebraic_template(test['q'])
                algebraic_expression = algebric_expression_generation(question_template)
                python_code = python_code_generation(question_template)
                outcome = perform_computational_verification(algebraic_expression, python_code, variable_mapping)
                print("------------------------------")
                print(f"TEST {index}")
                print("Generated Algebraic Expression:", algebraic_expression)
                print("Generated Python Code:", python_code)
                print("Expected Answer", test['Correct'])
                print("Calculated Answer", outcome)
                self.assertEqual(outcome, test['Correct'])
                results.append(True)
            except AssertionError as e:
                print(f"FAILED: {str(e)}")
                results.append(False)
        
        self.assertTrue(all(results), "Some computational verifications failed.")

if __name__ == '__main__':
    unittest.main()
