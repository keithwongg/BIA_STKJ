import json 
import pandas as pd
from pandas.io.json import json_normalize

def queen_json_pandas_converter(file):
    with open(file) as train_file:
        dict_train = json.load(train_file)

    # convert json to dataframe
    train = pd.DataFrame.from_dict(dict_train, orient='columns')
    train.reset_index(level=0, inplace=True)
    train.set_index('index', inplace=True)

    return train

# # Option 1 to pretty print
# print(train.to_string())
# # Option 2 to pretty print 
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(df)