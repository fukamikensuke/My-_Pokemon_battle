import pandas as pd
import sqlite3


def create_db():
    df = pd.read_csv("ポケモンデータシート - ポケモンデータシート .csv")
    # skill_df = pd.read_csv("技データリスト.csv")
    df = df.drop(["ぜんこくNo.", "名前", "英語名"], axis=1)
    # skill_df = skill_df.drop(["ダイマックス", "直接", "守る", "対象", "説明"], axis=1)
    my_pokemon = []
    dbname = "pokemon.db"
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS My_pokemon")
    cur.execute("DROP TABLE IF EXISTS My_pokemon_parameta")
    cur.execute("DROP TABLE IF EXISTS My_pokemon_skill")
    # ポケモンの登録
    cur.execute(
        "CREATE TABLE My_pokemon(pokemon_id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)"
    )
    # ポケモンの個体値のDB
    cur.execute(
        "CREATE TABLE My_pokemon_parameta(id INTEGER,name STRING,main_type STRING,sub_type STRING,hp INTEGER,attack INTEGER,deffence INTEGER,sp_attack INTEGER,sp_deffence INTEGER,speed INTEGER)"
    )
    # #ポケモンの所持技
    cur.execute(
        "CREATE TABLE My_pokemon_skill(id INTEGER, skill_1 STRING,skill_2 STRING,skill_3 STRING,skill_4 STRING)"
    )
    # ポケモン能力変化のあたい
    # cur.execute("CREATE TABLE rank_table (num INTEGER,rank FLOAT)")
    # cur.execute("insert into rank_table values(0,1)")
    # cur.execute("insert into rank_table values(1,1.5)")
    # cur.execute("insert into rank_table values(2,2)")
    # cur.execute("insert into rank_table values(3,2.5)")
    # cur.execute("insert into rank_table values(4,3)")
    # cur.execute("insert into rank_table values(5,3.5)")
    # cur.execute("insert into rank_table values(6,4)")
    # cur.execute("insert into rank_table values(-1,0.67)")
    # cur.execute("insert into rank_table values(-2,0.5)")
    # cur.execute("insert into rank_table values(-3,0.4)")
    # cur.execute("insert into rank_table values(-4,0.33)")
    # cur.execute("insert into rank_table values(-5,0.29)")
    # cur.execute("insert into rank_table values(-6,0.25)")
    # #ポケモンのバトル中の能力変化
    # cur.execute(
    #     "CREATE TABLE pokemon_battle_status(id INTEGER, who INTEGER,hp INTEGER,attack INTEGER,deffence INTEGER,sp_attack INTEGER,sp_deffence INTEGER,speed INTEGER)"
    # )
    # 技データベース作成
    # cur.execute(
    #     "CREATE TABLE skill_data(id INTEGER , name STRING,type STRING, class STRING,power INTEGER,aim INTEGER,pp INTEGER)"
    # )
    # skill_data = skill_df.values
    # for i in skill_data:
    #     sql = "insert into skill_data(id,name,type,class,power,aim,pp) values(?,?,?,?,?,?,?)"
    #     data = [
    #         i[0],
    #         i[1],
    #         i[2],
    #         i[3],
    #         i[4],
    #         i[5],
    #         i[6],
    #     ]
    #     cur.execute(sql, data)
    # ポケモンのタイプＤＢ
    # cur.execute(
    #     "CREATE TABLE Pokemon_type(name STRING ,'ノーマル'FLOAT,'ほのお' FLOAT,'みず' FLOAT,'でんき' FLOAT,'くさ' FLOAT,'こおり' FLOAT,'かくとう' FLOAT,'どく' FLOAT,'じめん' FLOAT,'ひこう' FLOAT,'エスパー'FLOAT,'むし'FLOAT,'いわ' FLOAT,'ゴースト' FLOAT,'ドラゴン' FLOAT,'あく' FLOAT ,'はがね' FLOAT,'フェアリー' FLOAT)"
    # )
    # c = conn.cursor()
    # c.execute("insert into Pokemon_type values('ノーマル',1,1,1,1,1,1,1,1,1,1,1,1,0.5,0,1,1,0.5,1)")
    # c.execute("insert into Pokemon_type values('ほのお',1,0.5,0.5,1,2,2,1,1,1,1,1,2,0.5,1,0.5,1,2,1)")
    # c.execute("insert into Pokemon_type values('みず',1,2,0.5,1,0.5,1,1,1,2,1,1,1,2,1,0.5,1,1,1)")
    # c.execute("insert into Pokemon_type values('でんき',1,1,2,0.5,0.5,1,1,1,0,2,1,1,1,1,0.5,1,1,1)")
    # c.execute("insert into Pokemon_type values('くさ',1,0.5,2,1,0.5,1,1,0.5,2,0.5,1,0.5,2,1,0.5,1,0.5,1)")
    # c.execute("insert into Pokemon_type values('こおり',1,0.5,0.5,1,2,0.5,1,1,2,2,1,1,1,1,2,1,0.5,1)")
    # c.execute("insert into Pokemon_type values('かくとう',2,1,1,1,1,2,1,0.5,1,0.5,0.5,0.5,2,0,1,2,2,0.5)")
    # c.execute("insert into Pokemon_type values('どく',1,1,1,1,2,1,1,0.5,0.5,1,1,1,0.5,0.5,1,1,0,2)")
    # c.execute("insert into Pokemon_type values('じめん',1,2,1,2,0.5,1,1,2,1,0,1,0.5,2,1,1,1,2,1)")
    # c.execute("insert into Pokemon_type values('ひこう',1,1,1,0.5,2,1,2,1,1,1,1,2,0.5,1,1,1,0.5,1)")
    # c.execute("insert into Pokemon_type values('エスパー',1,1,1,1,1,1,2,2,1,1,0.5,1,1,1,1,0,0.5,1)")
    # c.execute("insert into Pokemon_type values('むし',1,0.5,1,1,2,1,0.5,0.5,1,0.5,2,1,1,0.5,1,2,0.5,0.5)")
    # c.execute("insert into Pokemon_type values('いわ',1,2,1,1,1,2,0.5,1,0.5,2,1,2,1,1,1,1,0.5,1)")
    # c.execute("insert into Pokemon_type values('ゴースト',0,1,1,1,1,1,1,1,1,1,2,1,1,2,1,0.5,1,1)")
    # c.execute("insert into Pokemon_type values('ドラゴン',1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,0.5,0)")
    # c.execute("insert into Pokemon_type values('あく',1,1,1,1,1,1,0.5,1,1,1,2,1,1,2,1,0.5,1,0.5)")
    # c.execute("insert into Pokemon_type values('はがね',1,0.5,0.5,0.5,1,2,1,1,1,1,1,1,2,1,1,1,0.5,2)")
    # c.execute("insert into Pokemon_type values('フェアリー',1,0.5,1,1,1,1,2,0.5,1,1,1,1,1,1,2,2,0.5,1)")
    conn.commit()
    conn.close()
    conn.close()

    return 0
