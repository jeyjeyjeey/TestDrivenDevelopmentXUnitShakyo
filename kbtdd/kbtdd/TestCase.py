from abc import abstractmethod

class TestCase:
  def __init__(self, name) -> None:
    self.name = name

  @abstractmethod
  def setUp(self):
    pass

  def run(self, result):
    result.testStarted()
    self.setUp()
    try:
      method = getattr(self, self.name)
      method()
    except Exception as e:
      result.testFailed()
      result.addErrorLog(self.name, e)
    self.tearDown()
  @abstractmethod
  def tearDown(self):
    pass