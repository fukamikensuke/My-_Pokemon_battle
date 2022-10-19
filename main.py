from threading import currentThread
from tkinter import INSERT
import pandas as pd
import sqlite3
from fastapi import FastAPI, Form
import cruds.party as party

app = FastAPI()

df = pd.read_csv("ポケモンデータシート - ポケモンデータシート .csv")
df = df.drop(["ぜんこくNo.", "名前", "英語名"], axis=1)
my_pokemon = []

dbname = "pokemon.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS My_pokemon")
cur.execute(
    "CREATE TABLE My_pokemon(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)"
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


@app.get("/my_regist/parameta")
def my_prameta():
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT name FROM My_pokemon")
    for row in cur:
        print(row[0])
        my_pokemon.append(row[0])
    conn.close
    pokemon_data = []
    for i in my_pokemon:
        pokemon_data.append((df[df["名前(フォルム)"] == i]).values[0])
    print(pokemon_data)
    return pokemon_data


# for i in input_name_list:
#     df[df["名前"] == i]
