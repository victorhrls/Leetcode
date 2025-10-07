
# tamanho 7
lista = [9,8,7,6,4,3,1]
# 7 // 2 = 3 

lista.sort()



def binary_search (list,objective):
    found = False
    size = len(list)

    position = size//2
    midterm = list[position] # this is the value , not the position

    if midterm == objective:
        return position
    else:
        if midterm < objective: # go right
            return binary_search(list[position+1:],objective)
        else:                   # go left
            return binary_search(list[:position],objective)



    return position
    



