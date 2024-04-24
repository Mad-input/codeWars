# Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5
# For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

# Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

# For example, decode("h3 th2r2") would return "hi there".

# For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.


def encode(st):
    vocals = {
        'a': 1,
        'e': 2,
        'i': 3,
        'o': 4,
        'u': 5
    }
    new_st = ''
    for c in st:
        if c in vocals:
            new_st += str(vocals[c])
        else: new_st += c
    return new_st

print(encode('How are you today?'))
            
        
    
def decode(st):
    vocals = {
        '1': 'a',
        '2': 'e',
        '3': 'i',
        '4': 'o',
        '5': 'u'
    }
    new_st = ''
    for c in st:
        if c in vocals:
            new_st += str(vocals[c])
        else: new_st += c
    return new_st

print(decode(encode('How are you today?')))