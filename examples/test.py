from unittest import TestCase

def get_even(numbers: list[int]) -> list[int]:
  return [n for n in numbers if n % 2 == 0]

class TestGetEven(TestCase):
  def test_duplicates(self):
    actual = get_even([2, 2, 3])
    self.assertEqual(actual, [2, 2])

  def test_none_raises_error(self):
    with self.assertRaises(TypeError):
      get_even(None)