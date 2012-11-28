import unittest
from progfun import factorial, fib, vetor_maioria, div_by_three_or_five, primo


class TestAlgoritmos(unittest.TestCase):

    def test_factorial_de_zero(self):
        self.assertEqual(1, factorial(0))

    def test_factorial_de_um(self):
        self.assertEqual(1, factorial(1))

    def test_factorial_de_oito(self):
        self.assertEqual(40320, factorial(8))

    def test_vetor_eh_maioria(self):
        arr = [1, 1, 1, 1, 1, 3, 4, 5, 6]
        self.assertEqual(True, vetor_maioria(arr))

    def test_vetor_nao_eh_maioria(self):
        arr = range(10)
        self.assertEqual(False, vetor_maioria(arr))

    def test_fibonacci_de_zero(self):
        self.assertEqual(0, fib(0))

    def test_fibonacci_de_um(self):
        self.assertEqual(1, fib(1))

    def test_fibonacci_de_sete(self):
        self.assertEqual(13, fib(7))

    def test_fibonacci_de_vinte(self):
        self.assertEqual(6765, fib(20))

    def test_div_by_three_or_five_with_array_of_1000(self):
        self.assertEqual(233168, div_by_three_or_five(range(1000)))

    def test_numero_3_eh_primo(self):
        self.assertEqual(True, primo(3, range(1, 100)))

    def test_numero_4_nao_eh_primo(self):
        self.assertEqual(False, primo(4, range(1, 100)))

if __name__ == "__main__":
    unittest.main()
