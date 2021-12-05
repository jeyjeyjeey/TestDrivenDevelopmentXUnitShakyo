from kbtdd.WasRun import WasRun
from kbtdd.TestCase import TestCase

class TestCaseTest(TestCase):
  def testTemplateMethod(self):
    test = WasRun("testMethod")
    test.run()
    assert("setUp testMethod tearDown " == test.log)

TestCaseTest("testTemplateMethod").run()
