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


def chose_my_party(chose_list):

    return my_party_list


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
