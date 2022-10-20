from pickletools import int4
from threading import currentThread
from tkinter import INSERT
import pandas as pd
import sqlite3
from fastapi import FastAPI, Form
import cruds.party as party
import cruds.prameta as parameta
import array

app = FastAPI()

df = pd.read_csv("ポケモンデータシート - ポケモンデータシート .csv")
df = df.drop(["ぜんこくNo.", "名前", "英語名"], axis=1)
my_pokemon = []

dbname = "pokemon.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS My_pokemon")
cur.execute("DROP TABLE IF EXISTS My_pokemon_parameta")
cur.execute(
    "CREATE TABLE My_pokemon(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)"
)
cur.execute(
    "CREATE TABLE My_pokemon_parameta(name STRING,main_type STRING,sub_type STRING,hp INTEGER,attack INTEGER,deffence INTEGER,sp_attack INTEGER,sp_deffence INTEGER,speed INTEGER)"
)
conn.close()


@app.get("/")
def root():
    a = (df[df["名前(フォルム)"] == "アルセウス"]).values[0]
    return {print(a)}


@app.post("/my_regist/")  # 自分のポケモンの登録
async def regist(
    p1: str = Form(),
    p2: str = Form(),
    p3: str = Form(),
    p4: str = Form(),
    p5: str = Form(),
    p6: str = Form(),
):
    party.my_regist(p1)
    party.my_regist(p2)
    party.my_regist(p3)
    party.my_regist(p4)
    party.my_regist(p5)
    party.my_regist(p6)

    return {"message": "Ok"}  # ユーザー名が返ってくる


@app.post("/my_regist/parameta")
def my_prameta(
    p1: list = Form(),
    p2: list = Form(),
    p3: list = Form(),
    p4: list = Form(),
    p5: list = Form(),
    p6: list = Form(),
):
    pokemon_data = parameta.my_get_parameta()
    my_pokemon_data = parameta.pokemon_parameta(pokemon_data[0], p1)
    print(pokemon_data[0])
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
    return {"message": "Ok"}


# for i in input_name_list:
#     df[df["名前"] == i]
