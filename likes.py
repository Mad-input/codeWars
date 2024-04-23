def likes(names):
    frase = ''
    lenNames = len(names)
    if lenNames == 0:
        frase = 'no one likes this'
    elif lenNames == 1:
        frase = f'{names[0]} likes this'
    elif lenNames == 2:
        frase = f'{names[0]} and {names[1]} like this'
    elif lenNames == 3:
        frase = f'{names[0]}, {names[1]} and {names[2]} like this'
    elif lenNames >= 4:
        frase = f'{names[0]}, {names[1]} and {lenNames - 2} others like this'
        
    return frase
            
        
        
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))