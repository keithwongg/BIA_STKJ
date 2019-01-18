import queen_converter as queen
from text_processing import basic_preprocessing
import json
import csv 
# Dark souls 3 id : 374320
# No man's sky id : 275850

df = queen.queen_json_pandas_converter('374320_2k.json') # converting json to dataframe
toclean = list(df['Comments']) # convert to a [[words]] (list in a list)
print('can select')
cleaned = basic_preprocessing(toclean) # pre-processing using silvester's function
print(cleaned.to_string())
df['Comments'] = cleaned
print(df.to_string())
df.dropna(how='any', inplace=True)

output = df.to_csv(encoding='utf-8') # write out to csv file
print(output)
with open('cleaned_374320_2k.csv', 'w') as f:
	f.write(output)



df = queen.queen_json_pandas_converter('275850_2k.json') # converting json to dataframe
toclean = list(df['Comments']) # convert to a [[words]] (list in a list)
print('can select')
cleaned = basic_preprocessing(toclean) # pre-processing using silvester's function
print(cleaned.to_string())
df['Comments'] = cleaned
print(df.to_string())
df.dropna(how='any', inplace=True)

output = df.to_csv(encoding='utf-8') # write out to csv file
print(output)
with open('cleaned_275850_2k.csv', 'w') as f:
	f.write(output)