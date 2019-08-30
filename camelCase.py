def camelCase():
    txt = input("Enter a string to be converted to camel case: ")
    txtsplit = txt.split()
    txtlist = [word for word in txtsplit]

    firstWord = txtlist[0].lower()
    txtlist.pop(0)

    lowerlist = [word.lower() for word in txtlist]
    caplist = [word.capitalize() for word in lowerlist]
    camelString = firstWord + ''.join(caplist)
    print(camelString)

camelCase()
