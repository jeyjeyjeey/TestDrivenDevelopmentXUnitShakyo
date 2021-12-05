from kbtdd.WasRun import WasRun

test = WasRun("testMethod")
assert(not test.wasRun)
test.run()
assert(test.wasRun)
