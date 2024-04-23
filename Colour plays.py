# Colour plays an important role in our lifes. Most of us like this colour better then another. User experience specialists believe that certain colours have certain psychological meanings for us.

# You are given a 2D array, composed of a colour and its 'common' association in each array element. The function you will write needs to return the colour as 'key' and association as its 'value'.

# For example:

# var array = [["white", "goodness"], ...] returns [{'white': 'goodness'}, ...]


def colour_association(arr):
    arr2 = list()
    
    for data in arr:
        arr2.append({data[0]: data[1]})
    return arr2

print(colour_association([["white", "goodness"], ["blue", "tranquility"]]))