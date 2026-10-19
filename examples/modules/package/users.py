from .validators import is_valid_age

class User:
  def __init__(self, age):
    if not is_valid_age(age):
      raise ValueError("age < 0")
    
    self._age = age
