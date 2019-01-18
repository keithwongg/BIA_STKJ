def basic_preprocessing(words):
    #importing libraries
    import pandas as pd
    import numpy as np
    from nltk.corpus import stopwords
    from textblob import TextBlob
    from textblob import Word
    
    #saving as DataFrame, and renaming column to 'words'
    df = pd.DataFrame(words)
    df.columns=['words']
    
    #changing all words to lower case
    df['words'] = df['words'].apply(lambda x: " ".join(x.lower() for x in x.split()))
    
    #removing punctuation
    df['words'] = df['words'].str.replace('[^\w\s]','')
    
    #removal of stopwords
    stop = stopwords.words('english')
    df['words'] = df['words'].apply(lambda x: ' '.join(x for x in x.split() if x not in stop))
    
    #common word removal (top 10 most frequently occuring words)
    freq = pd.Series(' '.join(df['words']).split()).value_counts()[:10]
    freq = list(freq.index)
    df['words'] = df['words'].apply(lambda x: ' '.join(x for x in x.split() if x not in freq))
    
    #rare word removal (bottom 10 most frequently occuring words)
    freq = pd.Series(' '.join(df['words']).split()).value_counts()[-10:]
    freq = list(freq.index)
    df['words'] = df['words'].apply(lambda x: ' '.join(x for x in x.split() if x not in freq))
    
    #spelling correction    
    df['words'] = df['words'].apply(lambda x: str(TextBlob(x).correct())) # take quite long 
    
    #lemmatization
    #preferred over stemming as it converts words into root words rather than just removing suffices
    df['words'] = df['words'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
    
    return df
    