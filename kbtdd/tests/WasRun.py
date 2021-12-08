from kbtdd.TestCase import TestCase

class WasRun(TestCase):
  def setUp(self):
    self.log = "setUp "
  def testMethod(self):
    self.log += "testMethod "
  def testBrokenMethod(self):
    raise Exception("Expected Exception")
  def tearDown(self):
    self.log += "tearDown "
