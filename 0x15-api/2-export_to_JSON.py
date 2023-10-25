#!/usr/bin/python3
"""
    This module gets an info on an employee using REAST API
    Author: Peter Ekwere
"""
import json
import requests
import sys


if __name__ == "__main__":
    """ If run Directly """
    user_id = sys.argv[1]
    user_todo = requests.get(f'https://jsonplaceholder.typicode.com/users/'
                             f'{user_id}/todos')
    user_info = requests.get(f'https://jsonplaceholder.typicode.com/users/'
                             f'{user_id}')

    if user_todo.status_code == 200:
        if user_info.status_code == 200:
            user_todo = user_todo.json()
            user_info = user_info.json()

            user_name = user_info.get("username")
            data = {}
            new_data = []

            for i in range(len(user_todo)):
                items = {}
                items["task"] = user_todo[i].get("title")
                items["completed"] = user_todo[i].get("completed")
                items["username"] = user_name
                new_data.append(items)
            data[user_id] = new_data
            file_name = f"{user_id}.json"
            with open(file_name, "w") as json_file:
                json_string = json.dumps(data)
                json_file.write(json_string)
        else:
            print(f"Error: Unable to fetch data user info"
                  f"(Status code {user_info.status_code})")
    else:
        print(f"Error: Unable to fetch data user todo"
              f"(Status code {user_todo.status_code})")
