import json, sys, os
from api import CybApi

from settings import api_url, api_client_id, \
        api_client_secret, api_password, api_username

OKGREEN = '\033[92m'
FAIL = '\033[91m'

api = CybApi(api_username, api_password, api_client_id, api_client_secret)

roles = {"Design": 24, "Arkiv": 26, "Web": 23, "DJ": 20, "Kaféfunk": 19, "Barfunk": 18, "Arrmester": 17, "Kaffemester": 16, "Skjenkemester": 15}

data = json.load(open("persons.json", "r"))

def add_role():
    for d in data:
        if len(data[d]["groups"]) is not 0:
            print("Adding {}".format(data[d]["name"]))
            for i in data[d]["groups"]:
                if roles.get(i) is None:
                    continue
                if api.register_internrole(data[d]["username"], roles.get(i)):
                    print("--> {} {} DONE".format(i, roles.get(i)))
                else:
                    print("--> {} {} FAILED".format(i, roles.get(i)))

def get_users():
    users = api.get_users()
    for u in users:
        user_dict.update({u["username"]:u["id"]})

def add_card():
    for d in data:
        if len(data[d]["groups"]) is not 0 and len(data[d]["cardNumber"]) < 20:
            print("Adding {}".format(data[d]["name"]))
            if api.register_card(user_dict[data[d]["username"]], data[d]["cardNumber"]):
                print("--> {} {} DONE".format(data[d]["cardNumber"], OKGREEN))
            else:
                print("--> {} {} FAILED".format(data[d]["cardNumber"], FAIL))

add_role()
user_dict = {}
get_users()
add_card()
