'''
author : mithun

'''

###this programs checks for matching  brackets , paranthesis and braces in a string ###
### returns true if matches are found false other wise###
###doesnot consider strings inside single quotes ####

from stack import *


def isMatchingpair(char1,char2):
   
   #import pdb;pdb.set_trace();
   if (char1 == '{' and char2 == '}'):
      return 1
   elif (char1 == '[' and char2 == ']'):
      return 1
   elif (char1 == '(' and char2 == ')'):
      return 1
   else:
      return 0

ostack = myStack(); ## object for myStack
delimiter = "'"
def expBreaker(exp):
   ''' This function is to split the strings based on the delimiter.We will not consider the brackets 
   which are present within the delimiters'''
   return exp
def matchBracks(expression):
   expression = expBreaker(expression)
   for myvilla in expression:
      if myvilla in ('{','[','('):
         ostack.push(myvilla)
      if myvilla in ('}',']',')'):
         if ostack.isEmpty():
            return 0
         elif not  isMatchingpair(ostack.pop(),myvilla):
            return 0
   if ostack.isEmpty():
      return 1
   else:
      return 0

exp = raw_input() ## getting the string as input

if matchBracks(exp):
   print 'Balanced'
else:
   print 'Not balanced'

