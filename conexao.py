import sqlite3
import datetime

conn = sqlite3.connect('db.sqlite3')

cursor = conn.cursor()

data_nascimento_antiga = {}

cursor.execute("SELECT id, birth_date FROM homepage_integrante")
rows = cursor.fetchall()

for row in rows:
    id, birth_date = row
    data_nascimento_antiga[id] = birth_date

conn.close()

for id, birth_date in data_nascimento_antiga.items():
    if birth_date:
        try:
            data_nascimento = datetime.datetime.strptime(birth_date, '%d/%m/%Y').date()
            data_nascimento_formatada = data_nascimento.strftime('%Y-%m-%d')
            data_nascimento_antiga[id] = data_nascimento_formatada
        except ValueError:
            print(f"Erro ao converter a data de nascimento para o id {id}: {birth_date}")
    else:
        data_nascimento_antiga[id] = None



for id, birth_date in data_nascimento_antiga.items():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("UPDATE homepage_integrante SET birth_date = ? WHERE id = ?", (birth_date, id))
    conn.commit()
    conn.close()