import json
import os
import typing as tp
from getpass import getpass

import twill.commands as t


def get_data(username: tp.Optional[str] = None, password: tp.Optional[str] = None):
    os.remove("./output.json")

    if username is None:
        username = input("Enter username:")
    if password is None:
        password = getpass("Enter password:")

    login = "https://safetynet.liverpool.ac.uk/login/"

    t.go(login)
    t.showforms()
    t.form_clear("1")
    t.formvalue("1", "username", username)
    t.formvalue("1", "password", password)
    t.submit("1")

    t.go(
        "https://safetynet.liverpool.ac.uk/equipment/booking/api/list/?limit_to=&start=2023-03-26T00%3A00%3A00Z&end=2023-05-07T00%3A00%3A00%2B01%3A00"
    )

    with open("output.json", "w+") as f:
        t.set_output(f)
        t.show()


if __name__ == "__main__":
    get_data()
