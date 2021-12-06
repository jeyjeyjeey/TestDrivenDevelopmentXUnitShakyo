from abc import abstractmethod
from .TestResult import TestResult

class TestCase:
  def __init__(self, name) -> None:
    self.name = name

  @abstractmethod
  def setUp(self):
    pass

  def run(self):
    result = TestResult()
    result.testStarted()
    self.setUp()
    try:
      method = getattr(self, self.name)
      method()
    except:
      result.testFailed()
    self.tearDown()
    return result

  @abstractmethod
  def tearDown(self):
    pass