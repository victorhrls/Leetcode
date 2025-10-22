"""
LeetCode - Group Anagrams
Difficulty: Medium
https://leetcode.com/problems/group-anagrams/description/

Problem:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Approach:
"""

# strs = [""]



strs = ["eat","tea","tan","ate","nat","bat"]


for ch in strs:
    print(ch)
    print(type(ch))

    print()
    sort = ''.join(sorted(ch))
    print(sort)
    print()


print()


def is_anagram(list_of_words):

    # sort everything out 

    out =[]

    for ch in list_of_words:
        element_1 = list_of_words[ch]
        sort_1 = ''.join(sorted(list_of_words[ch]))

        print(sort_1)


        #element = []

        #element.append(element_1)
        '''
        for j in range(i+1,list_of_words):
            element_2 = list_of_words[i+1]

            sort_2 = ''.join(sorted(list_of_words[i+1]))

            if sort_1 == sort_2 :  element.append(element_2)
            else: continue
        out.append(element)
         '''

    
    #return element
        

#is_anagram(strs)


# Check if word 1 and word 2 are equal 

