# Write a simple parser that will parse and run Deadfish.

# Deadfish has 4 commands, each 1 character long:

# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.

def parse(data):
    res = 0
    arr = []
    for char in list(data):
        if char in 'idso':
            if char == 'i':
                res += 1
            elif char == 'd':
                res -= 1
            elif char == 's':
                res = res**2
            elif char == 'o':
                arr.append(res)
        else: continue
        
    return arr

print(parse("ioioio"))