import praw
import random
import time

print "I am Softy:)"

replied_posts = set()
replied_users = set()

def run(r):
	for comment in r.subreddit('depression').new(limit=200):
		if 'suicide' in comment.title or 'kill myself' in comment.title or '' in comment.title:
			for user in replied_users:
				print user
			if comment.author in replied_posts:
				print 'Not replying'
			else:
				print comment.author
				print comment.title
				comment.reply("You. Yes,  you. You are beautiful. You are amazing. Keep doing you. If you or anyone you know is on the verge of suicide, please call the national suicide hotline at 1-800-273-8255. They need you, buddy.")
				replied_posts.add(comment.author)
	
	for replies in r.subreddit('all').comments(limit=200):
		if 'suicide' in replies.body or 'kill myself' in replies.body or '' in replies.body:
			for user in replied_users:
				print user
			if replies.author in replied_users:
				print 'Not replying'
			else:
				print replies.author
				print replies.title
				replies.reply("You. Yes,  you. You are beautiful. You are amazing. Keep doing you. If you or anyone you know is on the verge of suicide, please call the national suicide hotline at 1-800-273-8255. They need you, and you shouldn't be here alone.")
				replied_users.add(replies.author)
	run(r)

def secondry():
	user = "USERNAME"
	word = "PASSWORD"
	cli_id = "CLIENT_ID"
	cli_sec = "CLIENT_SECRET"
	
	r = praw.Reddit(username=user,
	    	password=word,
	    	client_id=cli_id,
	    	client_secret=cli_sec,
            	user_agent="SoftyBot 2000"
	 	)
	return r

r = secondry()

run(r)
