list1 = [n * n for n in range(5) if n % 2 != 0]
print(list1)


#gen expression
def make_even_numbers_gen(limit):
  return (n for n in range(0, limit + 1, 2))

for n in make_even_numbers_gen(6):
  print(n)

tuple1 = tuple(n for n in range(5))

print(sum(make_even_numbers_gen(1000)))

squares = {n: n * n for n in range(100)}

remainders = {n % 2 for n in range(5)}