from functools import wraps

def log_call(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    print('Вызываем фукнцию')
    func(*args, **kwargs)
  
  return wrapper

@log_call
def add(a, b):
  print(a + b)

add(1, 2)