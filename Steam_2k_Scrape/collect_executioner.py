from king_extractor import steam_comments_king_extractor
import lxml.html
import requests

# Dark souls 3 id : 374320 # max 4137
# No man's sky id : 275850 # max >5000

steam_comments_king_extractor(374320, 200) # later remember to try this again 
steam_comments_king_extractor(275850, 200)