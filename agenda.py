import sqlite3, time

path = r'D:\SQLite\Agenda'

conectar = sqlite3.connect(path+r'\agenda.db')
c = conectar.cursor()

def criar_db():
    c.execute('CREATE TABLE IF NOT EXISTS cadastro (nome text, telefone text, email text)')

try:
    criar_db()
except:
    print('Erro ao criar o banco de dados')
else:
    print('Banco de dados criado com sucesso')
  
    
def inserir(n, t, e):
    c.execute("INSERT INTO cadastro VALUES(?, ?, ?)", (n, t, e))
    conectar.commit()
    
def pesquisar(p):
    sql = 'SELECT * FROM cadastro WHERE nome = ?'
    for row in c.execute(sql, (p,)):
        print(row)
    
fc = int(input('1 - Cadastrar \n2 - Pesquisar \nO que voce deseja fazer?'))
    
if fc == 1:
    
    try:
        print('Cadastro da Agenda')
        time.sleep(2)
        n = str(input('Digite um nome: '))
        t = str(input('Digite um telefone: '))
        e = str(input('Digite um email: '))
        inserir(n, t, e)
        
    except:
        print('Erro ao cadastrar')
        
    else:
        print('Cadastrado com sucesso')
        
elif fc == 2:
    print('Buscando')
    time.sleep(1)
    p = str(input('Digite o nome a ser buscado: '))
    pesquisar(p)
    
else:
    print('...')
        
