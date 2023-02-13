import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('drop table if exists songs cascade; '
            'drop table if exists albums cascade;')

cur.execute('create table albums('
            'id int generated always as identity primary key,'
            'name text not null unique,'
            'image text not null unique);'
            )
cur.execute('create table songs('
            'id int generated always as identity primary key,'
            'name text not null unique,'
            'link text not null unique,'
            'album_id int references albums);'
            )

# Insert data into the table

cur.execute("insert into albums (name, image) values "
            "('POPSTAR', '/home/sirius/Загрузки/sounds_web/images/popstar.jpg'),"
            "('MONEYDEALER', '/home/sirius/Загрузки/sounds_web/images/moneydealer.png');"
            )


cur.execute("insert into songs (name, link, album_id) values "
            "('ЗА ДЕНЬГИ ДА', '/home/sirius/Загрузки/sounds_web/zadenigida.mp3', 1),"
            "('КАК MOMMY', '/home/sirius/Загрузки/sounds_web/kakmommy.mp3', 1),"
            "('LIPSI HA', '/home/sirius/Загрузки/sounds_web/lipsiha.mp3', 2),"
            "('И ЧТО', '/home/sirius/Загрузки/sounds_web/ichto.mp3', 2),"
            "('DADADA', '/home/sirius/Загрузки/sounds_web/dadada.mp3', 2),"
            "('JUICY', '/home/sirius/Загрузки/sounds_web/juicy.mp3', 2),"
            "('ХЛОПАЙ', '/home/sirius/Загрузки/sounds_web/hlopai.mp3', 2);"
            )

conn.commit()

cur.close()
conn.close()
