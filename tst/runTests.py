'''
Created on 2012-11-7

@author: x52chen
'''

import glob
import unittest
import os

    
if __name__ == '__main__':
    PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
    os.chdir(PROJECT_PATH)
    test_file_strings = glob.glob('Test*.py')
    
    module_strings = [str[0:len(str)-3] for str in test_file_strings]
    suites = [unittest.defaultTestLoader.loadTestsFromName(str) for str in module_strings]
    testSuite = unittest.TestSuite(suites)
    text_runner = unittest.TextTestRunner().run(testSuite)