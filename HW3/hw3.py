'''
Author: Marc Sulsenti
Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''

#Problem 1
def addOne(l):
    '''returns a list with one added to every # in the list'''
    if l == []:
        return []
    else:
        return ([l[0]+1])+addOne(l[1:])
        
#Problem 2
def explode(s):
    '''returns a list of the characters in  a string'''
    if s == "":
        return []
    else:
        return [s[0]]+explode(s[1:])
#Problem 3
def myFilter(f,l):
    '''returns the list of elements of l for which func is true'''
    if not l:
        return []
    if f(l[0]):
        return [l[0]]+myFilter(f,l[1:])
    else:
        return myFilter(f,l[1:])

    
#Problem 4
def sumPos(l):
    ''' returns the sum of only the positive numbers in the list'''
    if l == []:
        return 0
    elif (l[0]>0) == True:
        return l[0] + sumPos(l[1:])
    else:
        return sumPos(l[1:])




