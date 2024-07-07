# def fibonacci(l):
#     seq = [0,1]
   
#     for i in range(2, l+1):
#         seq.append(seq[i - 1] + seq[i - 2])
#     return seq

# print(fibonacci(10))

def fibonacci(n):
    if n == 0: return n
    if n == 1: return n
    return fibonacci(n -1 )+ fibonacci( n - 2)        
    
for i in range(0,11):
    print(fibonacci(i))
