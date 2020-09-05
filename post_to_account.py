import os
from instabot import Bot 
import psycopg2
import time

def postToAccount():
    databaseName = str(input("Enter database name: "))
    user = str(input("Enter database user: "))
    passwordDataBase = str(input("Enter database password: "))
    path = str(input("Enter path of directory of instagram photos: "))
    db = psycopg2.connect(database=databaseName,user=user,password=passwordDataBase,host="127.0.0.1",port="5432")

    cursor = db.cursor()
    username = str(input("Enter instagram username: "))
    password = str(input("Enter instagram password: "))
    bot = Bot() 
    os.chdir(path)
    bot.login(username = username,  
            password = password) 
    r = cursor.execute("SELECT * FROM photos_instagram")
    rows = cursor.fetchall()
    for row in rows:
        owner = row[3]
        path = row[1]
        status = row[2]
        ID = row[0]
        caption = "Owner: " + "@"+ owner + "\n" + "If you are the owner of the post and want to remove it, please contact me and I will remove it."
        if status == "NOTPOSTED":
            bot.upload_photo(path,caption=caption)
            time.sleep(10)
            cursor.execute("SELECT * FROM photos_instagram WHERE id = "+"'"+ID+"'"+";")
            cursor.execute("UPDATE photos_instagram SET status = 'POSTED';")
            os.rename(ID+".REMOVE_ME",ID+".jpeg")
        else:
            pass

    db.commit()
    db.close()
