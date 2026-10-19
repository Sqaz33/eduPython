#обычный метод получает self в качестве 1 парам

class User:
  def __init__(self, name, age):
    self._name = name
    self._age = age
  
  @classmethod
  def from_dict(cls, data): # если отнаследовать Admin(User) в cls будет Admin
    return cls(**data)

  @staticmethod
  def is_valid_age(age):
    return age >= 0

  def __str__(self):
    return f'{self._name}, {self._age}'
  
  def __repr__(self):
    return f'User(name={self._name!r}, age={self._age})'

  def __eq__(self, other):
    if not isinstance(other, User):
      return NotImplemented
    
    return (
      self._name == other._name
      and self._age == other._age
    )

u = User.from_dict({"name": "user1", "age": 0})
print(u)
print(User.is_valid_age(-1))
print(repr(u))
