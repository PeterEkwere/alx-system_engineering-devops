#!/usr/bin/python3
"""
    This module gets an info on an employee using REAST API
    Author: Peter Ekwere
"""
import csv
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
            data = []

            for i in range(len(user_todo)):
                new_data = []
                status = user_todo[i].get("completed")
                title = user_todo[i].get("title")
                new_data = [f'{user_id}', f'{user_name}',
                            f'{status}', f'{title}']
                data.append(new_data)
            file_name = f"{user_id}.csv"
            with open(file_name, "w") as csv_file:
                csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                csv_writer.writerows(data)
        else:
            print(f"Error: Unable to fetch data user info"
                  f"(Status code {user_info.status_code})")
    else:
        print(f"Error: Unable to fetch data user todo"
              f"(Status code {user_todo.status_code})")
