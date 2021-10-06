import re

def clean_tweet(text):
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = text.lower()
    text_split = text.split()
    remove = [] #remove from string

    def getChain(index, data)-> list():
        if (index == len(text_split)-1):
            if("#" in text_split[index]):
                data.append(index)
        elif (index >= len(text_split)):
            print("Cleaning......Invalid index")
        elif("#" not in text_split[index]):
            print("Cleaning.....Chain ended")
        else: 
            data.append(index)
            getChain(index+1, data)

        return data 

    for i in range(len(text_split)):
        if ("#" in text_split[i] and i not in remove):
            data = getChain(i+1, [])
            if (len(data) != 0):
                data.append(i)
                remove += data
                data = []
        if ("@" in text_split[i] or "https:" in text_split[i]):
            text_split[i] = text_split[i].replace(text_split[i], " ")


    for index in remove:
        text_split[index] = text_split[index].replace(text_split[index], " ")

    cleaned = " ".join(text_split)
    pat = r'[^a-zA-z0-9.,!?/:;\"\'\s]' 

    return " ".join(re.sub(pat, '', cleaned).split())







        
