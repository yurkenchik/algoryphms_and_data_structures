import glob
import unittest

testSuite = unittest.TestSuite()
test_file_strings = glob.glob('test_*.py')
module_strings = [filename[:-3] for filename in test_file_strings]

for module in module_strings:
    # Import the module
    mod = __import__(module)
    # Add tests from the module to the test suite
    testSuite.addTests(unittest.defaultTestLoader.loadTestsFromModule(mod))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(testSuite)