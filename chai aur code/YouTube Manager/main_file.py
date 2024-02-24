import json

def load_data():
    try:   # If we get the file then do this
        with open('youtube_database', 'r') as file:
            return json.load(file)
        
    except FileNotFoundError:   # If we don't get the file then do this
        print("Your List is EMPTY !")
        print("Try Adding something")
        return []


def write_data(videos):
    with open('youtube_database', 'w') as file:
        # json.dump -> writes data on a file
        # (para1, para2): para1 -> what to write ? and para2 -> where to write ?
        json.dump(videos, file)


def list_all_videos(videos):
    if len(videos) == 0:
        print("Empty List.\nTry Adding some videos.", end = '\n\n')
        return
    
    print("Here's Your List of Videos:", end = '\n\n')
    print('*' * 100)
    for index, vid in enumerate(videos, start = 1):
        print(f"{index}. Name: {vid['name']}, Duration: {vid['time']}")
    print('*' * 100, end = '\n\n')

def add_video(videos):
    video_name = input("Enter Video Name: ")
    video_length = input("Enter Video Length: ")
    videos.append({'name': video_name, 'time': video_length})
    # write this data in file
    write_data(videos)
    print()

def update_video(videos):
    if len(videos) == 0:
        print("\nYour List is Empty")
        print("Add a video first !", end = '\n\n')
        return 
    
    list_all_videos(videos)
    index = int(input("Which video to Update: "))
    if 1 <= index <= len(videos):
        name = input("Enter New name: ")
        time = input("Enter New time: ")
        videos[index-1] = {'name': name, 'time': time}
        print("Successfully Updated !", end = '\n\n')
        # write the new data in the file
        write_data(videos)

    else:
        print("Entered Video number Not Found")
        print("Try Again !", end = '\n\n')

def delete_video(videos):
    if len(videos) == 0:
        print("\nYour List is Empty\nNo video to delete", end = '\n\n')
        return
    
    print("\nHere are your list of Videos:")
    list_all_videos(videos)
    delete = int(input("Which video you want to delete: "))
    if 1 <= delete <= len(videos):
        # videos.remove(videos[delete-1])
        del videos[delete-1]
        print("Video Successfully Deleted !", end = '\n\n')
        write_data(videos)
    else:
        print("Enter a valid choice")
        print("Try Again !", end = '\n\n')


def main():
    videos = load_data()
    print("\nYOUTUBE MANAGER")
    print("You can do the following operations:", end = '\n\n')
    while True:
        print("1. List all videos")
        print("2. Add a YouTube Video")
        print("3. Update video details")
        print("4. Delete a Video")
        print("5. Exit the Program", end = '\n\n')
        print("Choose an Option:", end = " ")
        user_input = input()

        match user_input:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Thank You for using my Program")
                break
            case _:  # Default Case
                print("Invalid Choice")


if __name__ == "__main__":
    main()