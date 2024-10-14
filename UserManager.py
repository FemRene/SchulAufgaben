import sqlite3


def getAllUsers() -> list['']:
    data = []
    conn = sqlite3.connect("users.sql")
    c = conn.cursor()
    c.execute("select * from users")
    records = c.fetchall()
    for record in records:
        data.append((record[0], record[1], record[2], record[3], record[4], record[5]))
    conn.commit()
    conn.close()
    return data


def getUserByID(id: int) -> list['']:
    data = []
    conn = sqlite3.connect("users.sql")
    c = conn.cursor()
    c.execute(f"select * from users where ID is '{id}'")
    records = c.fetchall()
    for record in records:
        data.append((record[0], record[1], record[2], record[3], record[4], record[5]))
    conn.commit()
    conn.close()
    return data


def getUserByName(name: str) -> list['']:
    data = []
    conn = sqlite3.connect("users.sql")
    c = conn.cursor()
    c.execute(f"select * from users where Name is '{name}'")
    records = c.fetchall()
    for record in records:
        data.append((record[0], record[1], record[2], record[3], record[4], record[5]))
    conn.commit()
    conn.close()
    return data


def addUser(Name: str, Vorname: str, Geburtsdatum: str, Adresse: str, Email: str):
    exe: bool = False
    conn = sqlite3.connect("users.sql")
    c = conn.cursor()
    if c.execute(f"INSERT INTO users (Name, Vorname, Geburtsdatum, Adresse, Email) VALUES ('{Name}', '{Vorname}', '{Geburtsdatum}', '{Adresse}', '{Email}');"):
        exe = True
    conn.commit()
    conn.close()
    return exe


def deleteUserByID(id: int):
    exe: bool = False
    conn = sqlite3.connect("users.sql")
    c = conn.cursor()
    if c.execute(f"delete from users where ID is '{id}'"):
        exe = True
    conn.commit()
    conn.close()
    return exe


def deleteUserByName(name: str):
    exe: bool = False
    conn = sqlite3.connect("users.sql")
    c = conn.cursor()
    if c.execute(f"delete from users where Name is '{name}'"):
        exe = True
    conn.commit()
    conn.close()
    return exe