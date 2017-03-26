list = [1,2,3,4,5,6]
def isDistinct(list):
    length = len(list)

    result = False
    for i in range(0,length):
        if result == False:
            for j in range(0,length):
                if (i!= j):
                    list[i] == list[j]
                    result = True
                else:
                    result = False

    if result == True:
        return False
    else:
        return True

print(isDistinct(list))