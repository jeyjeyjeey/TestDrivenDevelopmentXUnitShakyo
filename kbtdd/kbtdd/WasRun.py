from . import TestCase

class WasRun(TestCase.TestCase):
  def __init__(self, name) -> None:
      self.wasRun = None
      super().__init__(name)
      
  def testMethod(self):
    self.wasRun = 1
