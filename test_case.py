import unittest
from progfun import *


class TestAlgoritmos(unittest.TestCase):

    def test_vetor_maioria_retorna_true(self):
        arr = [1, 1, 1, 1, 1, 2, 3, 4, 5]
        self.assertEqual(True, vetor_maioria(arr, 0))

    def test_vetor_maioria_retorna_false(self):
        arr = [1, 1, 1, 1, 2, 2, 2, 2]
        self.assertEqual(False, vetor_maioria(arr, 0))

    def test_fibonacci_de_zero(self):
        self.assertEqual(0, fib(0))

    def test_fibonacci_de_um(self):
        self.assertEqual(1, fib(1))

    def test_fibonacci_de_sete(self):
        self.assertEqual(13, fib(7))

    def test_fibonacci_de_vinte(self):
        self.assertEqual(6765, fib(20))

if __name__ == "__main__":
    unittest.main()
