import praw
from textblob import TextBlob   

reddit = praw.Reddit('bot', user_agent='cs40bot')

# Upvote any submission mentioning my favorite candidate
for submission in list(reddit.subreddit("BotTown2").new(limit=500)):
    if 'biden' in submission.title.lower():
        submission.upvote()
        print('Submission Upvoted!')
# Downvote any submission mentioning a candidate I don't like
    if 'trump' in submission.title.lower():
        submission.downvote()
        print('Submission Downvoted!')
# Upvoting or downvoting comments based on polarity 
    for comment in submission.comments.list():
        blob = TextBlob(str(comment.body))
        polarity = blob.sentiment.polarity
        if 'biden' in comment.body.lower() and polarity > 0.5:
            comment.upvote()
        if 'trump' in comment.body.lower() and polarity > 0.5:
            comment.downvote()