#criando Banco de Dados

# importando SQLite
import sqlite3 as lite

#criando conectecão
con = lite.connect('dados.db')

# tabela quantia total
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Quantia(id INTEGER PRIMARY KEY AUTOINCREMENT, valor DECIMAL)")

#Tabela de Despesas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Despesas (id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, descricao TEXT, valor DECIMAL)")