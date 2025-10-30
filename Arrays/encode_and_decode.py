"""
LeetCode - Encode And Decode Strings
Difficulty: Medium
https://leetcode.com/problems/encode-and-decode-strings/description/

Problem:
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Approach:

"""

test=["neet","code","love","you"]

# Output:["neet","code","love","you"]



'''
The thing is that i want to transforme my input in ONE string , in a way i can recover this later as the same list

So i need to know where the word finishes and the other begins

So a solution is to keep the SIZE of each word before it and make a marker for each word , even if it has a comma , space etc

'''


# my sep will be '#' 
def encode(strs):
    encoded = ''
    for word in strs:
        size = len(word)
        # Now i will add the size and the sep with each word
        encoded += str(size)+ '#' + word
        #print(f"This is my encoded : {encoded} and i am treating now the word \t {word}")

    return encoded

def decode(s):

    # Using the method of strings s.find(#) to find the position inside the string

    # I will get the FULL string and check the SIZE and the sep marker

    # When i get to the size i will run until i find another sep marker

    decoded =[]

    size_encoded = len(s)

    # the value before `#` will always be the SIZE of the word

    i=0
    while i < size_encoded:  # i will run all through my coded 

        print(f'We are on the element {s[i]}')
        print()

        j= s.find('#',i) # Which position is the separater # 

        word_length = int(s[i:j])

        print(f"we found a #, so we have the word_length as {word_length}")
        print()

        start = j+1 # Skipped 

        word = s[start:start+word_length]   

        print()

        print(f"So our word will be {word}")

        decoded.append(word)


        print(f"Now our decoded is : {decoded}")
        print()

        i = start+ word_length

        

        



test_encode = encode(test)
decode(test_encode)