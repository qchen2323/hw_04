import praw
import time

from praw.reddit import Subreddit

reddit = praw.Reddit('bot', user_agent='cs40bot')

Subreddit = reddit.subreddit("politics").top(limit=200)
for post in Subreddit:
    print('title=', post.title)
    reddit.subreddit("BotTownAlt").submit(title=post.title, url=post.url )