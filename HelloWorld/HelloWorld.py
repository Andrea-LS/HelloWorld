'''
Created on 2012-11-7

@author: burke
'''

PROJECT_AUTHOR = 'burke'

class User():
    def __init__(self,name):
        self.__name = name
    
    def sayWelcomeMessage(self):
        return 'Hello ' + self.__name

def getUser():
    return PROJECT_AUTHOR


if __name__ == '__main__':
    author = User(PROJECT_AUTHOR)
    print author.sayWelcomeMessage()
    