import time
import instagram
from instagram import Account, Media, WebAgent, Story, Location, Tag, Comment

agent = WebAgent()
account = Account("acc")

posts = agent.get_media(account, pointer=None, count=5)
res = list(list(posts)[0])
i = 0 #counts of posts
likes = []
likes_prev = []
comments = []
comments_prev = []
import requests
while True:
	media = Media(res[i])
	likes.append(media.likes_count)
	comments.append(media.comments_count)
	i += 1
	
	if i == len(res):
		likes_prev = likes
		likes = []
		comments_prev = comments
		comments = []
		time.sleep(3)	
		try:
			for i in range(len(res)):
				media = Media(res[i])
				agent.update(media)
				likes.append(media.likes_count)
				comments.append(media.comments_count)

				if likes_prev[i] < likes[i] or comments_prev[i] < comments[i]:
						print("Beats")

			likes = []
			likes_prev = []
			comments = []
			comments_prev = []
			i = 0

		except requests.HTTPError:
			time.sleep(10)



			


