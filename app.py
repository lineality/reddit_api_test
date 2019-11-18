#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 21:03:23 2019
@author: secret_santa_big_mood_Broccoli
"""

"""
For decouple (for the environmental variables)
!pipenv install python-decouple
or
conda install python-decouple
see: https://pypi.org/project/python-decouple/

For PRAW (python wrapper for the reddit api)
See: https://praw.readthedocs.io/en/latest/
!pipenv install praw
or
conda install praw
"""


"""
r's elegant version:

import praw

reddit = praw.Reddit(client_id="",
                     client_secret="",
                     user_agent="")


subs = reddit.subreddits.popular()
for i in subs.__iter__():
    print(i)

"""


#importing libraries and packages
import decouple
from decouple import config
import praw

"""configuring connecting to the reddit API, getting data from env-file"""
reddit = praw.Reddit(client_id = config('client_id'),
                    client_secret = config('client_secret'),
                    password = config('password'),
                    user_agent = config('user_agent'),
                    username = config('username')
                    )

"""making connection"""
reddit

"""
examples of what can be done with connection
https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
"""

# get 10 hot posts from the MachineLearning subreddit
hot_posts = reddit.subreddit('MachineLearning').hot(limit=5)
for post in hot_posts:
    print(post.title)

# get hottest posts from all subreddits
hot_posts = reddit.subreddit('all').hot(limit=5)
for post in hot_posts:
    print(post.title)

# from a dataframe
# https://datatofish.com/export-pandas-dataframe-json/
import pandas as pd
posts = []
ml_subreddit = reddit.subreddit('MachineLearning')
for post in ml_subreddit.hot(limit=10):
    posts.append([post.title,
                post.score,
                post.id,
                post.subreddit,
                post.url,
                post.num_comments,
                post.selftext,
                post.created])
posts = pd.DataFrame(posts,columns=['title',
                                    'score',
                                    'id',
                                    'subreddit',
                                    'url',
                                    'num_comments',
                                    'body',
                                    'created'])
print(posts)

"""
#exports df (current working directory)
df.to_csv('data.csv')
posts.to_csv('posts_csv.csv')

see:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html

df.to_json(r'Path where you want to store the exported JSON file\File Name.json')
posts.to_json(r'Path where you want to store the exported JSON file\posts_json.json')

See:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html
"""

# get MachineLearning subreddit data
ml_subreddit = reddit.subreddit('MachineLearning')

print(ml_subreddit.description)



"""Get comments from a specific post"""
submission = reddit.submission(url="https://www.reddit.com/r/MapPorn/comments/a3p0uq/an_image_of_gps_tracking_of_multiple_wolves_in/")
# or
submission = reddit.submission(id="a3p0uq")

"""To get the top-level comments we only need to iterate over"""
for top_level_comment in submission.comments:
    print(top_level_comment.body)

""" we can check the datatype of each comment before printing the body."""
from praw.models import MoreComments
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body)


"""
a method called replace_more ,
which replaces or removes the MoreComments
"""

submission.comments.replace_more(limit=0)
for top_level_comment in submission.comments:
    print(top_level_comment.body)

"""
CommentForest provides the .list method,
which can be used for getting all comments
inside the comment section."""

submission.comments.replace_more(limit=0)
for comment in submission.comments.list():
    print(comment.body)
