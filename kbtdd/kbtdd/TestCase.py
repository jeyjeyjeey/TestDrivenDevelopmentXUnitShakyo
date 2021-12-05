class TestCase:
  def __init__(self, name) -> None:
      self.name = name

  def run(self):
    method = getattr(self, self.name)
    method()
