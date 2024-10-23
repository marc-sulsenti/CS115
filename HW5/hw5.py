'''
Created on November 2nd 2022
@author:   Marc Sulsenti
Pledge:    I Pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 5
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
#Testing for compression
#num to binary and binary to num needed)


def numToBinary(n):
    '''Converts at base 10 number to base 2'''
    if (n<=0):
        return''
    else:
        return str(numToBinary(n//2)) + str(n%2)+ ''

def binaryToNum(s):
    '''Converts a base 2 number to base 10'''
    if s =='': return 0
    else:
        return 0+(int(s[0])*2**(len(s)-1))+binaryToNum(s[1:])

def binary_help(s):
    """Will return a binary number that is the correct bit length (5 bits)"""
    if len(s) >= COMPRESSED_BLOCK_SIZE:
        return s
    else:
        return binary_help('0'+s)
    
def repeat2(l,s):
    '''Finds how many times the character l is FIRST repeated in string s'''
    #This repeat function, is not restricted by MAX_RUN_LENGTH
    if s=='':
        return 0
    elif(l==s[0]):
        return  1+repeat(l,s[1:])
    else:
        return 0
    
def repeat(l,s):
    '''Finds how many times the character l is FIRST repeated in string s'''
    #add in repeats cannot be larger than the max runtime (31)
    if s=='':
        return 0
    elif(l==s[0]):
        check = 1+repeat(l,s[1:])
        if(check>=MAX_RUN_LENGTH):
            return MAX_RUN_LENGTH
        else:
            return check
    else:
        return 0

    
def compress_help(s):
    ''''Helper function for compress. Returns the 6 bit format. the first bit is a 1 or a 0. the next n bits tell how many 1s or 0s would follow'''
    if s =='':
        return ""
    if(repeat2('1',s)>MAX_RUN_LENGTH):
        return binary_help(numToBinary(repeat('1',s)))+('0' * 5)+compress_help(s[repeat('1',s)
                                                                                 :])
    
    if(repeat2('0',s)>MAX_RUN_LENGTH):
        return binary_help(numToBinary(repeat('0',s)))+('0' * 5)+compress_help(s[repeat('0',s):])
    
    elif s[0] == '1':
        return binary_help(numToBinary(repeat('1',s)))+compress_help(s[repeat('1',s):])

    else:
        return  binary_help(numToBinary(repeat('0',s)))+compress_help(s[repeat('0',s):])


def compress(s):
    '''Compress a string of bits s'''
    if s[0] == '1':
        return ('0'*5)+compress_help(s)
    else:
        return compress_help(s)

        
def uncompress_help(x, s):
    if s == '':
        return ''
    elif x == '1':
        return binaryToNum(s[:5]) * '1' + uncompress_help('0', s[5:])
    elif x == '0':
        return binaryToNum(s[:5]) * '0' + uncompress_help('1', s[5:])

def uncompress(s):
    '''uncompresses a string of bits s'''
    if s == '':
        return '0'
    return uncompress_help('0',s)

def compression(s):
    """Returns the compression ratio of a compressed str compared to an uncompressed str"""
    return len(compress(s))/len(s)

#SET UP COMPRESSION RATIO TESTER FUNCTION
def tests():
    #peguin
    print(compression("00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"))
    #smile
    print(compression("0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8))
    #five
    print(compression("1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"))

'''
Comment Questions
Question 1
The maximum number of bits my compression algorithim could possibly use, is 325 bits. The reasoning
behind this is that the most ineffection compression would be the bits '10' repeat 32 times to create a repeating pattern of 64 bits.
This would require the algorithim to count have to use 5 bits to represent every 1 1 and every 1 0. 5 bits*64 bits = 320 bits + 5 bits for the extra 00000 at the begining
for when the sequence of 64 bits starts with a 1 to represent that there are 0 0s at the begining.

Question 2
The tests i conduced was that I used the compression function, and the images provided to find the ratio of the compressed function to the uncompressed function.
Compression ratios testing
all of these ratios can be found by running the tests function
Penguin picture compression ratio - 1.484375
Smile picture compression ratio - 1.328125
Five picture compression ratio - 1.015625

With these three tests, I have found that my algoritihim uncsucessfully shortens all of the images. The compressed stings of bits actually come out larger than the original strings.
the only image that came close to a 1:1 comparrison was the five picture, which was off by a value of 0.015625.

Question 3
Such an algrothim simply cannot exist.
Professor Lai is essentially claiming that her algorithim is 100% efficient. It is known that in the real world, no machine object, or program can be entirely 100% efficient.
This measn that there is an a string of 64 bits that when plugged into Professor Lai's algorithim will make it inefficient. A certain series of 1s and 0s will take up more effort
to be represented by the algorithim than if they were left alone. Computers use patterns to understand the bits relayed to them, and these patterns can easily be inefficient.

For example in my algorithim, the pattern goes
how manys 0s (represented in 5 bits) how manys 1s (represented in 5 bits) and continues until the end of the original string.
This program is incredibly inefficient when in the original 64-bit string you keep alternating between 1s and 0s. If you alternate,
the computer will keep having to use 5 bits to represent just one.

In conclusion, in the idea that no machine is 100% efficient, there will always be a certain 64 bit string, that causes Professor Lai's algorithim to become inefficient.

'''

