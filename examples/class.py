class Base:
  def foo(self):
    print("hi1")


class Derived(Base):
  def foo(self):
      print("hi2");

if __name__ == '__main__':
  obj = Derived()
  obj.foo()



class User:
  def __init__(self):
    self._age = 0

  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, value):
    if value < 0:
        raise ValueError("age < 0")
    self._age = value 


class TaskService:
  def __init__(self, notifier):
    self._notifier = notifier

  def complete_task(self, task):
    task.complete()
    self._notifier.send(task.status())

class EmailNotifier:
  def send(self, text):
      print(text)
  
service = TaskService(EmailNotifier())