#!/usr/bin/python3
"""
    This module gets an info on an employee using REAST API
    Author: Peter Ekwere
"""
import json
import requests


if __name__ == "__main__":
    """ If run Directly """
    user_todo = requests.get('https://jsonplaceholder.typicode.com/todos/')
    user_info = requests.get('https://jsonplaceholder.typicode.com/users/')

    if user_todo.status_code == 200:
        if user_info.status_code == 200:
            user_todo = user_todo.json()
            user_info = user_info.json()
            data = {}
            i = 0

            for j in range(len(user_info)):
                user_id = user_info[j].get("id")
                user_name = user_info[j].get("username")
                new_data = []
                for i in range(len(user_todo)):
                    if user_id == user_todo[i].get("userId"):
                        items = {}
                        items["username"] = user_name
                        items["task"] = user_todo[i].get("title")
                        items["completed"] = user_todo[i].get("completed")
                        new_data.append(items)

                data[user_id] = new_data
            file_name = "todo_all_employees.json"
            with open(file_name, "w") as json_file:
                json_string = json.dumps(data)
                json_file.write(json_string)
        else:
            print(f"Error: Unable to fetch data user info"
                  f"(Status code {user_info.status_code})")
    else:
        print(f"Error: Unable to fetch data user todo"
              f"(Status code {user_todo.status_code})")
