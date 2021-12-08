from kbtdd.TestCase import TestCase
from kbtdd.TestResult import TestResult
from kbtdd.TestSuite import TestSuite

from WasRun import WasRun

class TestCaseTest(TestCase):
  def setUp(self):
    self.result = TestResult()
  def testTemplateMethod(self):
    test = WasRun("testMethod")
    test.run(self.result)
    assert("setUp testMethod tearDown " == test.log)
  def testResult(self):
    test = WasRun("testMethod")
    test.run(self.result)
    assert(1 == self.result.runCount)
    assert(0 == self.result.errorCount)
  def testFailedResult(self):
    test = WasRun("testBrokenMethod")
    test.run(self.result)
    assert(1 == self.result.runCount)
    assert(1 == self.result.errorCount)
  def testFailedResultFormatting(self):
    self.result.testStarted()
    self.result.testFailed()
    assert(1 == self.result.runCount)
    assert(1 == self.result.errorCount)
  def testSuite(self):
    suite = TestSuite()
    suite.add(WasRun("testMethod"))
    suite.add(WasRun("testBrokenMethod"))
    suite.run(self.result)
    assert(2 == self.result.runCount)
    assert(1 == self.result.errorCount)
  def testFrailedTearDown(self):
    test = WasRun("testBrokenMethod")
    test.run(self.result)
    assert("setUp tearDown " == test.log)
  def testFailedOutputLog(self):
    test = WasRun("testBrokenMethod")
    test.run(self.result)
    assert("1 run, 1 failed" == self.result.summary())
    assert("Error Msg: testBrokenMethod\nExpected Exception" == self.result.errorLog)

suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testSuite"))
suite.add(TestCaseTest("testFrailedTearDown"))
suite.add(TestCaseTest("testFailedOutputLog"))
result = TestResult()
suite.run(result)
print(result.summary())