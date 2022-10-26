from pickletools import int4
from ssl import PROTOCOL_SSLv23
from threading import currentThread
from tkinter import INSERT
import pandas as pd
import sqlite3
from fastapi import FastAPI, Form
import cruds.party as party
import cruds.prameta as parameta
import cruds.db_create as db_create
import array

app = FastAPI()

db_create.create_db()

df  = pd.read_csv("ポケモンデータシート - ポケモンデータシート .csv")
skill_df = pd.read_csv("技データリスト.csv")
df = df.drop(["ぜんこくNo.", "名前", "英語名"], axis=1)
skill_df = skill_df.drop(["ダイマックス","直接","守る","対象","説明"],axis=1)
a = skill_df.values

print(a[0])
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
    # p2: list = Form(),
    # p3: list = Form(),
    # p4: list = Form(),
    # p5: list = Form(),
    # p6: list = Form(),
):

    pokemon_data = parameta.my_get_parameta()
    parameta.my_pokemon_regsist(pokemon_data[0], p1)
    # parameta.my_pokemon_regist(pokemon_data[1], p2)
    # parameta.my_pokemon_regist(pokemon_data[2], p3)
    # parameta.my_pokemon_regist(pokemon_data[3], p4)
    # parameta.my_pokemon_regist(pokemon_data[4], p5)
    # parameta.my_pokemon_regist(pokemon_data[5], p6)
    return {"message": "Ok"}


# for i in input_name_list:
#     df[df["名前"] == i]
