def analyzeSMSes(inputFilename):
    #allowedCharacterList is all letters and numbers, which are the only characters allowed
    allowedCharacterList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    spamWordCounts = {}
    hamWordCounts = {}
    SMSTextList = getSMSList(inputFilename)
    hamTextList = []
    spamTextList = []

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

    #separate ham and spam texts into different lists
    for message in SMSTextList:
        if message[0] == 'spam':
            spamTextList.append(message)
        else:
            hamTextList.append(message)
    
    totalSpamWords = sum(spamWordCounts.values())
    totalHamWords = sum(hamWordCounts.values())
    #print top 10 frequent spam words
    spamTuples = sorted(spamWordCounts.items(), key = lambda item: item[1],reverse = True)
    hamTuples = sorted(hamWordCounts.items(), key = lambda item: item[1],reverse = True)
    spamTableFormat = []
    hamTableFormat = []
    spamFrequency = []
    hamFrequency = []
    spamMessageFrequency = []
    hamMessageFrequency = []
    print("SPAM Words:\nWord: the word associated with the stats\nWord Count: amount of times that word occurs in total throughout the text messages inputted\nWord Frequency: the percentage of how often the word occurs\nMessage Frequency: the percentage of how many messages contain this word\n")
    #populate spam frequency list in order of sorted list
    for item in spamTuples:
        spamFrequency.append('{n:.{d}f}'.format(n=(item[1]/totalSpamWords),d = 4))
    #populate spam message frequency list in order of sorted list
    for wordCount in spamTuples:
        totalMessages = 0
        totalMessagesContainingWord = 0
        for line in spamTextList:
            if wordCount[0] in line:
                totalMessagesContainingWord += 1
            totalMessages += 1
        spamMessageFrequency.append('{n:.{d}f}'.format(n=(totalMessagesContainingWord/totalMessages),d = 4))
    for index in range(len(spamTuples)):
        spamTableFormat.append((spamTuples[index][0],spamTuples[index][1],spamFrequency[index],spamMessageFrequency[index]))
    template = "| {0:6} | {1:10} | {2:14} | {3:17} |"
    printTable(template,spamTableFormat)

    print("\nHAM Words:\nWord: the word associated with the stats\nWord Count: amount of times that word occurs in total throughout the text messages inputted\nWord Frequency: the percentage of how often the word occurs\nMessage Frequency: the percentage of how many messages contain this word\n") 
    #populate ham frequency list in order of sorted list
    for item in hamTuples:
        hamFrequency.append('{n:.{d}f}'.format(n=(item[1]/totalHamWords),d = 4))
    #populate message ham frequency list in order of sorted list
    for wordCount in hamTuples:
        totalMessages = 0
        totalMessagesContainingWord = 0
        for line in hamTextList:
            if wordCount[0] in line:
                totalMessagesContainingWord += 1
            totalMessages += 1
        hamMessageFrequency.append('{n:.{d}f}'.format(n=(totalMessagesContainingWord/totalMessages),d = 4))
    for index in range(len(spamTuples)):
        hamTableFormat.append((hamTuples[index][0],hamTuples[index][1],hamFrequency[index],hamMessageFrequency[index]))
    printTable(template,hamTableFormat)

    print("\nHAM Words (containing more than 3 characters):\n")
    hamTuplesMoreThan3Letters = [item for item in hamTableFormat if len(item[0]) > 3]
    printTable(template,hamTuplesMoreThan3Letters)

    print("\nSPAM Words (containing more than 3 characters):\n")
    spamTuplesMoreThan3Letters = [item for item in spamTableFormat if len(item[0]) > 3]
    printTable(template,spamTuplesMoreThan3Letters)

    #sortedTuplesGreater3 = sorted(hamTuplesMoreThan3Letters,key = lambda item: item[1], reverse = True)
    #print(sortedTuplesGreater3[:10])
    #print(hamTuples[:10])
    #sortedHamTuples = sorted(hamTuples, key = lambda item: item[1],reverse = True)
    #print(sortedHamTuples[:10])
    #sortedHamWordCounts = sorted(hamWordCounts, 
    #print(sortedHamWordCounts,spamWordCounts)
    #print(SMSTextList[:10])

#prints a table from the tuples passed in in table format
def printTable(template,tuples):
    print("------------------------------------------------------------")
    print (template.format("WORD", "WORD COUNT","WORD FREQUENCY","MESSAGE FREQUENCY"))
    print("============================================================")
    for rec in tuples[:10]: 
        print (template.format(*rec))
        print("------------------------------------------------------------")


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

