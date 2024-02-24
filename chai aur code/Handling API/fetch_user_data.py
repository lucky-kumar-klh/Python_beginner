import requests

def fetech_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    # print(response)
    # Converting the reponse from string to json
    data = response.json()
    # print(data)
    if data["success"] and data in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]

        return username, country
    
    else:
        # Raise an error
        raise Exception("Failed to fetch User-Data")


def main():
    try:
        username, country = fetech_random_user()
        print(f"Username: {username}\nCountry: {country}")
    except Exception as exp: 
        print(str(exp))

if __name__ == "__main__":
    main()

