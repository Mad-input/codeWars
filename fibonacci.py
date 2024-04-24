def fibonacci(l):
    seq = [0,1]
   
    for i in range(2, l+1):
        seq.append(seq[i - 1] + seq[i - 2])
    return seq

print(fibonacci(10))