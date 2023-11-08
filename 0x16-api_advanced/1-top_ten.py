#!/usr/bin/python3
"""
  This api queries the reddit api
  Author: Peter Ekwere
"""
import requests


def top_ten(subreddit):
    """ Returns the title of the 10 hottest posts for a subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
            "User-Agent": "v1.0.0"
            }
    params = {
            "limit": 10
            }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return 0
    res = response.json().get("data")
    for hottest in res.get("children"):
        print(hottest.get("data").get("title"))
