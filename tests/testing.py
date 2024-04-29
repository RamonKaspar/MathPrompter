import unittest
import sys

# Add the root directory to sys.path to find the main module
sys.path.append('..')

from main import *
from test_cases import *

class Test(unittest.TestCase):
    def test_generate_algebric_template(self):
        for test in test_cases:
            question_template, mapping = generating_algebraic_template(test['q'])
            self.assertEqual(question_template, test['qt'], "The template does not match the expected template.")
            self.assertEqual(mapping, test['Mapping'], "The mapping does not match the expected mapping.")
    
    def test_compute_verification(self):
        for test in test_cases:
            qt, variable_mapping = generating_algebraic_template(test['q'])
            exp = algebric_expression_generation(qt)
            code= python_code_generation(qt)
            res = perform_computational_verification(exp, code, variable_mapping)
            self.assertEqual(res, test['Correct'], "Not the correct answer.")

if __name__ == '__main__':
    unittest.main()
