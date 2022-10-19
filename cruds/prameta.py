from pickletools import string1
import sqlite3
from turtle import Turtle
from fastapi import *


def my_party(pokemon_name):
    conn = sqlite3.connect("pokemon.db")
    c = conn.cursor()
    c.execute("insert into My_pokemon values(?)", (pokemon_name))
    conn.commit()
    conn.close()
    return 0


def parameta_cal(origin: int, endevor: int):
    return ((origin * 2 + 31 + (endevor / 4)) * 50 / 100) + 5


def hp_cal(origin: int, endevor: int):
    return ((origin * 2 + 31 + (endevor / 4)) * 50 / 100) + 60
