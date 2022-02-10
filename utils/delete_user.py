import requests
from pprint import pprint


URL = "http://127.0.0.1:5000/users"

def display_user(pk):
    current_user = requests.get("%s/%s" % (URL, pk))
    if current_user.status_code == 200:
        pprint(current_user.json())
    else:
        print(
            "Something went wrong while "
            "trying to update the user."
        )


def delete_user(pk):
   
    out = requests.delete("%s/%s" % (URL, pk))
    if out.status_code == 204:
        print("User Deleted")
    else:
        print(
            "Something went wrong while "
            "trying to delete a user.")

if __name__ == "__main__":
    pk = int(input("Type in the desired user id: "))
    print("Current User: ")
    display_user(pk)
    option = input("Would you like to delete the displayed user? [y/n]")
    if option == "y" or option == "Y":
        delete_user(pk)