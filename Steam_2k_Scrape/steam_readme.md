# Steam Scraping Readme

## Collection (Web Scraping)
Open the file collect_executioner.py to change desired Game IDs and number of reviews that you would like to scrape. This script uses the web-scraping function coded in king_extractor.py. Data collected is stored in json format. 


## Cleaning (Pre-Processing)
Open the file clean_executioner.py to clean comments collected. This script uses the text pre-processing function coded in text_processing.py after converting the .json file to pandas DataFrame using the function coded in queen_converter.py. The cleaned data is then exported into a csv file.


## Data
### Initial Phase 
For now, the 2 games that we are focusing on is Dark Souls 3 and No Man's Sky.
Steam Game IDs:
Dark Souls 3 - 374320
No Man's Sky - 275850
The collect_executioner.py script was set to scrape for 200 pages (10 comments per page), thus 2000 comments for each game. This is expected to increase once we have the initial ML model done.
The cleaned data is as shown in the cleaned_374320_2k.csv and cleaned_275850_2k.csv files. 
