#!/usr/bin/python3
"""
    This module gets an info on an employee using REST API
    Author: Peter Ekwere
"""
import requests
import sys


if __name__ == "__main__":
    """ if module is run directly DO """
    user_id = sys.argv[1]
    user_todo = requests.get(f'https://jsonplaceholder.typicode.com/users/'
                             f'{user_id}/todos')
    user_info = requests.get(f'https://jsonplaceholder.typicode.com/users/'
                             f'{user_id}')

    if user_todo.status_code == 200:
        if user_info.status_code == 200:
            user_todo = user_todo.json()
            user_info = user_info.json()

            user_name = user_info.get("name")
            total_tasks = len(user_todo)
            done_tasks = 0
            titles = []

            for i in range(len(user_todo)):
                if user_todo[i].get("completed") is True:
                    done_tasks += 1
                    titles.append(user_todo[i].get("title"))
            print(f"Employee {user_name} is done with"
                  f"tasks({done_tasks}/{total_tasks}):")
            for title in titles:
                print(f"\t {title}")
        else:
            print(f"Error: Unable to fetch data user info"
                  f"(Status code {user_info.status_code})")
    else:
        print(f"Error: Unable to fetch data user todo"
              f"(Status code {user_todo.status_code})")
