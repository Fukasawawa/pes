import ChangeName, re

def splitName(Name):
    xName = re.split('[ -]', Name)
    return xName

def omitName(xName):
    for i in range(len(xName)-1):
        xName[i] = xName[i][0]
    return xName

def unionName(xName):
    new_Name = xName[0]
    #if len(xName) <= 1:
    #    return new_Name
    for i in range(len(xName)-1):
        new_Name += ". " + xName[i+1]
    return new_Name


def main():
    english_name = ChangeName.main()
    xName = splitName(english_name)
    new_Name = unionName(omitName(xName))
    #print(new_Name)
    return new_Name

# main関数呼び出し
if __name__ == "__main__":
    main()
