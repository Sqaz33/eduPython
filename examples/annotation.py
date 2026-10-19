def greet(name: str, age: int | None = None) -> None:
  greetings = f'Hi {name}'
  breakpoint()
  if age is not None:
    greetings += f' age: {age}'
  print(greetings)

greet("1234")