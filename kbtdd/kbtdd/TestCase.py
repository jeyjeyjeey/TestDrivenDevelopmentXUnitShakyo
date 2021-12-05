from abc import abstractmethod


class TestCase:
  def __init__(self, name) -> None:
    self.name = name
    
  @abstractmethod
  def setUp(self):
    pass

  def run(self):
    self.setUp()
    method = getattr(self, self.name)
    method()
    self.tearDown()

  @abstractmethod
  def tearDown(self):
    pass