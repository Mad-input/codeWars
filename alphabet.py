def alphabet_position(text):
    newStr = text.replace('[\W]gi', '')
    print(newStr)
    
alphabet_position('The sunset sets at twelve o clock.')