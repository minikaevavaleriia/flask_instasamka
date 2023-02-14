import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn


@app.route('/')
@app.route('/home')
def home():
    links = "home/sirius/Загрузки/sounds_web/kakmommy.mp3"
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select * from songs where name is not null;')
    songs = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('home.html', songs=songs, links=links)


@app.route('/music')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select * from songs where album_id = 2;')
    songs = cur.fetchall()
    cur.close()
    cur1 = conn.cursor()
    cur1.execute('select name from albums where id = 2;')
    album = cur1.fetchall()
    cur1.close()
    conn.close()
    return render_template('index.html', songs=songs, album=album, x=1)

#oihioefhco;evhdevo;lhl;
#kgilgfilfgilo



