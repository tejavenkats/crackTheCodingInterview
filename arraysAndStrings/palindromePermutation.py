'''
Q. Check if the given string is a permutation of a palindrome

My approach was to create a hashmap of the string after removing any spaces.
If it is an even length palindrome, every character has to occur even number
of times, for odd length palindrome, only one character must occur odd number
of time and all other even number of times. So I implemented the same below.

I could have reduced the number of look ups in the hash table by removing 
duplicates using a set. But I don't know it yet and I thought this will do. I 
might implement and update this later with the implementation of a set for 
lesser lookups giving a lesser real runtime.
'''


def makeHashmap(str, hashmap):
    for i in str:
        if(i in hashmap):
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    return hashmap


def palindromePermutation(str):
    str = str.replace(" ", "")
    strhashmap = dict()
    strhashmap = makeHashmap(str, strhashmap)
    if(len(str) % 2 == 0):
        for i in str:
            if(strhashmap[i] % 2 != 0):
                return "It is not a permutation"
        return "It is a permutation"
    if(len(str) % 2 != 0):
        count = False
        for i in str:
            if(strhashmap[i] % 2 == 1 and not count):
                count = True
                strhashmap[i] = 0
        if(not count):
            return "It is not a permutation"
        for i in str:
            if(strhashmap[i] % 2 != 0 and count):
                return "It is not a permutation"
        return "It is a permutation"


print(palindromePermutation("lahdaddfdqdtltdqaha"))
