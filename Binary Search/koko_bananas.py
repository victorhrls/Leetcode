"""
LeetCode  - Koko Eating Bananas
Difficulty: Medium
https://leetcode.com/problems/koko-eating-bananas/description/

Problem:
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
Approach:

"""


def Koko(piles,hours):
    bananas = piles.copy() # do not mess with piles
    bananas.sort() # increasing number , test the smaller and increase

    # run in h hours 
    least = bananas[0] #first value
    size = len(bananas)

    times = 0

    for i in range(hours):
        print("We are dealing with the element",bananas[i])

        while bananas[i] != 0 or times <hours:
            times +=1

            if bananas[i] < least :
                print("we know that", least, " is bigger than" ,bananas[i], "So i will zero this")
                bananas[i] = 0
                continue
            else:
                print("we are subtracting the bananas by \n")
                print("First we had",bananas[i])
                print()
                print("The result will be:", bananas[i], " - ", least)
                bananas[i] -= least

                print()
                print("Thus , our new bananas will be: ", bananas[i])
        
    return times
        

print()
piles = [3,6,7,11]
h =8

print(Koko(piles,h))



