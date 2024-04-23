def disemvowel(string):
    for a in string:
        if a in 'aeiouAEIOU':
           string = string.replace(a,'')
    return string