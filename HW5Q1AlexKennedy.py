def analyzeSMSes(inputFilename):
    #allowedCharacterList is all letters and numbers, which are the only characters allowed
    allowedCharacterList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    spamWordCounts = {}
    hamWordCounts = {}
    SMSTextList = getSMSList(inputFilename)

    for index in range(len(SMSTextList)):
        SMSTextList[index] = SMSTextList[index].split()
    SMSTextList = removeUnwantedCharacters(SMSTextList,allowedCharacterList)
    for message in SMSTextList:
        if message[0] == 'ham':
            for word in message[1:]:
                if word != '':
                    hamWordCounts[word] = hamWordCounts.get(word,0) + 1
        else:
            for word in message[1:]:
                if word != '':
                    spamWordCounts[word] = spamWordCounts.get(word,0) + 1
                    
    #print top 10 frequent spam words
    spamTuples = list(zip(spamWordCounts.keys(), spamWordCounts.values()))
    sortedSpamTuples = sorted(spamTuples, key = lambda item: item[1],reverse = True)
    print("The 10 most common words in the spam messages (any number of characters) are:")
    for wordNumber in range(10):
        print((wordNumber + 1),".)",sep = '', end = ' ')
        print(sortedSpamTuples[wordNumber][0]," - ",sortedSpamTuples[wordNumber][1],sep='')

    print()
    totalSpamWords = sum(spamWordCounts.values())
    totalHamWords = sum(hamWordCounts.values())
    #print top 10 frequent ham words
    hamTuples = list(zip(hamWordCounts.keys(), hamWordCounts.values()))
    sortedHamTuples = sorted(hamTuples, key = lambda item: item[1],reverse = True)
    print("The 10 most common words in the ham messages (any number of characters) are:")
    for wordNumber in range(10):
        ham = sortedHamTuples[wordNumber]
        hamFrequency = '{n:.{d}f}'.format(n=(ham[1] / totalHamWords),d = 4)
        print((wordNumber + 1),".)",sep = '', end = ' ')
        print(ham[0]," - ",ham[1]," Word Frequency: ",hamFrequency,sep='')

    #print the top 10 information about words in a pretty table format
    template = "{0:6}|{1:10}|{2:14}"
    print (template.format("WORD", "WORD COUNT","WORD FREQUENCY"))
    print("================================")
    for rec in sortedHamTuples[:10]: 
        print (template.format(*rec))
        print("--------------------------------")
    #hamTuplesMoreThan3Letters = [item for item in hamTuples if len(item[0]) > 5]
    #sortedTuplesGreater3 = sorted(hamTuplesMoreThan3Letters,key = lambda item: item[1], reverse = True)
    #print(sortedTuplesGreater3[:10])
    #print(hamTuples[:10])
    #sortedHamTuples = sorted(hamTuples, key = lambda item: item[1],reverse = True)
    #print(sortedHamTuples[:10])
    #sortedHamWordCounts = sorted(hamWordCounts, 
    #print(sortedHamWordCounts,spamWordCounts)
    #print(SMSTextList[:10])

#makes a list of the SMS messages, each member of the list is a message.
def getSMSList(filename):
    SMSTextList = []
    with open(filename,encoding = 'utf-8') as SMSSpamCollection:
        for line in SMSSpamCollection:
            line = line.lower()
            SMSTextList.append(line)
    return SMSTextList

#removes all characters except for the ones from the allowed character list
def removeUnwantedCharacters(textList,allowedCharacters):
    newTextList = list(textList)
    for messageIndex in range(len(newTextList)):
        for wordIndex in range(len(newTextList[messageIndex])):                              
            wordAsList = list(newTextList[messageIndex][wordIndex])
            newWord = ''
            for char in wordAsList:
                if char in allowedCharacters:
                    newWord += char
            newTextList[messageIndex][wordIndex] = ''.join(newWord)
    return newTextList

