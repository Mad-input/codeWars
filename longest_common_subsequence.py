"""
Write a function called LCS that accepts two sequences and returns the longest subsequence common to the passed in sequences.

Subsequence
A subsequence is different from a substring. The terms of a subsequence need not be consecutive terms of the original sequence.

Example subsequence
Subsequences of "abc" = "a", "b", "c", "ab", "ac", "bc" and "abc".

LCS examples
lcs( "abcdef" , "abc" ) => returns "abc"
lcs( "abcdef" , "acf" ) => returns "acf"
lcs( "132535365" , "123456789" ) => returns "12356"
"""

def lcs(x, y):
    print(list(y),set(x))
    return ''.join([s1 for s1 in y for s2 in set(x) if s1 == s2])

print(lcs("anothertest", "notatest")) ### Return (ac)