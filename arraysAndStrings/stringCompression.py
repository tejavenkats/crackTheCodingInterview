def stringCompression(inputString):
    ansStringList = list()
    inputString = inputString.lower()
    streak = 0
    prevChar = inputString[0]
    for i in range(len(inputString)):
        if(prevChar != inputString[i]):
            ansStringList.append(prevChar)
            if(len(ansStringList) == 1):
                ansStringList.append(str(streak))
            if(len(ansStringList) > 2):
                ansStringList.append(str(streak + 1))
            streak = 0
            prevChar = inputString[i]
            continue
        streak += 1
        prevChar = inputString[i]
    ansStringList.append(prevChar)
    ansStringList.append(str(streak+1))
    if(len(ansStringList) > len(inputString)):
        return inputString

    return "".join(ansStringList)


print(stringCompression("aab"))
