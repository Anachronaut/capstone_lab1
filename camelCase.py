def camelCase():
    txt = input("Enter a string to be converted to camel case: ")
    txtsplit = txt.split() #split string into characters
    txtlist = [word for word in txtsplit] #put split text in list as complete words

    firstWord = txtlist[0].lower() #sets first word in list as lower case
    txtlist.pop(0) #removes first word from list

    lowerlist = [word.lower() for word in txtlist] #converts all remaining words in list to lower case
    caplist = [word.capitalize() for word in lowerlist] #capitalizes the first letter of all remaining words
    camelString = firstWord + ''.join(caplist) #joins lower case first word with correctly formatted remaining words into camel case
    print(camelString)

camelCase()
