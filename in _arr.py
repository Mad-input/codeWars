"""
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

Example 1:
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

"""

def in_array(array1, array2):
    r = set()
    for i in array2:
        for j in array1:
            if j in i:
                r.add(j) 
            
    return sorted(r)

print(in_array(["tarp", "mice", "bull"],["lively", "alive", "harp", "sharp", "armstrong"]))