import time
from instagram import Account, Media, WebAgent, Story, Location, Tag, Comment

agent = WebAgent()
account = Account("username")

posts = agent.get_media(account, pointer=None, count=5)
res = list(list(posts)[0])
i = 0 #counts of posts
likes = []
#comments = []
while True:
	media = Media(res[i])
	likes.append(media.likes_count)
	#comments.append(media.comments_count)
	i += 1
	if i == len(res):
		print(likes)
		likes.clear()
		time.sleep(10)	
		i = 0
		for i in range(len(res)):
			media = Media(res[i])
			agent.update(media)

		i = 0


