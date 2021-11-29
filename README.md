# HW_04 
### Reddit Bot for CSCI040
My Reddit Bot "professionalcs40bot" is a bot that likes to convince people to move/visit a different state.

My [favorite interaction involving my bot](https://old.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/hlvekka/) took place on the [BotTown2](https://old.reddit.com/r/BotTown2/) subreddit. 

<img width="1001" alt="Screenshot of My Bot's Interaction with Other Bots" src="https://github.com/qchen2323/hw_04/blob/755028a31fd036b093b15386b03e1eadb3da0eb0/bot%20interaction%20screenshot.png">

I like how all the other bots started interact with my bot.


#### The Output of my `bot_counter.py` file running:

```
PS C:\Users\Srly4\College\CSCI 40\bot> python3 bot_counter.py --username professionalcs40bot
len(comments)= 783
len(top_level_comments)= 98
len(replies)= 685
len(valid_top_level_comments)= 64
len(not_self_replies)= 684
len(valid_replies)= 676
========================================
valid_comments= 740
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
```
These numbers above were captured on Saturday, November 27, 2021 at 10:27:26 PM. Since then, I ran into some issues that reduced my valid comments. However, I do have a screenshot available that will prove that my bot did reach these numbers. 

<img width="1001" alt="Screenshot of My Valid Comments on Saturday, November 27, 2021 at 10:27:26 PM" src="https://github.com/qchen2323/hw_04/blob/4c86f3d427339e6af6b14871cbbf149a141cc2b2/valid%20comment%20screenshot.png">

#### My Score

My score for this project should be 32/30. 
- **+18 Points**: My `bot.py` file works correctly, and each `FIXME` has been fixed. 
- **+2 Points**: My github repo awards 2 points.
- **+4 Points**: Looking at the output of my `bot_counter.py` file, my bot has 740 valid comments. This overall awards me 4 points, from extra credit tasks 1 and 2. 
- **+2 Points**: I also created a `submission.py` file for task 4. My bot "professionalcs40bot" has posted over 200 submissions. The submissions included reposts from other subreddits and self posts that contain unique titles and links. You can see these submissions within the [BotTownAlt](https://old.reddit.com/r/BotTownAlt/) subreddit. This awards 2 points.
- *I did not complete task 5.*
- **+2 Points**: I completed task 6 by adding a line of code in task 4 of `bot.py`. This is seen in line 180. This awards 2 points.
- **+4 Points**: I completed task 7 by creating a separate python file `upvote_downvote.py`. This is worth two points. I also used the TextBlob sentiment analysis library to decide when to upvote and downvote. This awards additional two points. I should receive 4 points total because my bot has upvoted and downvoted at least 100 submissions and 500 comments.
- *I did not complete the 5 points of extra credit task.*

In total, my score will be **32 points** out of 30.


 
