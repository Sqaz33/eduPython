
if __name__ == '__main__':
  try:
    x = int("1234s")
  except ValueError as error:
    print(f'{error}')

def parse_number(string):
  try:
    return int(string)
  except ValueError:
    #raise прокинуть исключение дальше
    return None
  # else чтобы отделить от ожидаемой ошибки
  # finaly выполнить в любом случае

class TaskAlreadyCompletedError(Exception): pass