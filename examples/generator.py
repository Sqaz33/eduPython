def even_numbers(limit):
  for n in range(0, limit+1, 2):
    yield n

gen = even_numbers(6)
for n in gen:
  print(n)