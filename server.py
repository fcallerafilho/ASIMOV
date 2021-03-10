from socket import *
    

meuhost = 'localhost'
minhaport = 30000
sockobj = socket(AF_INET, SOCK_STREAM)

sockobj.bind((meuhost, minhaport))
    
sockobj.listen(5)    
    
while True:
    conexao, endereco = sockobj.accept()
    print("O servidor esta conectado por", endereco)
    while True:
        data = conexao.recv(1024)
        if not data:
            break;
            conexao.send(b'Eco=>' + data)
        conexao.close()
            
        
        
    