import re

def clean_tweet(text):
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = text.lower()
    text_split = text.split()

    for t in text_split:
        if ("@" in t or "https:" in t):
            text = text.replace(t, "")

    pat = r'[^a-zA-z0-9.,!?/:;\"\'\s]' 

    return " ".join(re.sub(pat, '', text).split())

        
