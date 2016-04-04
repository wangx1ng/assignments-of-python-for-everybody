# Many Students in Many Courses(Python 3.4.x)
import json
import sqlite3

# Create tables
conn = sqlite3.connect("roster.sqlite")
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Membership;
CREATE TABLE Students (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT NOT NULL UNIQUE
);
CREATE TABLE Courses (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT NOT NULL UNIQUE
);
CREATE TABLE Membership (
student_id INTEGER NOT NULL,
course_id INTEGER NOT NULL,
role INTEGER,
PRIMARY KEY (student_id, course_id)
);''')

# Parse json file and feed data into tables
fname = input("Enter file name:")
if len(fname) < 1: fname = "roster_data.json"
jdata = json.loads(open(fname).read())
for entry in jdata:
    name = entry[0]
    title = entry[1]
    role = entry[2]
    print(name, title)
    # Fill Students
    cur.execute("INSERT OR IGNORE INTO Students (name) VALUES (?)", (name,))
    cur.execute("SELECT id FROM Students WHERE name = ?", (name,))
    student_id = cur.fetchone()[0]
    # Fill Courses
    cur.execute("INSERT OR IGNORE INTO Courses (title) VALUES (?)", (title,))
    cur.execute("SELECT id FROM Courses WHERE title = ?", (title, ))
    course_id = cur.fetchone()[0]
    # Fill Membership
    cur.execute("INSERT INTO Membership (student_id, course_id, role) VALUES (?, ?, ?)", (student_id, course_id, role))
conn.commit()

# Retrieve data
cur.execute('''
SELECT hex(Students.name || Courses.title || Membership.role ) AS X FROM
    Students JOIN Membership JOIN Courses
    ON Students.id = Membership.student_id AND Membership.course_id = Courses.id
    ORDER BY X''')
print(cur.fetchone())
