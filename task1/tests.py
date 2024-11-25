import unittest
from solution import strict


@strict
def add(a: int, b: int) -> int:
    """Пример функции для сложения двух чисел."""
    return a + b


@strict
def multiply(a: float, b: float) -> float:
    """Функция умножения двух вещественных чисел."""
    return a * b


@strict
def concatenate(a: str, b: str) -> str:
    """Конкатенация двух строк."""
    return a + b


@strict
def check_equality(a: bool, b: bool) -> bool:
    """Проверка равенства двух логических значений."""
    return a == b


class TestStrictDecorator(unittest.TestCase):
    def test_add_correct_types(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-10, 20), 10)
        self.assertEqual(add(0, 100), 100)

    def test_add_incorrect_types(self):
        with self.assertRaises(TypeError):
            add("hello", 42)
        with self.assertRaises(TypeError):
            add(123, "world")
        with self.assertRaises(TypeError):
            add(True, False)

    def test_multiply_correct_types(self):
        self.assertAlmostEqual(multiply(2.5, 4.0), 10.0)

    def test_multiply_incorrect_types(self):
        with self.assertRaises(TypeError):
            multiply("pi", 3.14159)
        with self.assertRaises(TypeError):
            multiply(6.28, True)

    def test_concatenate_correct_types(self):
        self.assertEqual(concatenate("Hello", " World"), "Hello World")
        self.assertEqual(concatenate("", "Empty string"), "Empty string")

    def test_concatenate_incorrect_types(self):
        with self.assertRaises(TypeError):
            concatenate(123, "number")
        with self.assertRaises(TypeError):
            concatenate("string", 456)

    def test_check_equality_correct_types(self):
        self.assertTrue(check_equality(True, True))
        self.assertFalse(check_equality(False, True))

    def test_check_equality_incorrect_types(self):
        with self.assertRaises(TypeError):
            check_equality(1, True)
        with self.assertRaises(TypeError):
            check_equality(False, "False")


if __name__ == '__main__':
    unittest.main()
