import functools

def get_even(numbers: list[int]) -> list[int]:
  return [n for n in numbers if n % 2 == 0]

def make_test_stats_print(name = ''):
  def decorator(test_case):
    @functools.wraps(test_case)
    def test_stats_print(*args, **kwargs):
      try:
        test_case(*args, **kwargs)
      except AssertionError as error:
        print(f'test {name} - AssertionError: {str(error)}')
      else:
        if name != '':
          print(f'test {name} - OK')
    return test_stats_print
  return decorator

@make_test_stats_print("duplication preserved")
def test1():
  actual = get_even([2, 2, 3])
  expected = [2, 2, 1]
  assert actual == expected, (
    f'Expect {expected} actual {actual}'
  )

test1()