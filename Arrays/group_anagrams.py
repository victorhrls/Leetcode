"""
LeetCode - Group Anagrams
Difficulty: Medium
https://leetcode.com/problems/group-anagrams/description/

Problem:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Approach:
"""


# I can solve it with key , without needing to check every pair (brutal force)

# strs = [""]



strs = ["eat","tea","tan","ate","nat","bat"]



string = 'bolo'

print(string)


sorted = ''.join(sorted(string))

print(sorted)

print()

def is_anagram(list_of_words):


    # sort everything out 

    out =[]

    for ch in list_of_words:


        check = []

        

        word_of_test = ''.join(sorted(ch))

        check.append(ch)

        #print(word_of_test)

        print(f'A palavra eh {ch} ,ela sorted eh {word_of_test} ')
        # Check 2 by 2 if there is any anagram
        # If it is anagram, add to the list

        print()


        for candidate in list_of_words:

            if candidate!= word_of_test: # skip first element
                sort = ''.join(sorted(candidate))

                print(word_of_test, candidate, sort)


                if word_of_test == sort:
                    check.append(candidate)
                else:
                    continue
        
        print(check)

        print()

        out.append(check)

        print(out)


                
        

is_anagram(strs)