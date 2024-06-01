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


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints the titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        res = requests.get(url)
        res.raise_for_status()  # Raise an exception for HTTP errors
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return

    print("Status Code: {}".format(res.status_code))

    if res.headers.get("Content-Type") == "application/json; charset=utf-8":
        json_data = res.json()
        for post in json_data:
            print(post["title"])

def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them in a csv file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        res = requests.get(url)
        res.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return

    if res.headers.get("Content-Type") == "application/json; charset=utf-8":
        json_data = res.json()

        csvfile = "posts.csv"
        data = []

        for key, value in json_data[0].items():
            dict_data = {}
            if key != "UserId":
                dict_data[key] = value
            data.append(dict_data)

        headers = dict_data.keys()

        with open(csvfile, "w", newline="") as file:
            csv_write = csv.DictWriter(file, fieldnames=headers)
            csv_write.writeheader()
            csv_write.writerows(data)
