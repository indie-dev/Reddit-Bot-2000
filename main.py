import praw
import random
import time

print "I am Softy:)"

replied_users = set()

def run(r):
	for comment in r.subreddit('all').comments(limit=200):
		if ' ' in comment.body or '' in comment.body:
			for user in replied_users:
				print user
			if comment.author in replied_users:
				print 'Not replying'
			else:
				print comment.author
				print comment.body
				comment.reply("Do you own an Android phone? Do you want to check out a new, awesome, minimal launcher? Come check out mine called [Comely](https://play.google.com/store/apps/details?id=com.Softy.Launcher2). It's pretty, like you:)")
				replied_users.add(comment.author)
	run(r)

def secondry():
	user = "froggie-style-pepe"
	word = "abcgold13"
	cli_id = "sDZakdCFvFt5zg"
	cli_sec = "rmKHpCIkQqYA2EPDeDo1b83G6mc"
	
	r = praw.Reddit(username=user,
	    	password=word,
	    	client_id=cli_id,
	    	client_secret=cli_sec,
            	user_agent="SoftyBot 2000"
	 	)
	return r

r = secondry()

run(r)
