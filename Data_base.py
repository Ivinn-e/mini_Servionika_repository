import mysql.connector

from mysql.connector import connect, Error



mydb = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="Wassabbathmetal1975)",
        database="servionika_db", 
        )

cursor = mydb.cursor()

create_table_query = "CREATE TABLE applications"\
                        "(media_group_id INT NOT NULL, "\
                        "chat_id TEXT NOT NULL, "\
                        "media_group_caption TEXT, "\
                        "photo BLOB NOT NULL, "\
                        "PRIMARY KEY (media_group_id))"

#cursor.execute(create_table_query)

insert_data_applications_query = "INSERT INTO applications"\
                                "(media_group_id, chat_id, "\
                                "media_group_caption, photo)"\
                                "VALUES (%s, %s, %s, %s)"

def Insert_data_appications(media_group_id, chat_id, media_group_caption,
                            photo):
        insert_data = [media_group_id, chat_id, media_group_caption, photo]
        cursor.executemany(insert_data_applications_query, insert_data)