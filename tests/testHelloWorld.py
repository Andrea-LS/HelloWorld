'''
Created on 2012-11-7

@author: burke
'''
import unittest
from HelloWorld import *

class TestHelloWorld(unittest.TestCase):
    
    def testGetUser(self):
        self.assertEquals(PROJECT_AUTHOR, getUser())

    def testGetWelcomeMessage(self):
        message = User(PROJECT_AUTHOR).sayWelcomeMessage()
        self.assertEquals('Hello ' + PROJECT_AUTHOR, message)
        
    def testGetExceptionWhileGetingPrivateUserName(self):
        try:
            User(PROJECT_AUTHOR).__name
            self.fail('Private member in class User can\'t be access')
        except Exception, e:
            self.assertEquals('User instance has no attribute \'_TestHelloWorld__name\'', str(e))


if __name__ == "__main__":
    unittest.main()