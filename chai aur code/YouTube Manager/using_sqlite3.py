import sqlite3

conn = sqlite3.connect('video_manager.db')
cursor = conn.cursor()

# ''' ''' Is recommended as is keeps data as formatted 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY, name TEXT NOT NULL, time TEXT NOT NULL)''')


def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()


def update_video(id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, id))
    conn.commit()


def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (id,))
    conn.commit()


def main():
    print("\nVIDEO MANAGER IN DB")
    print("You can do the following operations:", end = '\n\n')
    while True:
        print("\n1. List all videos")
        print("2. Add a YouTube Video")
        print("3. Update video details")
        print("4. Delete a Video")
        print("5. Exit the Program", end = '\n\n')
        print("Choose an Option:", end = " ")
        user_input = input()

        match user_input:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter Video Name: ")
                time = input("Enter Video Time: ")
                add_video(name, time)
            case '3':
                id = input("Enter Video ID: ")
                name = input("Update Name: ")
                time = input("Update Time: ")
                update_video(id, name, time)
            case '4':
                id = input("Enter Video ID to Delete: ")
                delete_video(id)
            case '5':
                print("Thank You for using my Program")
                break
            case _:  # Default Case
                print("Invalid Choice")

    # After While Loop close the connection in order to successfully exit safely
    conn.close()

if __name__ == "__main__":
    main()