# In Bali, as far as I can gather, when ex-pats speak to locals, they basically insert the word 'Pak' as often as possible. I am assured it means something like 'mate' or 'sir' but that could be completely wrong.

# Anyway, as some basic language education(??) this kata requires you to turn any sentence provided (s) into ex-pat balinese waffle by inserting the word 'pak' between every other word. Simple 8kyu :D

# Pak should not be the first or last word. Strings of just spaces should return an empty string.

def pak(s):
    list_s = s.split(' ')
    new_s = list()
    for word in list_s:
        new_s.append(f'{word} pak')
        
    new_words = ' '.join(new_s).split(' ')
    
    return ' '.join(new_words)[:-4]

print(pak("Man I need a taxi up to Ubud"))
    