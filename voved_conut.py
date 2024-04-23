def get_count(sentence):
    vocals = 'aeiouAEIOU'
    
    return sum(x in vocals for x in sentence)

print(get_count('Hola como estas')) ## 6