from Logics import test as LogicTest
from board import test as BoardTest

tests = {"Logics": LogicTest, "Board": BoardTest}

if __name__ == "__main__":
	for module,function in tests.iteritems():
		print "Testing:", module		
		function()
		print "Finished", module, "tests"
