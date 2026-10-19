
x = [1, 2, 3]

it = iter(x)

print(next(it))
print(next(it))
print(next(it))
try:
  print(next(it))
except StopIteration as error:
  print('StopIteration')