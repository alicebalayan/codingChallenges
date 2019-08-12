'''
Problem: 
  Check if a number is a palindrome, return true. Check if its' descendant is a palindrome, return true.  
  
Example 1, palindrome: 10801 , true
palindrome descendant - has to be even numbered to calculate

Example 2, 
    123312 - not palindrome, 1+2 3+3 1+2 = 363 - descendant, true
    11 - palindrome, true. 1+1 = 2 - non palindrome, false

From: https://edabit.com/challenge/MvtxpxtFDrzEtA9k5
'''

def palindrome_descendant(num):
