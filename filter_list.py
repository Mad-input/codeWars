def filter_list(l):
     # Use list comprehension to filter out strings
    return [x for x in l if not isinstance(x, str)]


print(filter_list(['1',1,'a','b',True]))