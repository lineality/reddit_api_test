#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 21:03:23 2019

@author: secret_santa_big_mood_Broccoli
"""
import decouple
from decouple import config


#!pip install praw

import praw

reddit = praw.Reddit(client_id = config('client_id'),
                    client_secret = config('client_secret'),
                    password = config('password'),
                    user_agent = config('user_agent'),
                    username = config('username')
                    )

reddit 
