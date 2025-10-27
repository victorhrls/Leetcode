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



#string = 'bolo'

#print(string)


#sorted = ''.join(sorted(string))

#print(sorted)

#print()





def is_anagram(list_of_words):
    # Keep the words already used
    # Control of items already used

    out = set()
    group_anagram = []

    for ch in list_of_words:
        #Verify if the words was used already
        if ch in out:
            continue

        word_of_test = ''.join(sorted(ch))
        check = []

        for candidate in list_of_words:
            
            sort = ''.join(sorted(candidate))

            if word_of_test == sort:
                check.append(candidate)

        out.update(check)
        group_anagram.append(check)


        # Now i have a list of words that entered , so i will pop them 
    
    return group_anagram



out= is_anagram(strs)

print(out)

                
        

