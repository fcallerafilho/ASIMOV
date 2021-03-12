import sqlite3

path = r'D:\SQLite\Banco de Dados'

conn = sqlite3.connect(path+r'\teste.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS dados(id integer, valor real, \
              nome text, endereco texto, total real)')
    
create_table()

def inserirDados():
    c.execute("INSERT INTO dados VALUES(1, 50, 'Fernando', 'Rua A', 500)")
    c.execute("INSERT INTO dados VALUES(2, 250, 'Fernando', 'Rua A', 500)")
    conn.commit()
    
inserirDados()

sql = 'SELECT * FROM dados WHERE nome = ?'

def ler_dados(vlrbusca):
    for row in c.execute(sql, (vlrbusca,)):
        print(row) 
        
ler_dados('Fernando') 