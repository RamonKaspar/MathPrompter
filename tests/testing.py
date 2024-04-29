import unittest
import sys

# Add the root directory to sys.path to find the main module
sys.path.append('..')

from main import generating_algebraic_template
from test_cases import *

class Test(unittest.TestCase):
    def test_generate_algebric_template(self):
        for test in test_cases:
            question_template, mapping = generating_algebraic_template(test['q'])
            self.assertEqual(question_template, test['qt'], "The template does not match the expected template.")
            self.assertEqual(mapping, test['Mapping'], "The mapping does not match the expected mapping.")

if __name__ == '__main__':
    unittest.main()
