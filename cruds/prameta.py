from pickletools import string1
import sqlite3
from turtle import Turtle
from fastapi import *
import main as main

dbname = "pokemon.db"


def my_get_parameta():
    pokemon = []
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT name FROM My_pokemon")
    for row in cur:
        print(row[0])
        pokemon.append(row[0])
    conn.close
    pokemon_data = []
    output_data = []
    j = 0
    for i in pokemon:
        pokemon_data.append((main.df[main.df["名前(フォルム)"] == i]).values[0])
    return pokemon_data


def my_pokemon_regsist(pokemondata, endever):
    my_pokemon_data = pokemon_parameta(pokemondata, endever)
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql = "insert into My_pokemon_parameta(name,main_type,sub_type,hp,attack,deffence,sp_attack,sp_deffence,speed)values(?,?,?,?,?,?,?,?,?)"
    data = (
        my_pokemon_data[0],
        my_pokemon_data[1],
        my_pokemon_data[2],
        int(my_pokemon_data[3]),
        int(my_pokemon_data[4]),
        int(my_pokemon_data[5]),
        int(my_pokemon_data[6]),
        int(my_pokemon_data[7]),
        int(my_pokemon_data[8]),
    )
    c.execute(sql, data)
    conn.commit()
    conn.close()
    return 0


def pokemon_set_parameta(pokemon_data, endevor: list):
    pokemon_para_data = []
    _endevor = endevor[0].split(",")
    for i in range(0, 9):

        if i <= 2:
            pokemon_para_data.append(pokemon_data[i])
        elif i == 3:
            pokemon_para_data.append(hp_cal(int(pokemon_data[i]), int(_endevor[i - 3])))
        elif i > 3:
            pokemon_para_data.append(
                parameta_cal(int(pokemon_data[i]), int(_endevor[i - 3]))
            )
    return pokemon_para_data


def parameta_cal(origin: int, endevor: int):
    return ((origin * 2 + 31 + (endevor / 4)) * 50 / 100) + 5


def hp_cal(origin: int, endevor: int):
    return ((origin * 2 + 31 + (endevor / 4)) * 50 / 100) + 60
