#!/usr/bin/python3
"""
MK: number of subcs for a given sub reddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns number of subs
    (not active users, total subs) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)

    if response.status_code == 200:
        try:
            results = response.json()

            # Check if 'data' key is present in the response
            if 'data' in results:
                # Check if 'subscribers' key is present in the 'data' dictionary
                subscribers = results['data'].get('subscribers')
                if subscribers is not None:
                    return subscribers

            # If 'data' or 'subscribers' key is missing, print an error message
            print("Error: Unexpected response format")
            return 0

        except Exception as e:
            print("Error parsing JSON: {}".format(e))
            return 0
    else:
        print("Request failed with status code {}".format(response.status_code))
        return 0
