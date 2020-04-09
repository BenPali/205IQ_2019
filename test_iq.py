import unittest
from IQ import nom_function

class ProjectTest(unittest.TestCase):
    def testPourcentageComeback1min(self):
        a = 0.2
        self.assertEqual(71.3, round((calc_derivation(a, 1) - calc_derivation(a, 0)) * 100, 1))

    def testPourcentageComeback2min(self):
        a = 0.2
        self.assertEqual(94.2, round((calc_derivation(a, 2) - calc_derivation(a, 0)) * 100, 1))

if __name__ == '__main__':
    unittest.main()