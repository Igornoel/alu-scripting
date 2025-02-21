#!/usr/bin/python3
"""Return number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json" \
        .format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data') \
            .get('subscribers')
    return 0
<<<<<<< HEAD
=======
# Add a newline here
>>>>>>> 7a527e4588e199b792c06d8407cf1d017fcdc042
