import praw
import time
from praw.models import MoreComments

reddit = praw.Reddit('c1')

subreddit = reddit.subreddit('nba')

#f = open('nba_reddit_10000.txt', 'w')

for submission in subreddit.submissions(1490011123,1497229236):
    print("Title",submission.title)
    print("Text",submission.selftext)
    print("Score",submission.score)
    #f.write("Title:")
    #f.write(str(submission.title))
    #f.write("\n")
    #f.write("Text:")
    #f.write(str(submission.selftext))
    #f.write("\n")
    #f.write("Score:")
    #f.write(str(submission.score))
    #f.write("\n")
    submission.comments.replace_more(limit=0)
    for comments in submission.comments.list():
        if isinstance(comments, MoreComments):
            continue
        #f.write("Comment:")
        #f.write(str(comments.body.encode('utf-8')))
        #f.write("\n")
        print("Comment", comments.body)
    #f.write("----END----\n")
    print("Timestamp",submission.created)
    print("----------------")
    time.sleep(2)
