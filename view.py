# importando SQLite
import sqlite3 as lite

#criando conectecão
con = lite.connect('dados.db')


# inserir quantia
def inserir_quantia(i):
    with con:
        cur = con.cursor()
        query ="INSERT INTO Quantia (valor) VALUES (?)"
        cur.execute(query, i)

# Ver Quantia Total
def ver_Quntia_Total():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Quantia")
        row = cur.fetchall()        

        for i in row:
            lista_itens.append(i)

    return lista_itens

# Atualizar Quantia 
def atualizar_quantia_total(i):
    with con:
        cur = con.cursor()
        query ="UPDATE Quantia SET valor=? WHERE id=?"
        cur.execute(query, i)
        
     