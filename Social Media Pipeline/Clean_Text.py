import re

#TODO: SEPERATE SENTENCES INTO AN ARRAY. DO SENTIMENT OF EACH SENTENCE THEN AVERAGE THE SCORE AND DETERMINE THE SENTIMENT 

def clean_tweet(text):
    #Take out emojis 
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = text.lower()
    text_split = text.split()

    for t in text_split:
        if ("@" in t or "https:" in t):
            text = text.replace(t, "")

    #take out special char
    pat = r'[^a-zA-z0-9.,!?/:;\"\'\s]' 

    return " ".join(re.sub(pat, '', text).split())

        
