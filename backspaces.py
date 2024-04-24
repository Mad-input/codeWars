# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

# Your task is to process a string with "#" symbols.

# Examples
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""

def clean_string(s):
    new_sr = []
    
    for c in s:
        if c == '#':
            if len(new_sr) < 1:
                continue
            else: new_sr.pop()
        else: 
            new_sr.append(c)    
    return '' if len(new_sr) == 0 else ''.join(new_sr)

print(clean_string('abc#d##c')) 


