import requests 
import lxml.html
import json 
from lxml import etree
from pprint import pprint 
# must put text processing file together with this file
from text_processing import basic_preprocessing


def steam_comments_king_extractor(code_id, pages):

	thumb_list = []
	hours_list = []
	comments_list = []

	for x in range(2, pages):
		try:
			html = requests.get("http://steamcommunity.com/app/{}/homecontent/?userreviewsoffset={}0&p={}&workshopitemspage={}&readytouseitemspage={}&mtxitemspage={}&itemspage={}&screenshotspage={}&videospage={}&artpage={}&allguidepage={}&webguidepage={}&integratedguidepage={}&discussionspage={}&numperpage=10&browsefilter=toprated&browsefilter=toprated&appid=374320&appHubSubSection=10&appHubSubSection=10&l=english&filterLanguage=default&searchText=&forceanon=1".format(code_id,x-1,x,x,x,x,x,x,x,x,x,x,x,x), verify=True)
			docs = lxml.html.fromstring(html.content)
			## Number of Products in user's account
			cards = docs.xpath('.//div[@class="apphub_UserReviewCardContent"]')
			for card in cards:
				review_info = card.xpath('.//div[@class="reviewInfo"]')
				for info in review_info:
					# Recommended
					
					thumb = info.xpath('.//div[@class="title"]/text()')
					if thumb[0] == 'Recommended':
						thumb = 1
					else:
						thumb = 0
					thumb_list.append(thumb)
					# Hours Played
					hours = info.xpath('.//div[@class="hours"]/text()')
					hours = hours[0].split(' ')
					hours = hours[0]
					if ',' in hours:
						hours = hours.replace(',', '')
					hours_list.append(float(hours))
				# Comments
				comments = card.xpath('.//div[@class="apphub_CardTextContent"]')
				comments = [[i.text_content().translate(str.maketrans("\n\t\r\"", "    ")).strip()] for i in comments]
				for com in comments:
					for c in com:
						if '\\[T]/' in c:
							comments = c.replace('\\[T]/', '')
						else:
							comments = c
				comments_list.append(comments)
				print('No: {} completed'.format(x))

		except lxml.etree.ParserError:
			print('max level reached')
			continue

	output = []
	for item in zip(thumb_list, hours_list, comments_list):
	    resp = {}
	    resp['Recommended'] = item[0]
	    resp['Hours_Played'] = item[1]
	    resp['Comments'] = item[2]
	    output.append(resp)
	print('Parse successful')

	with open('{}.json'.format(code_id), 'w') as json_file:
	    json.dump(output, json_file, sort_keys=False, indent=4, ensure_ascii=False)
	
	print('Json File Created')
