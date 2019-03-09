def basic_preprocessing(df):
    #importing libraries
    import pandas as pd
    import numpy as np
    from nltk.corpus import stopwords
    #from textblob import TextBlob
    from textblob import Word
    import re
    #from spellchecker import SpellChecker
    
    #changing all words to lower case
    df['words'] = df['words'].apply(lambda x: " ".join(x.lower() for x in str(x).split()))
    
    #removal of URL
    df['words'] = df['words'].apply(lambda x: " ".join(re.sub(r"http\S+", "", x) for x in x.split()))
    
    #removing punctuation
    df['words'] = df['words'].str.replace('[^\w\s]','')
    
    #removal of stopwords
    stop = stopwords.words('english')
    df['words'] = df['words'].apply(lambda x: ' '.join(x for x in x.split() if x not in stop))
    
    #common word removal (top 10 most frequently occuring words)
    #freq = pd.Series(' '.join(df['words']).split()).value_counts()[:10]
    #freq = list(freq.index)
    #df['words'] = df['words'].apply(lambda x: ' '.join(x for x in x.split() if x not in freq))
    
    #rare word removal (bottom 10 most frequently occuring words)
    #freq = pd.Series(' '.join(df['words']).split()).value_counts()[-10:]
    #freq = list(freq.index)
    #df['words'] = df['words'].apply(lambda x: ' '.join(x for x in x.split() if x not in freq))
    
    #spelling correction
    #spell = SpellChecker()
    #df['words'] = df['words'].apply(lambda x: " ".join(spell.correction(x) for x in x.split()))
    
    #lemmatization
    #preferred over stemming as it converts words into root words rather than just removing suffices
    df['words'] = df['words'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
    
    return df['words']
    