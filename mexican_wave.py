# Task
# In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 
# Rules
#  1.  The input string will always be lower case but maybe empty.

#  2.  If the character in the string is whitespace then pass over it as if it was an empty seat

# Example
# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

def wave(people):
    arr = []
    word = list(people)
    for i in range(len(people)):
        if(word[i] == ' '):
            word[i-1] = word[i-1].lower()
            continue 
        else: 
            word[i] = word[i].upper()
            if i > 0:
                word[i-1] = word[i-1].lower()
                    
        arr.append(''.join(word))
        
    return arr


print(wave('hello hola'))