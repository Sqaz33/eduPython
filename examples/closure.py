def make_multiplire(factor):
  calling_count = 0

  def multiplire(number):
    nonlocal calling_count
    calling_count += 1
    return number * factor
