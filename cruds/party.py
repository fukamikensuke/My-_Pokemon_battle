from pickletools import string1
import sqlite3
from turtle import Turtle
from fastapi import *


def my_regist(pokemon_name: str):
    conn = sqlite3.connect("pokemon.db")
    c = conn.cursor()
    c.execute("insert into My_pokemon values(null,?)", [pokemon_name])
    conn.commit()
    conn.close()
    return 0


def chose_my_party(chose_list: list):
    conn = sqlite3.connect("pokemon.db")
    name_list = []
    c = conn.cursor()
    c.execute(
        "SELECT hp FROM My_pokemon_parameta WHERE id = %d OR id = %d OR id = %d"
        % (int(chose_list[0]), int(chose_list[1]), int(chose_list[2]))
    )
    i = 0
    for row in c:
        sql = "insert into pokemon_battle_status (id,who,hp,attack,deffence,sp_attack,sp_deffence,speed)values(?,?,?,?,?,?,?,?)"
        data = (chose_list[i], 0, int(row[0]), 0, 0, 0, 0, 0)
        c.execute(sql, data)
    cur = conn.cursor()
    cur.execute(
        "SELECT name FROM My_pokemon_parameta WHERE id = ? OR id = ? OR id = ?",
        (chose_list[0], chose_list[1], chose_list[2]),
    )
    for row in cur:
        print(row[0])
        name_list.append(row[0])
    conn.commit()
    conn.close()
    print(name_list)
    return name_list


def get_myparty():
    conn = sqlite3.connect("pokemon.db")
    pokemon_data = []
    c = conn.cursor()
    c.execute("SELECT * FROM My_pokemon")
    for row in c:
        print(row[0])
        pokemon_data.append(row[0])
    conn.close
    conn.commit()
    conn.close()
    return pokemon_data

def get_skill_list(id):
    