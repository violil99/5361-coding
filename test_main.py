# To run your test please use the following commend:
# python3 -m unittest test_main.py
# or if you don't have python3 use:
# python -m unittest test_main.py

import unittest
import main

class TestMainMethods(unittest.TestCase):
    def test_evaluate_statement(self):
        self.assertEqual(main.evaluate_statement('P1 IF P2', {'P1': True, 'P2': False}), False)
        self.assertEqual(main.evaluate_statement('P1 IF ( P2 OR NOT P3 )', {'P1': True, 'P2': False, 'P3': True}), False)
        self.assertEqual(main.evaluate_statement('( NOT P1 AND ( P1 OR P2 ) ) IF P2', {'P1': False, 'P2': False}), True)
        self.assertEqual(main.evaluate_statement('( NOT P1 AND ( P1 OR P2 ) ) IF P2', {'P1': False, 'P2': True}), True)
        self.assertEqual(main.evaluate_statement('( NOT P1 AND ( P1 OR P2 ) ) IF P2', {'P1': True, 'P2': False}), True)
        self.assertEqual(main.evaluate_statement('( NOT P1 AND ( P1 OR P2 ) ) IF P2', {'P1': True, 'P2': True}), True)
        self.assertEqual(main.evaluate_statement('P2 AND ( P1 IF NOT P2 ) AND ( NOT P1 IF NOT P2 )', {'P1': True, 'P2': True}), False)
        self.assertEqual(main.evaluate_statement('P2 AND ( P1 IF NOT P2 ) AND ( NOT P1 IF NOT P2 )', {'P1': True, 'P2': False}), False)
        self.assertEqual(main.evaluate_statement('P2 AND ( P1 IF NOT P2 ) AND ( NOT P1 IF NOT P2 )', {'P1': False, 'P2': True}), False)
        self.assertEqual(main.evaluate_statement('P2 AND ( P1 IF NOT P2 ) AND ( NOT P1 IF NOT P2 )', {'P1': False, 'P2': False}), False)
        self.assertEqual(main.evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': True, 'P2': True, 'P3': True}), True)
        self.assertEqual(main.evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': True, 'P2': True, 'P3': False}), True)
        self.assertEqual(main.evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': False, 'P2': True, 'P3': False}), False)
        self.assertEqual(main.evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': True, 'P2': False, 'P3': False}), True)
        self.assertEqual(main.evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': True, 'P2': False, 'P3': True}), True)
        self.assertEqual(main.evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': False, 'P2': False, 'P3': True}), True)
        self.assertEqual(main.evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': False, 'P2': True, 'P3': True}), True)
        self.assertEqual(main.evaluate_statement('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', {'P1': False, 'P2': False, 'P3': False}), False)

    def test_generate_truth_table(self):
        pass

    def test_statement_type(self):
        self.assertEqual(main.statement_type('( NOT P1 AND ( P1 OR P2 ) ) IF P2', ['P1', 'P2']), 'tautology')
        self.assertEqual(main.statement_type('P2 AND ( P1 IF NOT P2 ) AND ( NOT P1 IF NOT P2 )', ['P1', 'P2']), 'contradiction')
        self.assertEqual(main.statement_type('( P1 IF ( P2 IF P3 ) ) IF ( ( P1 IF P2 ) IF P3 )', ['P1', 'P2', 'P3']), 'contingency')

if __name__ == "__main__":
    unittest.main() 