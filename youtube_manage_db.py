import sqlite3


conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()
cursor.execute('''  
               CREATE TABLE IF NOT EXITS videos(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
               )
               ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name , time):
    cursor.execute("INSERT INTO videos (name ,time) VALUES (? , ?)" , (name , time))
    conn.commit()
    
def update_video(video_id , new_name , new_time):
    cursor.execute("UPDATE videos SET name = ? , time =? WHERE id = ?" , (new_name , new_time , video_id))
    conn.commit()
    
def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?",(video_id,))
    conn.commit()
def main():
        while true:
            print("\n youtube manager app with db")
            print("1. list videos")
            print("2. add videos")
            print("3. update videos")
            print("4. delete videos")
            print("5. exit app")
            choice = input("enter your choice:")
            
            if choice == '1':
                list_videos()
            elif choice == '2':
                name = input("Enter the new video name:")
                time = input("enter the new video time:")
                add_video(name, time)
            elif choice == '3':
                video_id = input("enetr video id to update:")
                name = input("Enter the new video name:")
                time = input("enter the new video time:")
                update_video(video_id, name, time)
            elif choice == '4':
                video_id = input("enetr video id to update:")
                
                delete_video(video_id)
            elif choice == '5':
                break
            else:
                print("inavild choice")
                            
conn.close()


if __name__ == "__main__":
    main()
