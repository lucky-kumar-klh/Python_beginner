import json

user_credentals = {}

def get_all_credentials():
    if len(user_credentals) != 0:
        for user_id, password in user_credentals.items():
            print(f"User ID: {user_id}, Password: {password}")
    else:
        print("No User Found !")

class create_user:

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
        user_credentals[user_id] = password

        with open("credentials.txt", 'a') as file:
            json.dump(f"User ID: {self.user_id}, Password: {self.password}", file)
    
    def get_credentials(self):
        if self.user_id in user_credentals:
            print("User Found with ID:", self.user_id)
        else:
            print("User NOT Found !")

    def delete_credentials(self):
        if self.user_id in user_credentals:
            print("User Deleted with ID:", self.user_id)
            del user_credentals[self.user_id]
        else:
            print("User NOT Found !")




user1 = create_user('2310080034', 'Klh@1234')  # user id & password
# user1.get_credentials()
get_all_credentials()