#!/usr/bin/python3
"""
task_02_requests.py fetches all posts from JSONPlaceholder

Attributes:
    url (str): url of JSONPlaceholder
    res (object): response from http request
    json_data (object): response as json
"""
import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"
res = None
json_data = None

try:
    res = requests.get(url)
except:
    print("failed to retrieve data")

print("Status Code: {}".format(response.status_code))

if res.headers.get("Content-Type") == "application/json; charset=utf-8":
    json_data = response.json()


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints the titles
    """
    for post in json_data:
        print(post["title"])


def fetch_and_save_posts():
    """
    Fetches all post from JSONPlaceholder and saves them in a csv file
    """
    posts = []
    posts_dict = {}
    csvfile = "posts.csv"

    for post in json_data:
        for key, value in post.items():
            posts_dict[key] = value
        posts.append(posts_dict)

    headers = posts[0].keys()

    with open(csvfile, "w", newline="") as file:
        csv_write = csv.DictWriter(file, fieldnames=headers)
        csv_write.writeheader()
        csv_write.writerows(posts)
