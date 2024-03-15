import json

user_credentials: dict = {}


def get_all_credentials():
    if len(user_credentials) != 0:
        for user_id, password in user_credentials.items():
            print(f"User ID: {user_id}, Password: {password}")
    else:
        print("No User Found !")


class CreateUser:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
        user_credentials[user_id] = password

        with open("credentials.txt", 'a') as file:
            json.dump(f"User ID: {self.user_id}, Password: {self.password}", file)

    def get_credentials(self):
        if self.user_id in user_credentials:
            print("User Found with ID:", self.user_id)
        else:
            print("User NOT Found !")

    def delete_credentials(self):
        if self.user_id in user_credentials:
            print("User Deleted with ID:", self.user_id)
            del user_credentials[self.user_id]
        else:
            print("User NOT Found !")


user1 = CreateUser('2310080034', 'Klh@1234')  # user id & password
# user1.get_credentials()
get_all_credentials()
