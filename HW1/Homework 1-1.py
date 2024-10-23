'''Marc Sulsenti, Homework 1
I pledge my honor that I have abided by the Stevens Honor System. '''
from cs115 import *
def add(x,y):
    ''' returns the sum of x and y'''
    return x+y
def mult(x,y):
    '''returns the product of x , y'''
    return x*y
    
def factorial(n):
    '''returns the factorial of an integer n'''
    if(n==0):
        return 1
    else:
        return reduce(mult, range(1,n+1))

def mean(l):
    '''Takes in a list and returns the average value of all the numbers in the list'''
    return (reduce(add,l))/len(l)



