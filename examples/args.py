
def example(name, *args, **kwargs):
  print(name)

  for a in args:
    print(a)
  
  for key, value in kwargs.items():
    print(key, '->', value) 

example('name', 1, 2, 3, x = 3, y = 4)

def add(a, b): return a + b

pair = [1, 2]
print(add(*pair))

def introduce(name, age):
  print(f'hi i\'am {name} - {age}')

user = {"name": "DefaultUser", "age": 0}

introduce(**user)