from socket import *    

serverhost = 'localhost'
serverport = 30000
mensagem = [b'Ola, bem vindo!']
    
sockobj = socket(AF_INET, SOCK_STREAM)
    
sockobj.connect((serverhost, serverport))
    
for linha in mensagem:
    sockobj.send(linha)
        
data = sockobj.recv(1024)
print("cliente recebeu: ", data)
        
sockobj.close()
    
while True:
    conexao, endereco = sockobj.accept()
    print("O servidor esta conectado por", endereco)
    while True:
        data = conexao.recv(1024)
        if not data:
            break;
            conexao.send(b'Eco=>' + data)
    conexao.close()
        