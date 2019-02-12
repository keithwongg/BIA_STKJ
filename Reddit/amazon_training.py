#importing dataset from amazon json file
from amazon_data_extract import getDF
df = getDF('reviews_Video_Games_5.json.gz')

#selecting relevant columns
df_1 = df[['helpful','reviewText','overall']]

#creating function to calculate helpful score
def score(x):
    if x[1]==0:
        return 0
    else:
        return x[0]/x[1]

#apply score function to iput calculated values of helpful score into new column "helpful_score"    
df_1['helpful_score'] = df_1['helpful'].apply(score)

#creating function to set target variable - setting threshold of at least 0.5 for helpful score
def threshold(x):
    if x >= 0.5:
        return 1
    else:
        return 0

#apply threshold function to input target variable into new column "is_helpful"
df_1['is_helpful'] = df_1['helpful_score'].apply(threshold)

#rename column reviewText to words
df_1.rename(columns={'reviewText':'words'},inplace=True)

#saving dataframe into CSV
df_1.to_csv('amazon_dataset.csv', index=False)

#############################################################################################
#run this part onwards
#import library
import pandas as pd

#remove warnings
import warnings
warnings.filterwarnings("ignore")

#importing from dataframe from csv file
df = pd.read_csv('amazon_dataset.csv')

#extracting subset of dataset to pilot functions
df_test = pd.concat([df[df['is_helpful']==1].sample(n=420),
                     df[df['is_helpful']==0].sample(n=580)])

#preprocess list of words
from text_processing import basic_preprocessing
df_test['cleaned_text'] = basic_preprocessing(df_test)

#############################################################################################
#tf-idf method
#count vectorizer
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=0, lowercase=False)

#creating X, y variable for machine learning
X = vectorizer.fit_transform(df_test['cleaned_text']).toarray()
y = df_test['is_helpful'].values

#converting to tf-idf values
from sklearn.feature_extraction.text import TfidfTransformer
tfidfconverter = TfidfTransformer()
X = tfidfconverter.fit_transform(X).toarray()

#############################################################################################
#model testing function for cross validation score
def choose_model(model, X, y):
    from sklearn import model_selection
    
    kfold = model_selection.KFold(n_splits=10, random_state=0)
    cv_results = model_selection.cross_val_score(model, X, y, cv=kfold, scoring='accuracy')
    print('This model has mean accuracy of',
          str(cv_results.mean()), 'and standard deviation of', str(cv_results.std()))
    
#gaussian Naive Bayes
from sklearn.naive_bayes import GaussianNB
classifier_NB = GaussianNB()
choose_model(classifier_NB, X, y)

#random forest classifier
from sklearn.ensemble import RandomForestClassifier
classifier_RF = RandomForestClassifier()
choose_model(classifier_RF, X, y)

#logistic regression
from sklearn.linear_model import LogisticRegression
classifier_LR = LogisticRegression()
choose_model(classifier_LR, X, y)





