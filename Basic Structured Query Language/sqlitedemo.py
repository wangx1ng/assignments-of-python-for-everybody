# Counting Email in a Database(Python 3.4.x)
import sqlite3

# Connect to DB and create table
conn = sqlite3.connect("emails.sqlite")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

# Open file and get the information
fname = input("Enter the file location:")
try:
    fhand = open(fname)
except Exception as e:
    print(e)
    exit()
for line in fhand:
    if not line.startswith("From: "): continue
    org = line.split()[1].split("@")[1]
    print(org)
    cur.execute("SELECT count FROM Counts WHERE org = ?", (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (org,))
    else:
        cur.execute("UPDATE Counts SET count=count+1 WHERE org = ?", (org,))
conn.commit()

# Printing
for row in cur.execute("SELECT org, count FROM Counts ORDER BY count DESC"):
    print(str(row[0]) + ": " + str(row[1]))
cur.close()
