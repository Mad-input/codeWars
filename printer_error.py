def printer_error(s):
    err = 0
    for char in s:
        if char not in 'abcdefghijklm' or not char.isalnum():
            err +=1
    return f'{err}/{len(s)}'