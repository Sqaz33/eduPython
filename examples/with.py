class Resource:
  def __enter__(self):
    print("enter")
    return self

  def __exit__(self, exc_type, exc_value, tracerback):
    print("exit")
    return False

  def work(self):
    print("work")

with Resource() as resource:
  resource.work()

print("vse")