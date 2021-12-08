class TestResult:
  def __init__(self) -> None:
      self.runCount = 0
      self.errorCount = 0
      self.errorLog = ""
  def testStarted(self):
    self.runCount += 1
  def testFailed(self):
    self.errorCount += 1
  def addErrorLog(self, testName, errorLog):
    self.errorLog += f"Error Msg: {testName}\n{str(errorLog)}"
  def summary(self):
    return f"{self.runCount} run, {self.errorCount} failed"