# Multi-Table Database - Tracks(Python 3.4.x)
import sqlite3
import xml.etree.ElementTree as ET

# Create tables
conn = sqlite3.connect("tracks.sqlite")
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);
CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);
''')

# Parse XML and save it to DB
fname = input("Enter file location:")
if len(fname) < 1: fname = "Library.xml"
stuff = ET.parse(fname)
all = stuff.findall("dict/dict/dict")
print("Tracks: ", len(all))
# Def this func to find the value of a key
def findvalue(labellist, key):
    found = False
    for label in labellist:
        if found: return label.text
        if label.tag == "key" and label.text == key: found = True
for item in all:
    if findvalue(item, "Track ID") is None: continue
    artist_name = findvalue(item, "Artist")
    genre_name = findvalue(item, "Genre")
    album_title = findvalue(item, "Album")
    track_title = findvalue(item, "Name")
    track_len = findvalue(item, "Total Time")
    track_rating = findvalue(item, "Rating")
    track_count = findvalue(item, "Play Count")
    if artist_name is None or genre_name is None or album_title is None: continue
    print(artist_name, genre_name, album_title)
    # Fill Artist
    cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?)", (artist_name,))
    cur.execute("SELECT id FROM Artist WHERE name = ?", (artist_name,))
    artist_id = cur.fetchone()[0]
    # Fill Genre
    cur.execute("INSERT OR IGNORE INTO Genre (name) VALUES (?)", (genre_name,))
    cur.execute("SELECT id FROM Genre WHERE name = ?", (genre_name,))
    genre_id = cur.fetchone()[0]
    # Fill Album
    cur.execute("INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?, ?)", (artist_id, album_title))
    cur.execute("SELECT id FROM Album WHERE title = ?", (album_title,))
    album_id = cur.fetchone()[0]
    # Fill Track
    cur.execute('''INSERT OR REPLACE INTO TRACK (title, album_id, genre_id, len, rating, count) VALUES
    (?, ?, ?, ?, ?, ?)''', (track_title, album_id, genre_id, track_len, track_rating, track_count))
    conn.commit()

# Printing
cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.ID AND Track.album_id = Album.id AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3''')
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())
cur.close()
