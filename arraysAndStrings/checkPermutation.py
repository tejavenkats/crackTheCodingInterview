'''
Q. Check whether a string is a permutation of other or not.

My initial approach was to create 2 hashmaps to store the character count in
each string and compare them later. If at any time the count didn't match,
return and exit. Also if the string lengths are different return and exit.

There's another way of solving but this is inefficient. We sort both the
strings and compare them if they are equal, return true else false. I think
this is inefficient because of sorting as it takes O(nlogn) time + the O(n)
time for check the equality of strings.
 '''



def makeHashmap(str,hashmap):
    for i in str:
        if(i in hashmap):
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    return hashmap
def checkPermutation(str1, str2):
    if(len(str1) != len(str2)):
        print("string 1 is not a permutation of string 2");
        return
    str2Hashmap = dict()
    str1Hashmap = dict()
    str1Hashmap = makeHashmap(str1, str1Hashmap)
    str2Hashmap = makeHashmap(str2, str2Hashmap)
    for i in str1:
        if(str1Hashmap[i] != str2Hashmap[i]):
            print("string 1 is not a permutation of string 2")
            return
    print("string 1 is a permutation of string 2")

checkPermutation("bcda","abcd")
    
