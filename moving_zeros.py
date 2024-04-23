def move_zeros(lst):
    newNums = ''.join(list(lst))
    for a in lst:
        if a < 1:
            print(a)
    return list(newNums)


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
            
