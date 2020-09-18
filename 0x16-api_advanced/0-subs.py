#!/usr/bin/python3
"""Module for a function that returns the number
of subscribers in a subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers to a specified subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-Agent': 'Derek@dhk'}
    req = requests.get(url, headers=user_agent, allow_redirects=False)
    if req.status_code == 200:
        req = req.json()
        data = req.get('data')
        subscribers = data.get('subscribers')
        if data is not None and subscribers is not None:
            return subscribers
    return 0
