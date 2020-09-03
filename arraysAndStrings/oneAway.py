def replaceOne(str1, str2):
    replaced = False
    for i in range(len(str1)):
        if(str1[i] != str2[i]):
            if(replaced):
                return "Can't replace"
            replaced = True
    return "One replace away"


def insertOne(str1, l1, str2, l2):
    index1 = 0
    index2 = 0
    while(index1 < l1 and index2 < l2):
        if(str1[index1] != str2[index2]):
            if(index1 != index2):
                return "Can't insert"
            index1 += 1
        else:
            index1 += 1
            index2 += 1
    return "One insert away"


def oneAway(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    if(l1 == l2):
        print(replaceOne(str1, str2))
    if(l1 > l2):
        print(insertOne(str1, l1, str2, l2))
    if(l2 > l1):
        print(insertOne(str2, l2, str1, l1))


oneAway("pale", "bale")
