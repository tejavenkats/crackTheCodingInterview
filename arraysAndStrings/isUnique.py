''' 
Q. Check whether the string contains all unique characters or not. 
Can't use any additional data structures.

The initial approach is to check each char and push it into a hashmap or 
dictionary if it is not present already and set its count to one. If
it is already present then return and print false. 
'''

def checkIsUnique(inputString):
    hashmap =  dict()
    for i in inputString:
        if i in hashmap:
            hashmap[i] += 1
            print("The string is not unique")
            print(hashmap)
            return
        else:
            hashmap[i] = 1
    print("The string is unique")
    print(hashmap)
checkIsUnique("abcdghtiqkolvmnw")