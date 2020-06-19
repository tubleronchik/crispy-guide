import time
import instagram
import requests
import re
from instagram import Account, Media, WebAgent, Story, Location, Tag, Comment

agent = WebAgent()
account = Account("who")

	

posts = agent.get_media(account, pointer=None, count=5)
res = list(list(posts)[0])
i = 0 #counts of posts
likes = []
likes_prev = []
comments = []
comments_prev = []
tags = []
tags_prev = []
foll = []
foll_prev = []

def tag(url):
	begin = "count"
	end = "page_info"
	request = (requests.get(url)).text
	beg_ind = request.find(begin)+len(begin)
	end_ind = request.find(end)
	count = request[beg_ind:end_ind]
	return (int((re.search('\d+', count)).group()))	

url_tag = 'https://www.instagram.com/explore/tags/home/?__a=1' #link for hashtag

def followers(url):
	begin = "count"
	end = "followed_by_viewer"
	request = (requests.get(url)).text
	beg_ind = request.find(begin)+len(begin)
	end_ind = request.find(end)
	count = request[beg_ind:end_ind]
	return (int((re.search('\d+', count)).group()))


url_followers = 'https://www.instagram.com/who/?__a=1' #link for account

while True:
	media = Media(res[i])
	likes.append(media.likes_count)
	comments.append(media.comments_count)
	i += 1
	tags.append(tag(url_tag))
	foll.append(followers(url_followers))
	if i == len(res):
		likes_prev = likes
		likes = []
		comments_prev = comments
		comments = []
		tags_prev = tags
		tags = []
		foll_prev = foll
		foll = []
		time.sleep(3)	
		try:
			for i in range(len(res)):
				media = Media(res[i])
				agent.update(media)
				likes.append(media.likes_count)
				comments.append(media.comments_count)
				tags.append(tag(url_tag))
				foll.append(followers(url_followers))
				if likes_prev[i] < likes[i] or comments_prev[i] < comments[i] or tags_prev[i] < tags[i] or foll_prev[i] < foll[i]:
						print("Beats")

			likes = []
			likes_prev = []
			comments = []
			comments_prev = []
			tags_prev = []
			tags = []
			foll_prev = []
			foll = []
			i = 0

		except requests.HTTPError:
			time.sleep(10)
			agent.update(media)



			


