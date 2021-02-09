# A string is a valid parentheses string (denoted VPS) if it meets one of the following:

# It is an empty string "", or a single character not equal to "(" or ")",
# It can be written as AB (A concatenated with B), where A and B are VPS's, or
# It can be written as (A), where A is a VPS.
# We can similarly define the nesting depth depth(S) of any VPS S as follows:

# depth("") = 0
# depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
# depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
# depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
# For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

# Given a VPS represented as string s, return the nesting depth of s.

def validpar(s):
    
    s=[ch for ch in s]
    
    countleft=0
    countright=0
    dict1={}
    doc=str
    valu=[]
    for par in s:
        if par=="(":
            countleft=countleft+1
        if par==")":
            countright=countright+1

        doc=countleft-countright
        dict1[par]=doc
    for val in dict1.values():
        valu.append(val)
    return max(valu)
    
print(validpar("1"))

