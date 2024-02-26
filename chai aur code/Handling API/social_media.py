import requests
import time

def fetch_social_media_details(timer):
    print("Getting User Data ....")
    time.sleep(timer)
    url = "https://api.freeapi.app/api/v1/social-media/posts?page=1&limit=10"
    reponse = requests.get(url)
    data_set = reponse.json()

    if data_set["success"]:
        total_pages = data_set["data"]["totalPages"]
        total_posts = data_set["data"]["totalPosts"]
        return total_pages, total_posts
    else:
        print("Not Worked")
        return 

def main():
    try:
        pages, posts = fetch_social_media_details(2)
        print(f"Total Pages: {pages} & Posts: {posts}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()